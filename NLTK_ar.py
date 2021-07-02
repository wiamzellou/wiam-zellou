from codecs import utf_16_be_decode
import nltk
import string
import arabic_reshaper
import bidi.algorithm



text = u'ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل'
text=arabic_reshaper.reshape(text)
text=bidi.algorithm.get_display(text)

#Remove punctuation
punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ''' + string.punctuation
text_p = "".join([char for char in text if char not in punctuations])
print(text_p)

#Word Tokenization
from nltk import word_tokenize
words = word_tokenize(text_p)
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

