from transformers import pipeline

gerador = pipeline("text-generation", model="gpt2")
print(gerador("Era uma vez", max_length=50))
