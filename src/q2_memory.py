"""This module contains the q2_memory function."""

import heapq
import json
from collections import defaultdict
from typing import List, Tuple

import emoji

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q2-MEMORY")


@profile_function
@memory_profile_logging_wrapper
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 2 efficiently in memory.

        I use the `emoji` library to make things simpler.
        By doing so we leave it up to the library to keep
        the list of existing emojis up to date (
        thus reducing complexity and maintenance on our side).
        The downside of this is that we have no control over
        the implementation of this library and the processing
        may not be thinking about memory efficiency.

        Despite this, I consider that for this particular application,
        after some tests, this library fits very well for
        the usage scenario. The simplified emoji search
        implies that this library is an excellent solution.

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
            for value in emoji.analyze(data['content']):
                emoji_counter[value.chars] += 1
    module_logger.info("Emojis counted.")

    module_logger.info("Finding TOP 10 emojis")
    # Top 10 emojis
    top_10_emojis = heapq.nlargest(10, emoji_counter.items(), key=lambda x: x[1])
    module_logger.info("TOP 10 emojis found.")
    module_logger.info("Finishing Q2-MEMORY...")
    return top_10_emojis
