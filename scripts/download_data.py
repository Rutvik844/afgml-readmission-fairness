"""Download and unzip the UCI Diabetes 130-US Hospitals dataset (id 296).
Usage: python scripts/download_data.py --out data/raw
If the URL has changed, download manually from the UCI page listed in data/README.md."""
import argparse, hashlib, io, urllib.request, zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/raw")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    print("Downloading", URL)
    blob = urllib.request.urlopen(URL, timeout=120).read()
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        z.extractall(out)
        print("Extracted:", z.namelist())
    f = out / "diabetic_data.csv"
    if not f.exists():
        raise SystemExit("diabetic_data.csv not found after extraction; download manually (see data/README.md)")
    print("SHA-256 diabetic_data.csv:", hashlib.sha256(f.read_bytes()).hexdigest())

if __name__ == "__main__":
    main()
