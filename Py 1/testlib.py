from transformers import pipeline

nlp = pipeline("sentiment-analysis")
print(nlp("Este curso é incrível!"))
