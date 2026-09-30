import json
from pathlib import Path


# Find the CareerBridge project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Location of careers.json
DATA_FILE = BASE_DIR / "data" / "careers.json"


def load_careers():
    """Load career information from careers.json."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_career(career_name):
    """Get information about one specific career."""
    careers = load_careers()
    return careers.get(career_name)


def get_all_careers():
    """Get all available career names."""
    careers = load_careers()
    return list(careers.keys())