import os
import json
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

PATH = Path(os.getenv('PATH_TO_DATA', ''))

with open(PATH, 'r') as file:
    DATA = json.load(file)

