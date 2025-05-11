import argparse
from src.zipf.preprocessing import load_and_clean_text
from src.zipf.frequency import compute_word_frequencies
from src.zipf.plotting import plot_zipf_law

def main():
    parser = argparse.ArgumentParser(description="Analyse la loi de Zipf sur un corpus texte.")
    parser.add_argument("--input", type=str, default="data/raw/Corpus_Victor_Hugo.txt", help="Chemin du fichier texte.")
    parser.add_argument("--output-plot", type=str, default="results/zipf_plot.png", help="Chemin pour sauvegarder le graphique.")
    parser.add_argument("--min-freq", type=int, default=5, help="Fréquence minimale des mots à inclure.")
    args = parser.parse_args()

    # Pipeline
    text = load_and_clean_text(args.input)
    frequencies = compute_word_frequencies(text)
    plot_zipf_law(frequencies, args.output_plot, min_freq=args.min_freq)
    print(f"Analyse terminée ! Graphique sauvegardé sous {args.output_plot}.")

if __name__ == "__main__":
    main()