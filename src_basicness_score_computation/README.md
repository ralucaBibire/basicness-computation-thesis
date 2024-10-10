# Basicness score computation

```bash
python -m venv .basicness-venv
source .basicness-venv/bin/activate
pip install -r requirements.txt
```
Attualmente `requirements.txt` non è completo.

Le varie features possono essere eseguite singolarmente e si creeranno dei csv nella cartella df.

Una volta ottenuti tutti i csv con le features, eseguire `merge_features.ipynb` che creerà il file `df_merged_features.csv` contenente tutte le features.

Il file `compute_basicness_score_ML.ipynb` utilizza le features del file `df_merged_features.csv` per calcolare i basicness score che saranno contenuti nel file `df_basicness_score.csv`.