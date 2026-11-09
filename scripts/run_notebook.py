"""Run notebooks/AFGML.ipynb headlessly (no Colab needed); outputs go under results/.
  python scripts/run_notebook.py --quick    # smoke test
  python scripts/run_notebook.py            # full run
Needs data/raw/diabetic_data.csv (see data/README.md)."""
import argparse, os, time
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    out = root / "results" / ("p2_outputs_quick" if a.quick else "p2_outputs")
    out.mkdir(parents=True, exist_ok=True)
    os.environ["P2_OUT"] = str(out)
    os.environ["P2_QUICK"] = "1" if a.quick else "0"
    nb = nbformat.read(root / "notebooks" / "AFGML.ipynb", as_version=4)
    t = time.time()
    # cwd = data/raw so the notebook's find_file(".") finds the CSV
    ExecutePreprocessor(timeout=-1, kernel_name="python3").preprocess(
        nb, {"metadata": {"path": str(root / "data" / "raw")}})
    nbformat.write(nb, out / "AFGML_executed.ipynb")
    print(f"Done in {time.time()-t:.0f}s -> {out}")

if __name__ == "__main__":
    main()
