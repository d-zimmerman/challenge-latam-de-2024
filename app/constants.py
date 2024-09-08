"""This module contains constants for the app."""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"

FILENAME = "farmers-protest-tweets-2021-2-4.json"

EMOJI_PATTERN = re.compile(
    r'['
    r'\U0001F600-\U0001F64F'
    r'\U0001F300-\U0001F5FF'
    r'\U0001F680-\U0001F6FF'
    r'\U0001F700-\U0001F77F'
    r'\U0001F780-\U0001F7FF'
    r'\U0001F800-\U0001F8FF'
    r'\U0001F900-\U0001F9FF'
    r'\U0001FA00-\U0001FA6F'
    r'\U0001FA70-\U0001FAFF'
    r'\U00002700-\U000027BF'
    r'\U0001F1E6-\U0001F1FF'
    r']+'
)

DATETIME_FORMAT = r"%Y-%m-%dT%H:%M:%S%z"
DATE_FORMAT = r'%Y-%m-%d'
