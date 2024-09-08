"""This module contains the q3_memory function."""

import heapq
import json
from collections import defaultdict
from typing import List, Tuple

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q2-MEMORY")


@profile_function
@memory_profile_logging_wrapper
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 3 efficiently in memory.

        In this function we had two possible paths:
            1. Use a RegEx to find the mentions (@) in the context/text
              of the tweet.
            2. Use the `mentionedUsers` key in the JSON and leaving to
              the API of Tweeter the identification of those mentions

        I decided to go with the second approach.

        This approach also include reading the JSON file line by line
        and counting how many times the same user is mentioned.
        At the end the TOP 10 users is found.

    Parameters
    ----------
    file_path : str
        Path of the json file to be loaded

    Returns
    -------
    List[Tuple[datetime.date, str]]
        List of the 10 most mentioned users and
        the number of times they had been mentioned.
    """
    module_logger.info("Starting Q3-MEMORY...")
    users_counter = defaultdict(int)
    module_logger.info("Counting mentioned users")
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            mentioned_users = json.loads(line).get("mentionedUsers")

            if mentioned_users is None:
                continue

            for user in mentioned_users:
                if user.get("username") is not None:
                    users_counter[user.get("username")] += 1

    module_logger.info("Finding TOP 10 mentioned users")
    top_10_users = heapq.nlargest(10, users_counter.items(), key=lambda x: x[1])

    module_logger.info("Ending Q3-MEMORY...")

    return top_10_users
