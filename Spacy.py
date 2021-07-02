import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
nlp
#assign the english test to a variable
Engtext="""Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a
way which had not happened before."""
#calling the variable to examine the output 
Engtext
#feed the string object under 'Engtext' to the language object under 'nlp'
#store  the result under doc 
doc=nlp(Engtext)
#call the variableto examine the object 
doc
print(doc)
#tokenization
for token in doc:
    print(token)
#part of speech tagging 
for token in doc:
    print(token,token.pos_,token.tag_)
#morphological analysis 
for token in doc:
    print(token,token.morph)
#parsing 
for token in doc:
    print(token,token.dep_)
#print the index of current token ,the token,the token itself,the dependency,...
    print(token.i,token,token.dep_,token.head.i,token.head)

#visualising 
displacy.render(doc,style='dep',options={'compact':True})
#sentence segmentation 
#loop over sentences in the doc object and count thenm using enumarate ()
for number,sent in enumerate(doc.sents):
#print the token and it's dependency tag
    print(number,sent)
#lemmatizing 
for token in doc:
    print(token,token.lemma_)



   

