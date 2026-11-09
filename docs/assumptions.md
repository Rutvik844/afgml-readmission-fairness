# Assumptions register — Problem 2
| # | Assumption | Where used | How checked / limitation |
|---|------------|-----------|--------------------------|
| A1 | Recorded '<30' readmission is the outcome; no readmission recorded = Y=0 | label | cannot detect readmission elsewhere |
| A2 | Ignorable availability: RA, RN ⟂ (outcome, unobserved values) | given (race, gender, age, C, H) | BN-marg; CMH test on first encounters (§9b); MAR for the unobserved value itself is UNTESTABLE |
| A3 | Non-ignorable sensitivity: Y -> R | BN-obs | explicit sensitivity model; controlled MNAR simulation (§12-13) |
| A4 | Patient is the independent unit; encounters of one patient are dependent | splits, bootstraps | patient-disjoint split asserted; cluster bootstrap |
| A5 | Race/gender are recorded categories; 'Unknown'/'Invalid' kept as exploratory groups | audit | robustness (c) in §17 |
| A6 | Age band is a clinical predictor AND a secondary audit dimension | models, audit | §17(d) |
| A7 | Synthetic masks (MCAR/MAR/MNAR/GRP) are mechanisms known by construction | §12-14 | labelled synthetic; not facts about hospitals |
| A8 | Fixed follow-up capacity; selection = top-k within the evaluated batch | all decision metrics | capacities 10/20/30% (§15) |
| A9 | Group-aware EO baseline uses race x gender at decision time | baseline only | flagged in tables |
| A10| Associational graphs; no causal claim about race, gender or testing | graph analysis | §18 |
