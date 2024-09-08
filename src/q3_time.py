"""This module contains the q3_time function."""

from typing import List, Tuple

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q3-TIME")


@profile_function
@memory_profile_logging_wrapper
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 3 efficiently in time.

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

    module_logger.info("Ending Q3-TIME...")
