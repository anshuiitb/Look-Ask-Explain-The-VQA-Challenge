import nltk
from nltk.corpus import wordnet

# sym = wordnet.synsets('computer')
# print(sym[0].definition())


synonyms=[]
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)

for syn in wordnet.synsets('Computer'):
    print(syn)


antonyms=[]
for syn in wordnet.synsets('small'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

print(antonyms)