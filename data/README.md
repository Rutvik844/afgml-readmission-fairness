# Data

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008 (UCI ML Repository, id 296)
**Source:** https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
**Licence:** listed on UCI as CC BY 4.0 (verify on the page before redistributing). Not redistributed in this repo.
**Access date:** TODO (date you downloaded it)
**SHA-256 of diabetic_data.csv:** TODO (printed by notebook cell 2, saved in its output bundle)

## Acquisition
```bash
python scripts/download_data.py --out data/raw      # local
python scripts/download_data.py --out /content      # Colab
```
or download manually and place `diabetic_data.csv` and `IDS_mapping.csv` in `data/raw/` (local),
in `/content` (Colab), or in Google Drive under `MyDrive/afgml dataset/` (the notebook searches all of these).

## Exclusions / preprocessing (from the report)
101,766 encounters → 2,423 expired/hospice discharges removed → 99,343 encounters, 69,990 patients.
`?` race kept as "Unknown". A1C `None` = test not performed → treated as missing. Race/gender/age used as recorded, never inferred.
Patient-disjoint splits (seed 42): 59,814 / 19,727 / 19,802 encounters.
