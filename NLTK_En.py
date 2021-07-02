import string
import nltk
from nltk.tokenize import sent_tokenize
#nltk.download()



text="Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as \"algebraic objects\". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a way which had not happened before."

#Convert text to lowercase
text=text.lower()
print(text)

#Remove punctuation
text_p = "".join([char for char in text if char not in string.punctuation])
print(text_p)

#Word Tokenization
from nltk import word_tokenize
words = word_tokenize(text_p)
wordss=sent_tokenize(text_p)
print(words)

#Stemming
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
print(stemmed)

#lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
for word in words:
    print(lemmatizer.lemmatize(word))

#POS Tagger
from nltk import pos_tag
pos = pos_tag(words)
print(pos)

#chunking
chunks = nltk.ne_chunk_sents(pos)
for tree in chunks:
    print(tree)

#parsing
from nltk.corpus import treebank
t=treebank.parsed_sents("Perhaps one of the most significant advances made by Arabic mathematics began at this time")
t.draw()

