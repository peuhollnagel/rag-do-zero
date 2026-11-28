from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import math

load_dotenv()

LIMITE_SCORE = 0.4

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def cosseno(a, b):
    sqA = 0
    sqB = 0
    result = 0
    
    for x, y in zip(a, b):
        result += x * y
        sqA += x * x
        sqB += y * y
        
    modA = math.sqrt(sqA)
    modB = math.sqrt(sqB)
    
    cos = result / (modA * modB)
    return cos

def montar_contexto(array):
    contexto = []
    for nota in array:
        contexto.append(f"[{nota['nota']}]\n{nota['conteudo']}")
    contexto_str = "\n\n".join(contexto)
    return contexto_str
        
def carregar_documentos(pasta):
    notas = []
    for caminho in Path(pasta).glob("*.md"):
        with open(caminho, 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip():
                notas.append({
                    "nota": caminho.name,
                    "conteudo": conteudo
                })
    return notas

def dividir_por_paragrafo(texto):
    cortado = texto.split("\n\n")
    return [p.strip() for p in cortado if p.strip()]

def gerar_embeddings(docs):
    conteudos = [doc["conteudo"] for doc in docs]
    
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=conteudos
    )   
    
    for doc, item in zip(docs, response.data):
        doc["vetor"] = item.embedding     
    return docs

def embedding_pergunta(pergunta):
    
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=pergunta
    )
    
    return response.data[0].embedding

def buscar(pergunta, docs):
    
    pergunta_vet = embedding_pergunta(pergunta)
    
    for doc in docs:
        doc["score"] = cosseno(doc["vetor"], pergunta_vet)
        
    ordenados = sorted(docs, key=lambda doc: doc["score"], reverse=True)
        
    return list(filter(lambda doc: doc["score"] >= LIMITE_SCORE, ordenados[:3]))

def responder(pergunta, contexto):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=(
            "Você responde perguntas usando apenas as notas fornecidas. "
            "Diga de qual nota tirou cada informação, usando o nome entre colchetes. "
            "Se a resposta não estiver nas notas, diga que não encontrou. "
            "Nunca use conhecimento próprio nem ofereça usá-lo. "
        ),
        input=f"{contexto}\n\nPergunta: {pergunta}"
    )
    return response.output_text

def dividir_em_chunks(texto, tamanho, sobreposicao):
    chunk = []
    inicio = 0
    while inicio < len(texto):
        fim = inicio + tamanho
        chunk.append(texto[inicio:fim])
        inicio += tamanho - sobreposicao
    return chunk

def criar_chunks(documentos, tamanho, sobreposicao):
    chunks = []
    for documento in documentos:
        contador = 0
        doc_chunks = dividir_por_paragrafo(documento["conteudo"])
        for chunk in doc_chunks:
                chunks.append({
                    "nota": documento["nota"],
                    "parte": contador,
                    "conteudo": doc_chunks[contador]
                })
                contador += 1
    return chunks

if __name__ == "__main__":
    documentos = carregar_documentos("notas")
    chunks = criar_chunks(documentos, 800, 100)
    chunks = gerar_embeddings(chunks)

    while True:
        pergunta = input("> ")

        if pergunta == "sair":
            break

        if not pergunta.strip():
            continue

        resultado = buscar(pergunta, chunks)
        
        if not resultado:
            print()
            print("Essa informação não está nos documentos")
            print()
            continue
        
        contexto = montar_contexto(resultado)
        resposta = responder(pergunta, contexto)
        print()
        print(resposta)
        print()

