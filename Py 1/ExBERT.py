from transformers import pipeline

analisador = pipeline("sentiment-analysis")
resultado = analisador("Eu amo programação!")
print(resultado)
