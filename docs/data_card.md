# Data card
(The notebook also writes cards/data_card.md; after the final run, copy it here and reconcile.)
- **Population:** diabetic hospital encounters, 130 US hospitals, 1999–2008; 99,343 encounters / 69,990 patients after excluding 2,423 expired/hospice discharges.
- **Label:** Y=1 = recorded readmission within 30 days (P(Y=1)=0.114). Deaths, outside-hospital readmissions and loss to follow-up are not observed.
- **Demographics:** race (6 recorded categories, "?" = Unknown), gender (3), age band: as recorded, never inferred. Race/gender are not model inputs.
- **Missingness:** A1C unmeasured in 83.1% of encounters, kept as missing. MCAR/MAR/MNAR/group-dependent masks are synthetic.
- **Sampling unit / dependence:** patient is the independent unit; patient-disjoint splits, patient-cluster bootstrap.
- **Limitations:** no hospital identifiers; encounter_id is not temporal order; only four race×gender cells have at least 30 test positives.
- **Access:** public (UCI); not redistributed here (see data/README.md).
