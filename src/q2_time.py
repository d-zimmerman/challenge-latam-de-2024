"""This module contains the q2_time function."""

from typing import List, Tuple

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q2-TIME")


@profile_function
@memory_profile_logging_wrapper
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 2 efficiently in time.

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
    module_logger.info("Finishing Q2-TIME...")
