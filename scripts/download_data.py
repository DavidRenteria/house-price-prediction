from pathlib import Path
import urllib.request
import os

URL  = "https://raw.githubusercontent.com/wblakecannon/ames/master/data/housing.csv"
DEST = Path(__file__).resolve().parents[1] / "data" / "raw" / "ames.csv" 

def main() -> None: 
    DEST.parent.mkdir(parents=True, exist_ok=True)

    if DEST.exists(): 
        print(f"The file already exists: {DEST}") 
    
    print(f"Downloading file {URL}")
    urllib.request.urlretrieve(URL, DEST)
    print(f"Saved in {DEST}")
    return 

if __name__ == "__main__": 
    main()
