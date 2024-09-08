"""This module contains the q3_time function."""

from collections import Counter
from typing import List, Tuple

import orjson

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q3-TIME")


@profile_function
@memory_profile_logging_wrapper
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 3 efficiently in time.

        In this function, I decided to read line by line in order
        to extract the mentionedUsers object from each JSON.

        Once the mentionedUser object is retrieve a simple operation with
        a Counter and its `update()` method is used.

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
    module_logger.info("Starting Q3-TIME...")
    module_logger.info("Reading and parsing JSON file.")
    users_counter = Counter()
    with open(file_path, 'r', encoding="utf-8") as json_file:
        try:
            for line in json_file.readlines():
                data = orjson.loads(line)  # pylint: disable=E1101
                mentioned_users = data.get("mentionedUsers")
                if mentioned_users is None:
                    continue
                usernames = [user['username'] for user in mentioned_users]
                users_counter.update(usernames)
        except orjson.JSONDecodeError:  # pylint: disable=E1101
            module_logger.error(
                "There was an error reading the JSON. Some fields may be missing."
            )
            module_logger.info("The request couldn't be fulfilled.")
            return []

    module_logger.info("Finding TOP 10 mentioned users")

    module_logger.info("Ending Q3-TIME...")

    return users_counter.most_common(10)
