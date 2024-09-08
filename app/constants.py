"""This module contains constants for the app."""

from pathlib import Path

import emoji

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"

FILENAME = "farmers-protest-tweets-2021-2-4.json"

# Get all emojis in emoji library
ALL_EMOJIS = list(emoji.EMOJI_DATA.keys())
