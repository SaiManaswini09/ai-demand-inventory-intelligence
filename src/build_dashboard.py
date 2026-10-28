"""The prebuilt GitHub Pages dashboard is stored at repository-root index.html."""
from pathlib import Path
print(Path(__file__).resolve().parent.parent / "index.html")
