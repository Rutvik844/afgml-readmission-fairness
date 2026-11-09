# Requirement -> evidence matrix (Problem 2)

Status key: **VERIFY** = an evidence file exists in `results/manifest.json`; open it and confirm it really contains the item. **GAP** = nothing in the manifest covers it, or the report does not mention it. Change VERIFY to complete / partial / failed only after you have opened the file. Paths are relative to `results/`.

## A. Mandatory experiments (Problem 2)

| ID | Requirement | Evidence file(s) | Status | What to check / gap |
|---|---|---|---|---|
| P2-E1 | Patient-disjoint split; audit natural missingness by group | `tables/e1_missingness_race.csv`, `e1_missingness_race_gender.csv`, `figures/fig_e1_missingness_audit.png` | VERIFY | Report: A1C 16.2/18.4/25.0% by race; split asserted patient-disjoint |
| P2-E2 | Compare complete-case, imputation, indicator augmentation, probabilistic marginalization | `tables/e2_natural_comparison.csv`, `e2_bootstrap_intervals.csv`, `e2_group_recall_race_gender.csv` | VERIFY | Report Table 1 has LR-imp, LR-ind, HGB-ind, BN-marg, Complete-case. Confirm GB with plain imputation (no indicator) is present |
| P2-E3 | Inject MCAR, MAR and simulated MNAR missingness | `tables/e3_e4_shift_grid_all_seeds.csv`, `e3_e4_shift_grid_summary.csv`, `masking_realised_rates.csv` | VERIFY | Check all three mechanisms appear, and realised rates match targets |
| P2-E4 | Train under one mechanism, evaluate under altered rates / group dependence | `tables/e3_e4_shift_grid_*.csv`, `figures/fig_e4_shift_worst_group_recall.png` | VERIFY | Confirmatory test is train MAR@30 -> test MNAR@30 (`confirmatory_primary_test_holm.csv`) |
| P2-E5 | Fixed-capacity follow-up; fairness-utility-capacity trade-offs | `tables/e5_capacity_fairness_utility.csv`, `figures/fig_e5_capacity_tradeoffs.png` | VERIFY | Capacities 10/20/30% present |

## B. Ablations (Problem 2)

| ID | Requirement | Evidence | Status | What to check / gap |
|---|---|---|---|---|
| P2-A1 | Remove observation nodes | `tables/ablations.csv` row 'Remove observation nodes (drop Y->R): BN-obs -> BN-marg' | **partial** | The row drops the Y->R edge, not the R nodes. Notebook section 18 states R is outside Y's Markov blanket in BN-marg, so P(Y given evidence) ignores R by construction. Say this in the report and relabel the row 'remove Y->R sensitivity edge' |
| P2-A2 | Remove the fairness component | `tables/ablations.csv` (LR-ind+PAT -> LR-ind; BN-marg+PAT -> BN-marg) | **complete** | seen in notebook cell 28 |
| P2-A3 | Replace marginalization by single imputation | `tables/ablations.csv` (BN-marg -> BN-base; BN-obs -> BN-obs-imp) | **complete** | natural recall difference +0.0064 [-0.0018,+0.0146] |

## C. Robustness tests (Problem 2)

| ID | Requirement | Evidence | Status | What to check / gap |
|---|---|---|---|---|
| P2-R1 | Missingness rates 10%, 30%, 50% | `tables/e3_e4_shift_grid_summary.csv` | VERIFY | Config RATES = 0.1, 0.3, 0.5 (confirmed in config.json) |
| P2-R2 | Group-dependent masking | same grid (GRP scenario), report Fig. 2 | VERIFY | Report mentions "group-dependent" |
| P2-R3 | Alternative feature discretisation | `tables/robust_discretisation.csv` | VERIFY | |
| P2-R4 | Alternative treatment of unknown demographic categories | `tables/robust_unknown_demographics.csv` | VERIFY | |
| P2-R5 | (extra) smoothing strength, age audit | `tables/robust_smoothing.csv`, `robust_age_audit.csv` | VERIFY | Extra, not required |

## D. Baselines (Problem 2)

| ID | Requirement | Evidence | Status | What to check / gap |
|---|---|---|---|---|
| P2-B1 | LR and gradient boosting with imputation, repeated with indicators | LR-imp, LR-ind, HGB-imp, HGB-ind (notebook cells 16, 19) | VERIFY | Confirm an HGB-imp row exists in `e2_natural_comparison.csv`; Table 1 in the report omits it |
| P2-B2 | BN with imputed measurements, no observation nodes, matched variables | Table 1: BN-base | VERIFY | |
| P2-B3 | Reweighing after imputation | LR-imp+RW, LR-ind+RW (notebook cells 16, 19) | VERIFY | Implemented, but not in report Table 1: confirm the rows are in `e2_natural_comparison.csv` and mention them in the report |
| P2-B4 | Equal-opportunity threshold adjustment | Table 1: LR-ind+EO (uses race x gender at decision time) | VERIFY | Flagged comparator; fine |
| P2-B5 | Missingness-aware fairness comparator informed by [11] (Feng, Calmon, Wang 2023, "Adapting Fairness Interventions to Missing Values") | none | **GAP** | Your report cites Zhang & Long 2021 and Jeong et al. 2022 but **not Feng et al.**, which is the assigned reference. Either reproduce a documented restricted version, or state clearly that you did not and why |

