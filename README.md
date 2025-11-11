# Paveikslėlio apibūdinimo programa (Streamlit + Ollama)

Trumpa programa, kuri leidžia įkelti paveikslėlį per naršyklę (Streamlit) ir naudoja Ollama modelį `gemma3:4b` paveikslėlio aprašymui.

## Reikalavimai
- Paleista Ollama (lokaliai) ir turimas modelis `gemma3:4b`.
- Python 3.9+ (arba jūsų sistemoje palaikoma versija).

## Diegimas

Atidarykite PowerShell ir įdiekite reikalingas priklausomybes:

```powershell
python -m pip install -r requirements.txt
```

## Kaip paleisti

1. Įsitikinkite, kad Ollama veikia lokaliai (pvz. `ollama serve` arba kita jūsų įprasta komanda) ir modelis `gemma3:4b` yra prieinamas.
2. Paleiskite Streamlit:

```powershell
streamlit run app.py
```

3. Atidarykite naršyklę (Streamlit atidarys automatiškai arba atidarykite http://localhost:8501) ir įkelkite paveikslėlį.

## Pastabos
- Jei gaunate klaidą kviečiant modelį, patikrinkite Ollama serverio log'us ir ar modelis užkrautas.
- Programoje naudojame paprastą užklausos formą: siunčiame paveikslėlio baitus lauke `images` ir prašome modelio pateikti lietuvišką aprašymą.
# lecture-GitHub
project testing 
