import nltk
import matplotlib.pyplot as plt

text= """Welcome you to the programming knowledge. Lets start with our first tutorial on MLTK. We shall learn the basics of NLTK here."""
# from nltk.tokenize import word_tokenize

# print(word_tokenize(text))


# from nltk.tokenize import sent_tokenize

# print(sent_tokenize(text))

from nltk.tokenize import word_tokenize
word_tokenized=word_tokenize(text)


from nltk.probability import FreqDist
fd = FreqDist(word_tokenized)

print(fd.most_common(3))
fd.plot(30 , cumulative= False)
plt.show()