## E. Metrics (Problem 2)

| ID | Requirement | Evidence | Status | What to check / gap |
|---|---|---|---|---|
| P2-M1 | Predictive: AP, AUROC, recall at capacity, precision among selected | `e2_natural_comparison.csv` (columns AUROC, AP, recall, precision) | **complete** | seen in your output; AUROC 0.622 for LR-imp |
| P2-M2 | Fairness: dEOpp, dEOdds, worst-group recall, gaps within missingness patterns | `e2_natural_comparison.csv` (rg_dEOpp, rg_dEOdds, rg_dDP, rg_Rsel, rg_worst_tpr), `e2_gaps_within_missingness_patterns.csv` | **complete** (open the patterns file to confirm) | dEOdds point estimates exist; the bootstrap interval table has no dEOdds interval (minor) and the report omits dEOdds |
| P2-M3 | Probabilistic: log loss, Brier, group calibration, masked-value accuracy | `e2_natural_comparison.csv` (logloss, brier), `probabilistic_metrics.csv` (ECE), `group_calibration_race.csv`, `e3_masked_value_accuracy.csv` | **complete** (open group calibration file to confirm) | Group calibration is by race only: state that |
| P2-M4 | Secondary: equalized odds and group calibration as secondary criteria | as above | VERIFY | |

## F. Statistics, graph analysis, deliverables

| ID | Requirement | Evidence | Status | What to check / gap |
|---|---|---|---|---|
| C-SPLIT | Patient-disjoint split, test frozen | `cards/preregistration.json`, config (SPLIT_SEED 42) | VERIFY | |
| C-SEEDS | At least 5 seeds | `config.json` SEEDS 0-4 | **complete** | seen in your config.json |
| C-BOOT | At least 1,000 patient-cluster bootstraps | `config.json` N_BOOT 1000, `e2_bootstrap_intervals.csv` | **complete** (config) | |
| C-HOLM | Declared confirmatory family with Holm | `tables/confirmatory_primary_test_holm.csv` | VERIFY | Report: 3 comparisons, Holm p = 1.000 |
| C-SMALL | Group n, denominators, selection rate, TPR/FPR; <30 flagged exploratory | `e2_group_recall_race_gender.csv` (n, n_pos, n_neg, exploratory, recall per method) | **partial** | Denominators and exploratory flag present. The saved table has recall only: **no per-group selection rate or FPR table is in the manifest**, although the notebook computes them (cell 7). Add a saved table |
| C-GM1 | Normalisation, factor scopes, evidence handling | notebook cell 13 (CPTs normalised, |sum-1|<1e-9, scopes checked), `graphical_model_validation.csv` | VERIFY | |
| C-GM2 | Exact VE vs clique-tree agreement within stated tolerance | `tables/graphical_model_validation.csv` | **complete** | Max abs error 2.8e-17 (clique tree), 5.6e-17 (pgmpy VE), 0 vs brute force; tolerance TOL = 1e-8 (notebook cell 13) |
| C-GM3 | d-separation / conditional-independence checks | `tables/dseparation_statements.csv` | VERIFY | |
| P2-G1 | Paths linking protected attributes, observation indicators and predictions; marginalization, evidence propagation, Markov blanket | `dseparation_statements.csv`, `evidence_propagation_example.csv`, `figures/fig_graph_dags.png`, notebook section 18 | **complete** (notebook prints Markov blankets of Y for BN-marg and BN-obs) | Copy the Markov-blanket sentence into the report |
| C-SIM | Synthetic/semi-synthetic labelled as such | report Sec. 4, `assumptions.md` A7 | VERIFY | |
| P2-D1 | Missingness audit | E1 files | VERIFY | |
| P2-D2 | Masking generator | notebook section 12 | VERIFY | Cite notebook cell |
| P2-D3 | Patient-level splitting script | notebook | VERIFY | It is in the notebook, not a separate script: say so |
| P2-D4 | Assumption-specific results | E3/E4 grid by mechanism | VERIFY | |
| C-CARDS | Data card, model card, assumptions register | `docs/data_card.md`, `model_card.md`, `assumptions.md` | **complete** | copied from the full run |
| C-DOCS | Proposal and related-work table (at least 8 papers) | `docs/proposal.md`, `related_work.md` | **GAP** | Still TODO; report cites 4 related-work papers; Feng et al. 2023 must be added |
| C-MS | 8-10 page manuscript with reproducibility appendix | `report/` | **GAP** | Current report is the 2-3 page evaluation report only |
| C-DEMO | Demonstration, oral defence, individual statements | `demo/`, `docs/contributions.md` | **GAP** | TODO |
| P2-ETH | Ethical questions (missingness as access, denial of follow-up, incomplete label) | report Sec. 4 | VERIFY | Report covers all three briefly |
