import spacy


nlp = spacy.load('en_core_web_sm')
with open("./wiki_us.txt", "r") as f:
	text = f.read()

print(text)

# just one doc object in the script (good practice)
doc = nlp(text)

# see differences between doc onject and text "object"
for token in text[:10]:
	print(token)

print()

for token in doc[:10]:
	print(token)

print()

# not equal just to spit method:
for token in text.split()[:10]:
	print(token)

# sentence boundary detection
for sent in doc.sents:
	print(sent)

print()
sentence1 = list(doc.sents)[0]
print("Sentence 1:", sentence1)

# token attributed
for token in doc[:20]:
	print(token, 
	token.text, 
	token.left_edge, 
	token.right_edge, 
	token.ent_type, 
	token.ent_type_,
	token.ent_iob_,
	token.lemma_,
	token.morph,
	token.pos_,
	token.dep_,
	token.lang_)


# vord vectors in spacy
text = "Mike enjoys playing football."
doc2 = nlp(text)
print(doc2)

for token in doc2:
	print(token.text, token.pos_, token.dep_)

from spacy import displacy
displacy.render(doc2, style="dep")

# named entity reognition
for ent in doc.ents:
	print(ent.text, ent.label_)

displacy.render(doc2, style="ent")
