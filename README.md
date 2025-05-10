```markdown
# 📊 Projet : Analyse de la loi de Zipf sur un corpus de Victor Hugo

Ce projet a pour objectif d'explorer la **loi de Zipf** appliquée à un **corpus textuel** issu des œuvres de Victor Hugo. Il utilise Python, JupyterLab et des bibliothèques comme `nltk`, `matplotlib` et `collections`.

---

## 🗂️ Structure du projet

```

zipf-law-project/
├── data/
│   └── raw/                   # Corpus texte brut (non versionné)
├── notebooks/
│   └── analyse\_zipf.ipynb     # Notebook principal
├── scripts/                   # Scripts Python futurs (modulaires)
├── .gitignore                 # Exclusion des fichiers temporaires et lourds
└── README.md                  # Documentation du projet

````

---

## 🔍 Objectifs

- Nettoyage d’un corpus littéraire en français
- Tokenisation et filtrage linguistique
- Analyse de fréquence des mots
- Visualisation log-log des occurrences (loi de Zipf)
- Préparation à une comparaison avec la distribution théorique

---

## 📚 Données

- **Source** : œuvres de Victor Hugo (format `.txt`)
- **Emplacement** : `data/raw/Corpus_Victor_Hugo.txt`
- ⚠️ Les fichiers de données ne sont pas suivis par Git (`.gitignore`)

---

## 🛠️ Prérequis

- Python 3.x
- JupyterLab
- Anaconda (recommandé)
- Bibliothèques :
  ```bash
  pip install nltk matplotlib
````

---

## 🚀 Lancer le projet

1. Cloner le dépôt :

   ```bash
   git clone git@github.com:TON_UTILISATEUR/zipf-law-project.git
   cd zipf-law-project
   ```

2. Lancer JupyterLab :

   ```bash
   jupyter lab
   ```

3. Ouvrir `notebooks/analyse_zipf.ipynb`

---

## 📈 Extrait de visualisation

La fréquence des mots suit approximativement une décroissance log-log caractéristique de la loi de Zipf.

---

## 📌 À venir

* Ajout d'un tokenizer sur mesure (langue française)
* Comparaison avec modèle Zipf théorique
* Analyse sur d’autres auteurs (comparaison inter-corpus)

---

