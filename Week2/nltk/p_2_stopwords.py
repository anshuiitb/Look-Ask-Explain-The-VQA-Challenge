from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence="This is an example showing off stop word filtration."

# print(stopwords.fileids())

stop_words = set(stopwords.words("english"))

# print(stop_words)

words = word_tokenize(example_sentence)

# filtered_sentence = []

# for i in words:
#     if i not in stop_words:
#         filtered_sentence.append(i)

# print(filtered_sentence)

filtered_sentence=[i for i in words if i not in stop_words]
print(filtered_sentence)