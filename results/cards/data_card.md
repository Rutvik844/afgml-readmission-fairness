# Data card — Diabetes 130-US Hospitals (Problem 2)
- **Source / version**: https://archive.ics.uci.edu/dataset/296 · file `diabetic_data.csv` · sha256 `0689e7ec031237dc…` · 101,766 encounters × 50 columns
- **Licence**: Listed on the UCI page as CC BY 4.0 (verify before redistribution)
- **Inclusion**: all encounters except discharge dispositions [11, 13, 14, 19, 20, 21] (expired/hospice; readmission undefined) → 2,423 removed, 99,343 kept (69,990 patients).
- **Label**: Y=1 iff `readmitted == '<30'`; '>30' and 'NO' → Y=0. Absence of a recorded readmission is *not* proof of no readmission elsewhere.
- **Protected attributes** (recorded categories, not inferred): race (AfricanAmerican, Asian, Caucasian, Hispanic, Other, Unknown='?'), gender (incl. 3 'Unknown/Invalid'), age band (secondary).
- **Measurements with an observation indicator**: A1C result (naturally missing = test not performed, 83.1%); number of diagnoses (complete in raw data; masked only in semi-synthetic experiments).
- **Covariates**: prior inpatient visits (0/1/2+), prior outpatient+ED visits (0/1/2+), primary-diagnosis group (6 classes).
- **Not used**: encounter_id order (not temporal), hospital identifiers (absent) → no hospital-level or temporal claims.
- **Unit of dependence**: patient (multiple encounters per patient) → all splits/bootstraps are patient-level.
