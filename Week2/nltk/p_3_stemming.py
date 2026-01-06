from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

ps= PorterStemmer()

example_words=["pyhton","pythoner","pythoning","pythoned","pythoniy"]

for i in example_words:
    print(ps.stem(i))



new_text="It is very important to be pyhtonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for i in words:
    print(ps.stem(i))