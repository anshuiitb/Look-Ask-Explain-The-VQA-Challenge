import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text= """Welcome you to the programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demowords = ["playing" , "happiness" , "going","doing" , "yes" , "no" , "I", "having" , "had" , "haved", "coding" , "programming" , "code", "program" ]

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# stemmed_words = [stemmer.stem(i)  for i in (demowords)]
# lemmatized_words = [lemmatizer.lemmatize(i.lower() ,"v") for i in demowords]

# print(stemmed_words,"\n" ,lemmatized_words)

sia = SentimentIntensityAnalyzer()

print(sia.polarity_scores("This is not good at all"))
