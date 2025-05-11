from collections import Counter

def compter_mots(tokens, nb_stopwords=3):
    compteur = Counter(tokens)
    mots_a_supprimer = [mot for mot, _ in compteur.most_common(nb_stopwords)]
    tokens_nettoyes = [mot for mot in tokens if mot not in mots_a_supprimer]
    return Counter(tokens_nettoyes), mots_a_supprimer
