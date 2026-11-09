# Model card
(The notebook also writes cards/model_card.md; after the final run copy it here.)
- **Purpose:** research audit of missing-data handling for a 30-day readmission follow-up service. Not for clinical use.
- **Models:** LR / HistGradientBoosting (imputation ± indicators), complete-case LR, BN-base, BN-marg, BN-obs, BN-obs-imp, PAT threshold rule, group-aware EO baseline (flagged comparator).
- **Inputs:** age, prior inpatient visits, prior outpatient/ED visits, diagnosis group, number of diagnoses, A1C + availability indicators.
- **Protected attributes at prediction time:** none, except the EO baseline (race×gender at decision time).
- **Performance:** AUROC ≈ 0.62; recall@20% ≈ 0.31–0.33. Group performance and calibration: results/tables and report Table 1.
- **Prohibited extrapolation:** prospective, hospital-level, temporal or clinical-deployment claims.
- **Limitations:** weak signal; A1C missingness reflects care/documentation, so ranking can penalise poorly documented patients; human review required.
