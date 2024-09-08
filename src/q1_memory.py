"""This module contains the q1_memory function."""

import heapq
import json
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

from app.constants import DATE_FORMAT
from app.enums import LoggerModuleEnum
from app.logger import Logger
from app.utils import memory_profile_logging_wrapper, profile_function

module_logger = Logger.get_app_logger(LoggerModuleEnum.Q1_MEMORY)


@profile_function
@memory_profile_logging_wrapper
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Answer question 1 efficiently in memory.

        Objective: Find the 10 dates with the most tweets and
        the most active user for each date.

        This function iterates over a json file and gets the TOP 10
        dates on which users have tweeted the most.

        Once this is done, this function iterates over the same json looking
        for the most active user for each of these 10 dates.

        We can find the users for each date in a faster way
        and reading the json only once, but we are interested
        in memory efficiency. That is why we want to avoid having a
        dictionary with the users' activity until we know which
        dates we are interested in.

    Parameters
    ----------
    file_path : str
        Path of the json file to be loaded

    Returns
    -------
    List[Tuple[datetime.date, str]]
        List of the 10 most popular dates and their users.
        The date and user are returned as a tuple.
        The list is sorted in descending order
        (the most tweeted date will appear first).
    """
    module_logger.info("Starting Q1-MEMORY...")

    module_logger.info("Finding TOP 10 dates")
    # Initialize dict that will store the number of tweets per day.
    tweet_count_by_date = defaultdict(int)
    # Load json line by line so memory usage is optimized
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet = json.loads(line)
            # Extract date and parse it
            # Increment tweet counter by date
            tweet_count_by_date[
                datetime.strptime(tweet['date'].split('T')[0], DATE_FORMAT).date()
            ] += 1

    # Find TOP 10 dates
    # We use heapq instead of sorted:
    #   The heap method only stores the top n elements at any time,
    #   whereas the sorting method requires storage of all N elements.
    #   This means that for large datasets, the heap method's
    #   memory usage remains constant
    top_10_dates = heapq.nlargest(
        10,
        tweet_count_by_date.keys(),
        key=lambda date: tweet_count_by_date[date],  # noqa: F821
    )
    del tweet_count_by_date
    module_logger.info("TOP 10 dates found.")

    module_logger.info("Finding most active user for each date")
    # Initialize dict that will store the most active user.
    result = []
    user_tweet_count_by_date = defaultdict(lambda: defaultdict(int))
    # Load json line by line so memory usage is optimized
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet = json.loads(line)

            # If date is not in `top_10_dates` skip iteration
            # If the top_10_dates was larger (more than 10 dates)
            # we should think of another data type to store these dates.
            # to make this `not in` clause more memory efficient.
            # Given that we only have 10 dates, we are going to consider
            # this improvement as unnecessary for now.
            if (
                datetime.strptime(tweet['date'].split('T')[0], DATE_FORMAT).date()
                not in top_10_dates
            ):
                continue

            user_tweet_count_by_date[
                datetime.strptime(tweet['date'].split('T')[0], DATE_FORMAT).date()
            ][tweet["user"]['username']] += 1

        for top_date in top_10_dates:
            # Find TOP 10 dates
            # We use heapq instead of sorted:
            #   The heap method only stores the top n elements at any time,
            #   whereas the sorting method requires storage of all N elements.
            #   This means that for large datasets, the heap method's
            #   memory usage remains constant
            # pylint: disable=W0640
            top_user = heapq.nlargest(
                1,
                user_tweet_count_by_date[top_date].keys(),
                key=lambda username: user_tweet_count_by_date[top_date][  # noqa: F821
                    username
                ],
            )[0]
            # pylint: enable=W0640
            result.append((top_date, top_user))
        del user_tweet_count_by_date
    module_logger.info("Most active user for each date found")
    module_logger.info("Finishing Q1-MEMORY...")
    return result
