


from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    r"D:\math-for-ml\vectors\dolma_300_2024_1.2M.100_combined.txt",
    binary = False,
    no_header = True
)

king_vector = model['king']
man_vector = model['man']
woman_vector = model['woman']

print(king_vector)
print(man_vector)
print(woman_vector)

print(model.most_similar(positive = [king_vector - man_vector + woman_vector], topn = 1))