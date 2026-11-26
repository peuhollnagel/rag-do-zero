from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import math


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

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

def buscar(pergunta, docs):
    
    pergunta_vet = embedding_pergunta(pergunta)
    
    for doc in docs:
        doc["score"] = cosseno(doc["vetor"], pergunta_vet)
        
    ordenados = sorted(docs, key=lambda doc: doc["score"], reverse=True)
    
    return ordenados[:3]

def responder(pergunta, contexto):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=(
            "Você responde perguntas usando apenas as notas fornecidas. "
            "Diga de qual nota tirou cada informação, usando o nome entre colchetes. "
            "Se a resposta não estiver nas notas, diga que não encontrou."
            "Nunca use conhecimento próprio nem ofereça usá-lo."
        ),
        input=f"{contexto}\n\nPergunta: {pergunta}"
    )
    return response.output_text


documentos = carregar_documentos("notas")
documentos = gerar_embeddings(documentos)

while True:
    pergunta = input("> ")

    if pergunta == "sair":
        break

    if not pergunta.strip():
        continue

    resultado = buscar(pergunta, documentos)
    contexto = montar_contexto(resultado)
    resposta = responder(pergunta, contexto)
    print()
    print(resposta)
    print()

