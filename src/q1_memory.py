"""This module contains the q1_memory function."""

import gc
import heapq
import json
from datetime import datetime
from typing import List, Tuple

from app.logger import Logger
from app.utils import memory_profile_logging_wrapper

module_logger = Logger.get_app_logger("Q1-MEMORY")


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
    # Initialize dict that will store the number of tweets per day.
    module_logger.info("Finding TOP 10 dates")
    tweet_count_by_date = {}
    # Load json line by line so memory usage is optimized
    # By this we load in memory only the line that will be processed.
    # Previous line is discarded after processing. Next line waits in the buffer.
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet = json.loads(line)

            # Extract date from JSON
            date = tweet["date"].split("T")[0]

            # `defaultdict` could be used to avoid this check
            # but we prioritize memory as much as possible.
            if date not in tweet_count_by_date:
                tweet_count_by_date[date] = 0
            tweet_count_by_date[date] += 1

    # Find TOP 10 dates
    # We use heapq instead of sorted. In this way we iterate over
    # the dates and only keep the top 10. Sorted will try to sort the list
    # loading it completely in memory.
    top_10_dates = heapq.nlargest(
        10,
        tweet_count_by_date.keys(),
        key=lambda date: tweet_count_by_date[date],  # noqa: F821
    )
    del tweet_count_by_date
    gc.collect()  # Force garbage collection
    module_logger.info("TOP 10 dates found.")

    # Initialize dict that will store the most active user.
    user_tweet_count_by_date = {}

    module_logger.info("Finding most active user for each date")
    # Load json line by line so memory usage is optimized
    # By this we load in memory only the line that will be processed.
    # Previous line is discarded after processing. Next line waits in the buffer.
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet = json.loads(line)

            # Extract date from JSON
            date = tweet['date'].split('T')[0]

            # If date is not included in the TOP 10, skip loop
            if date not in top_10_dates:
                continue

            username = tweet["user"]['username']

            # `defaultdict` could be used to avoid this check
            # but we prioritize memory as much as possible.
            if date not in user_tweet_count_by_date:
                user_tweet_count_by_date[date] = {}
            if username not in user_tweet_count_by_date[date]:
                user_tweet_count_by_date[date][username] = 0
            # Increment counter
            user_tweet_count_by_date[date][username] += 1

    result = []
    for date in top_10_dates:
        # pylint: disable=W0640
        # heapq is triggering pylint without reason
        top_user = heapq.nlargest(
            1,
            user_tweet_count_by_date[date].keys(),
            key=lambda username: user_tweet_count_by_date[date][username],
        )
        # pylint: enable=W0640
        del user_tweet_count_by_date[date]
        gc.collect()  # Force garbage collection
        result.append((date, top_user))
    module_logger.info("Most active user for each date found")
    module_logger.info("Finishing Q1-MEMORY...")
    return result
