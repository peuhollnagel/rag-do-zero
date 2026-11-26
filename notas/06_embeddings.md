# Embeddings

Embeddings são representações numéricas de dados, como textos, imagens ou áudio, na forma de vetores de números reais. A ideia central é que itens com significados semelhantes fiquem próximos no espaço vetorial.

Por exemplo, as palavras "cachorro" e "gato" terão embeddings mais próximos entre si do que "cachorro" e "computador". Um exemplo clássico do Word2Vec, criado pelo Google em 2013, mostra que o vetor de "rei" menos "homem" mais "mulher" resulta em algo próximo de "rainha".

A similaridade entre dois embeddings costuma ser medida pela similaridade de cosseno, que calcula o cosseno do ângulo entre os vetores. O resultado vai de -1 a 1, e quanto mais próximo de 1, mais semelhantes são os textos. A fórmula é o produto escalar dos vetores dividido pelo produto de suas normas.

Modelos de embedding modernos geram vetores com centenas ou milhares de dimensões. O modelo text-embedding-3-small da OpenAI, por exemplo, produz vetores de 1536 dimensões.
