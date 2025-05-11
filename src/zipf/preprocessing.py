import re
from nltk.tokenize import TreebankWordTokenizer

def charger_texte(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ'\s-]", " ", texte)
    texte = re.sub(r"\s+", " ", texte).strip()
    return texte

def tokenizer_texte(texte):
    tokenizer = TreebankWordTokenizer()
    return tokenizer.tokenize(texte)
