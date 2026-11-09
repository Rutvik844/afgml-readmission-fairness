# Fair Readmission Prediction with Explicit Models of Missing Clinical Data
ICT 5143 – Algorithms, Fairness and Graphical Models Laboratory · **Problem 2**
Team: Rutvik Gokhale (261090830002), Harshad K (261090830011)

## Question and contribution
Does explicitly modelling A1C availability (Bayesian network with observation nodes, EM + exact variable elimination) reduce the deterioration of worst-group recall when missingness shifts from MAR@30% (train) to MNAR@30% (test)?
Data: UCI Diabetes 130-US Hospitals (99,343 encounters, 69,990 patients). Y=1: recorded 30-day readmission. D = race×gender cells (≥30 test positives).
Closest method reproduced: TODO

## Headline findings (from report/AFGML_Report.pdf)
- Qualified negative result: BN-marg gave no significant worst-group-recall advantage over LR-imp, LR-ind or BN-base after Holm correction (all Holm p = 1.000).
- AUROC ≈ 0.62; recall@20% ≈ 0.31–0.33 for all models. Only four race×gender cells have ≥30 positives.
- The pattern-aware threshold rule (PAT) did not improve ΔEOpp; complete-case LR is worst (worst-group recall 0.2059, ΔEOpp 0.2077; different population).
Full tables: `results/`. Evidence: `docs/`.

## Run in Google Colab (recommended)
1. Push this repo to GitHub (see below).
2. In Colab: **File → Open notebook → GitHub**, paste your repo URL, open `notebooks/AFGML.ipynb`. Optionally set Runtime → GPU (not required).
3. Add a first cell:
   ```python
   !git clone https://github.com/<your-username>/<your-repo>.git /content/repo
   %cd /content/repo
   !pip install -q -r requirements.txt
   !python scripts/download_data.py --out /content   # or put the CSVs in Drive: MyDrive/afgml dataset/
   ```
4. Set `QUICK = True` in the setup cell for a smoke test (≈ minutes; cannot support headline claims), or leave False for the full run.
5. Run all. Outputs go to `/content/p2_outputs`; the last cell offers a zip download. Unzip it into `results/` and commit.

## Run locally (optional)
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python scripts/download_data.py --out data/raw
python scripts/run_notebook.py --quick                 # smoke test
python scripts/run_notebook.py                         # full run -> results/p2_outputs
python -m pytest tests
```
Status of these commands: TODO (mark "tested on <date>, <hardware>" only after running from a clean clone). Full-run runtime/hardware: TODO.

## Evidence index
`docs/protocol.md` · `docs/requirements_matrix.md` · `docs/related_work.md` · `docs/data_card.md` · `docs/model_card.md` · `docs/assumptions.md` · `docs/contributions.md` · `report/` · `slides/` · `demo/README.md` · `results/manifest.csv`

## Contributions and attribution
See `docs/contributions.md`. Data: UCI (CC BY 4.0, verify). Libraries: pgmpy, fairlearn, scikit-learn. AI assistance disclosure: TODO.

## Ethics
Audit only, not for clinical use. Synthetic MNAR/group-dependent masks are simulations, not hospital mechanisms.
