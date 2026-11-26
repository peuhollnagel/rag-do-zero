# RAG (Retrieval-Augmented Generation)

RAG (Retrieval-Augmented Generation, ou Geração Aumentada por Recuperação) é uma técnica que combina a busca de informações com modelos de linguagem. O termo foi popularizado por um artigo de pesquisadores da Meta (Facebook AI Research) publicado em 2020.

O funcionamento básico tem três etapas:
1. Indexação: os documentos são divididos em pedaços (chunks) e convertidos em embeddings, que são vetores numéricos representando o significado do texto.
2. Recuperação: quando o usuário faz uma pergunta, ela também é convertida em embedding, e os chunks mais parecidos são buscados, geralmente usando similaridade de cosseno.
3. Geração: os chunks recuperados são inseridos no prompt como contexto, e o modelo de linguagem gera a resposta baseada neles.

A principal vantagem do RAG é permitir que o modelo responda com base em informações que não estavam nos seus dados de treinamento, como documentos internos de uma empresa, reduzindo alucinações. Bancos de dados vetoriais como Pinecone, Chroma, Weaviate e pgvector são comumente usados para armazenar os embeddings.
