"""This module contains the q2_memory function."""

from typing import List, Tuple

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger("Q2-MEMORY")


@profile_function
@memory_profile_logging_wrapper
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Answer question 2 efficiently in memory.

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
    module_logger.info("Finishing Q2-MEMORY...")
