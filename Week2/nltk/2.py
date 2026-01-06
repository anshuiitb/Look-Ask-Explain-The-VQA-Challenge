import nltk

from nltk.corpus import stopwords

text= """Welcome you to the programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

stop_words = stopwords.words("english")
# demowords = ["playing" , "happiness" , "going","doing" , "yes" , "no" , "I", "having" , "had" , "haved" ]

# demo_after_stopwords=[i for i in demowords if i.lower() not in stop_words]
# print(demo_after_stopwords)




from nltk.tokenize import sent_tokenize , word_tokenize

print(word_tokenize(text),"\n", sent_tokenize(text))

