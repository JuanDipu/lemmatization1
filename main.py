import nltk

# Raiz de la palabra
# Busca la raíz de los plurales
# Verbos irregulares
# nltk.download("wordnet") se tiene que instalar
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("dogs"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("better :", lemmatizer.lemmatize("driven", pos="a"))  # 'a' stands for 'adjective'

print("improving :", lemmatizer.lemmatize("driven"))
