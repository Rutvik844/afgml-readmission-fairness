# Protocol
- **Split:** patient-disjoint GroupShuffleSplit, seed 42 → 59,814 / 19,727 / 19,802 encounters. Preprocessing, EM, thresholds and PAT offsets use train/validation only; test frozen.
- **Primary utility:** recall@20% capacity; acceptable loss ≤ 0.01 vs LR-ind. Capacities 10%/30% are robustness checks.
- **Primary fairness:** ΔEOpp (range of TPR) across race×gender cells with ≥30 test positives; worst-group recall alongside.
- **Seeds:** 5 (0–4) for masking/model randomness.
- **Uncertainty:** 1,000 patient-cluster bootstrap replicates, paired.
- **Confirmatory family (Holm):** BN-marg vs LR-imp / LR-ind / BN-base, deterioration of worst-group recall, train MAR@30% → test MNAR@30%. All else exploratory.
- **Masking scenarios:** MCAR, MAR, MNAR, group-dependent at 10–50%.
