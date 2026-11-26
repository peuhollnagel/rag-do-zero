from openai import OpenAI
from dotenv import load_dotenv
import os
import math

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

frases = [
    "Queria ficar rico",
    "quero arrecadar muito dinheiro",
    "estou indo comprar um caderno",
    "vou comprar um material para escrever",
]

client = OpenAI(api_key=api_key)

embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=frases
)

listaVet = [n.embedding for n in embedding.data]

def produto_escalar(a, b):
    result = 0
    for x, y in zip(a, b):
        result += x * y
    return result

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


for i in range(len(listaVet)):
    for j in range(i + 1, len(listaVet)):
        cos = cosseno(listaVet[i], listaVet[j])
        prod = produto_escalar(listaVet[i], listaVet[j])
        print(f"{frases[i][:25]} x {frases[j][:25]}: cos {cos:.6f} | produto {prod:.6f}")

     