from codecs import utf_16_be_decode
import string
import arabic_reshaper
import bidi.algorithm
from transformers import BertModel, BertTokenizer



text = u'ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل'
text=arabic_reshaper.reshape(text)
text=bidi.algorithm.get_display(text)

#Tokenization
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print(f' Sentence: {text}')
print(f'   Tokens: {tokens}')
print(f'Token IDs: {token_ids}')
