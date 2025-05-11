import matplotlib.pyplot as plt
import numpy as np

def tracer_zipf(mots_freq, titre="Loi de Zipf", debut=1):
    frequences = [freq for _, freq in mots_freq]
    rangs = np.arange(1, len(frequences) + 1)
    
    # Courbe théorique
    zipf_theorique = [frequences[debut - 1] / r for r in rangs[debut - 1:]]
    
    # Tracé
    plt.figure(figsize=(8, 6))
    plt.plot(rangs, frequences, marker='o', linestyle='-', color='darkblue', label="Données observées")
    plt.plot(rangs[debut - 1:], zipf_theorique, linestyle='--', color='red', label="Zipf théorique")
    
    plt.xscale('log')
    plt.yscale('log')
    plt.title(titre)
    plt.xlabel("Rang (log)")
    plt.ylabel("Fréquence (log)")
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()