import numpy as np
from cosine import cosine, cosineNP
import time

start = time.time()
embenddings = {}

with open(
    r'D:\math-for-ml\vectors\dolma_300_2024_1.2M.100_combined.txt',
    "r",
    encoding="utf-8"
    ) as emb:
    for line in emb:

        word, vector_str = line.split(" ", 1)
        vector = np.fromstring(vector_str.strip(), sep=" ", dtype=np.float64)
        embenddings[word] = vector

print('success read...')
print('king:', embenddings['king'])

king_vector = embenddings['king']
similarities = []

for word, vector in embenddings.items():
    if word == 'king':
        continue

    cos = cosineNP(king_vector, vector)
    mycos = cosine(king_vector, vector)
    similarities.append((word, cos, mycos))

similarities.sort(key = lambda x: x[1], reverse=True)
print(similarities[:5]) 

end = time.time()
print("Время выполнения:", end - start, "секунд")