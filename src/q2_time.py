"""This module contains the q2_time function."""

from collections import Counter
from typing import List, Tuple

import orjson

from app.constants import EMOJI_PATTERN
from app.enums import LoggerModuleEnum
from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger(LoggerModuleEnum.Q2_TIME)


@profile_function
@memory_profile_logging_wrapper
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 2 efficiently in time.

        Since memory usage is not a limitation in this case,
        what we will do is load all the tweets into a single string
        and then process it with a Regular Expression (RegEx) that will contain
        all the emojis existing in the `emoji` library.

        After obtaining the list of total emojis, we will use a Counter
        to return the top 10 of these and their corresponding
        number of appearances.

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
    module_logger.info("Starting Q2-TIME...")
    module_logger.info("Reading and parsing JSON file.")
    full_text = ""
    with open(file_path, 'r', encoding="utf-8") as json_file:
        tweet_list = json_file.readlines()

        try:
            full_text = " ".join(
                [
                    orjson.loads(tweet)['content']  # pylint: disable=E1101
                    for tweet in tweet_list
                ]
            )
        except orjson.JSONDecodeError:  # pylint: disable=E1101
            module_logger.error(
                "There was an error reading the JSON. Some fields may be missing."
            )
            module_logger.info("The request couldn't be fulfilled.")
            return []
    module_logger.info("JSON file was read and parsed.")

    module_logger.info("Finding top 10 emojis")
    top_10_emojis = Counter(EMOJI_PATTERN.findall(full_text)).most_common(10)

    module_logger.info("Finishing Q2-TIME...")
    return top_10_emojis
