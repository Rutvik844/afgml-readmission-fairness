"""Reference implementations of the metric definitions in AFGML_Repository_Guide.md.
Used by tests/ as an independent cross-check of the notebook's numbers."""
import numpy as np

def group_stats(y_true, y_sel, groups, min_n=30):
    y_true, y_sel, groups = map(np.asarray, (y_true, y_sel, groups))
    rows = {}
    for g in np.unique(groups):
        m = groups == g
        pos, neg = int((y_true[m] == 1).sum()), int((y_true[m] == 0).sum())
        rows[g] = dict(n=int(m.sum()), pos=pos, neg=neg, sel=float(y_sel[m].mean()),
                       tpr=float(y_sel[m][y_true[m] == 1].mean()) if pos else np.nan,
                       fpr=float(y_sel[m][y_true[m] == 0].mean()) if neg else np.nan,
                       exploratory=pos < min_n)
    return rows

def _range(vals):
    v = [x for x in vals if not np.isnan(x)]
    return max(v) - min(v) if v else np.nan

def dp_gap(rows): return _range([r["sel"] for r in rows.values()])
def eopp_gap(rows, min_pos=30): return _range([r["tpr"] for r in rows.values() if r["pos"] >= min_pos])
def eodds_gap(rows): return max(_range([r["tpr"] for r in rows.values()]), _range([r["fpr"] for r in rows.values()]))
def selection_ratio(rows):
    s = [r["sel"] for r in rows.values()]
    return np.nan if max(s) == 0 else min(s) / max(s)   # undefined when denominator is zero
