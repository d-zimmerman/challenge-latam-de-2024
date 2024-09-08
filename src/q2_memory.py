"""This module contains the q2_memory function."""

import heapq
import json
from collections import defaultdict
from typing import List, Tuple

from app.constants import EMOJI_PATTERN
from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q2-MEMORY")


@profile_function
@memory_profile_logging_wrapper
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 2 efficiently in memory.

        The approach used in the function is to load the JSON
        file line by line.
        If the `content' key exists, then we look for emojis in the content.
        Once emojis are found for that line, the dictionary with the counts is
        updated.
        After every line has been reviewed, we look for the TOP 10.

    Parameters
    ----------
    file_path : str
        Path of the json file to be loaded

    Returns
    -------
    List[Tuple[datetime.date, str]]
        List of the 10 most used emojis and
        the number of times they had been used.
    """
    module_logger.info("Starting Q2-MEMORY...")

    module_logger.info("Counting emojis")
    emoji_counter = defaultdict(int)
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)
            if 'content' not in data:
                continue
            # Extract all emojis from tweet and update dict with count
            for match in EMOJI_PATTERN.findall(data["content"]):
                if match:  # Only count non-None matches
                    emoji_counter[match] += 1
    module_logger.info("Emojis counted.")

    module_logger.info("Finding TOP 10 emojis")
    # Top 10 emojis
    top_10_emojis = heapq.nlargest(10, emoji_counter.items(), key=lambda x: x[1])
    module_logger.info("TOP 10 emojis found.")
    module_logger.info("Finishing Q2-MEMORY...")
    return top_10_emojis
