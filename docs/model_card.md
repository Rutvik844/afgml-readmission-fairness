# Model card — readmission risk models (Problem 2)
**Intended use**: research benchmark / audit of missing-data handling; NOT for clinical deployment or real follow-up allocation.
**Models**: LR and gradient boosting (imputation +/- indicators), complete-case LR, Bayesian networks BN-base / BN-marg / BN-obs / BN-obs-imp, fairness baselines (reweighing, group-aware EO thresholds) and the proposed missingness-pattern-aware threshold rule.
**Inputs**: age, prior inpatient / outpatient+ED visits, primary-diagnosis group, number of diagnoses, A1C (+ availability indicators). **No scoring model uses race or gender at prediction time.**
**Evaluation**: patient-disjoint train/val/test; capacity 20%; patient-cluster bootstrap (B=1000); seeds [0, 1, 2, 3, 4].
**Headline (natural test)**:
```
                AP  recall  rg_worst_tpr  rg_dEOpp
method                                            
LR-ind      0.1665  0.3326        0.2744    0.0909
BN-marg     0.1677  0.3294        0.2977    0.0780
LR-ind+PAT  0.1665  0.3384        0.2744    0.0973
```
**Known limitations**: weak discrimination (AUROC ~0.62); few adequately supported race x gender cells; label is recorded readmission only; 1999-2008 data; availability reflects access.
