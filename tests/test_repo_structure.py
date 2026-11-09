import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md","LICENSE",".gitignore","requirements.txt","data/README.md","docs/protocol.md",
            "docs/requirements_matrix.md","docs/data_card.md","docs/model_card.md","docs/assumptions.md",
            "docs/contributions.md","docs/related_work.md","docs/proposal.md","notebooks/AFGML.ipynb","demo/README.md"]

def test_files_exist():
    missing = [p for p in REQUIRED if not (ROOT/p).exists()]
    assert not missing, missing

def test_no_todo_left_before_submission():
    # Fails the check while any TODO remains. Before submitting this must PASS.
    hits = [str(p.relative_to(ROOT)) for p in list(ROOT.glob("docs/*.md"))+[ROOT/"README.md", ROOT/"data/README.md"]
            if "TODO" in p.read_text()]
    assert not hits, f"TODO placeholders remain in: {hits}"
