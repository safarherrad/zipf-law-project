from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from src.zipf.preprocessing import load_and_clean_text
from src.zipf.frequency import compute_word_frequencies
from src.zipf.plotting import plot_zipf_law
import tempfile
import os

app = FastAPI(title="API Zipf Analysis")

@app.get("/analyze/")
async def analyze_zipf(
    input_path: str = "data/raw/Corpus_Victor_Hugo.txt",
    min_freq: int = 5
):
    try:
        # Pipeline
        text = load_and_clean_text(input_path)
        frequencies = compute_word_frequencies(text)
        
        # Crée un fichier temporaire pour le plot
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            plot_path = tmp.name
            plot_zipf_law(frequencies, plot_path, min_freq=min_freq)
        
        return FileResponse(plot_path, media_type="image/png", filename="zipf_plot.png")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if os.path.exists(plot_path):
            os.remove(plot_path)  # Nettoie le fichier temporaire

@app.get("/")
async def home():
    return {"message": "Utilisez /analyze/?input_path=...&min_freq=..."}