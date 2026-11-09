import sys, numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.fairness_metrics import *

def test_known_values():
    y = np.array([1,1,0,0, 1,1,0,0]); s = np.array([1,1,0,0, 1,0,0,1]); g = np.array(list("aaaabbbb"))
    r = group_stats(y, s, g, min_n=1)
    assert r["a"]["tpr"] == 1.0 and r["b"]["tpr"] == 0.5
    assert eopp_gap(r, min_pos=1) == 0.5
    assert dp_gap(r) == 0.0
    assert eodds_gap(r) == 0.5

def test_ratio_undefined_when_nobody_selected():
    r = group_stats([1,0,1,0], [0,0,0,0], list("aabb"), min_n=1)
    assert np.isnan(selection_ratio(r))

def test_small_group_flagged():
    r = group_stats([1]*10+[0]*10, [1]*20, ["a"]*20, min_n=30)
    assert r["a"]["exploratory"]
