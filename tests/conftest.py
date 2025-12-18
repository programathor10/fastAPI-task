import sys
from pathlib import Path

# Agrega la carpeta raíz del proyecto al PYTHONPATH
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
