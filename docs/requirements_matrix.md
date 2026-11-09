# Requirement → evidence matrix
Status: complete / partial / failed / missing. One row per independently checkable requirement.
**You must do:** copy every numbered experiment, ablation and robustness test of Problem 2 from AFGML_Research_Capstone_Problems.tex into the P2-* rows (I did not have that file, so they are empty on purpose).

| ID | Requirement | Config / command | Artifact and key finding | Status / limitation | Report / slide |
|---|---|---|---|---|---|
| C-GM | Exact VE and clique-tree agreement on a tractable instance | notebook graphical-model section; `python scripts/run_notebook.py --quick` | TODO max abs error + tolerance | TODO | Report §4 Reproducibility |
| C-STAT | Paired uncertainty on valid sampling unit | configs/main.yaml, 1,000 patient-cluster bootstraps | Report Table 2 | TODO | Report §3 |
| C-SEEDS | At least 5 seeds | configs/main.yaml | seeds 0–4 | TODO | Report §2 |
| C-SPLIT | Patient-disjoint split, frozen test | split_seed 42 | 59,814/19,727/19,802, no overlap asserted | TODO | Report §2 |
| C-GROUPN | Group n, denominators, selection rate, TPR/FPR; <30 flagged exploratory | notebook audit sections | TODO | TODO | Report Table 1 note |
| C-CARDS | Data card, model card, assumptions | docs/ | TODO | TODO | – |
| P2-E1 | TODO copy from .tex | | | | |
| P2-E2 | TODO | | | | |
| P2-A1 | TODO ablation | | | | |
| P2-R1 | TODO robustness | | | | |
