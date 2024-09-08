"""This module contains the q1_time function."""

from datetime import datetime
from typing import List, Tuple

import polars as pl

from app.extract import read_json_file
from app.logger import Logger
from app.utils import profile_function

module_logger = Logger.get_app_logger("Q1-TIME")


@profile_function
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Answer question 1 efficiently in time.

        In this case I've used the `polars` library instead of
        pandas because of the results that can be seen in the
        `notebooks/Q1 processing time.ipynb` nootebook.

        There is a small advantage for polars so I decided to keep
        polars.

        Note: Given the size of the JSON file, there is no need for
        parallel processing so PySpark and Dask were discarded. These
        two options could had beeen an excellent solution
        if the size of the size happened to be bigger.

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
    module_logger.info("Starting Q1-TIME...")

    module_logger.info("Reading JSON file.")
    data = read_json_file(file_path)
    module_logger.info("JSON file is read.")

    module_logger.info("Loading DataFrame")
    # Create a Polars DataFrame from the processed data
    tweets_df: pl.DataFrame = pl.DataFrame(
        data, schema=["date", "username"], orient="row"
    )

    module_logger.info("Parsing date column")
    # Convert the 'date' column to datetime format
    tweets_df = tweets_df.with_columns(
        [
            pl.col("date").str.strptime(
                pl.Datetime, format="%Y-%m-%dT%H:%M:%S%z", strict=False
            )
        ]
    )

    module_logger.info("Finding top users by date")
    # Group by date and username, counting the number of tweets per user each day
    tweets_per_day = tweets_df.group_by([pl.col("date").dt.date(), "username"]).agg(
        pl.count().alias("tweet_count")
    )

    # Find the user with the most tweets per day
    top_user_per_day = (
        tweets_per_day.sort("tweet_count", descending=True)
        .group_by("date")
        .agg(pl.first("username").alias("top_user"))
    )

    module_logger.info("Finding most tweeted dates")
    # Count the total number of tweets per day
    tweets_by_day = tweets_df.group_by(tweets_df["date"].dt.date()).agg(
        pl.count().alias("total_tweets")
    )

    module_logger.info("Joining top users with top dates")
    # Join the total tweets with the top user by day
    top_10_dates = tweets_by_day.join(top_user_per_day, on="date")

    module_logger.info("Parsing output")
    # Sort by total number of tweets per day and select the top 10 dates
    top_10_dates = top_10_dates.sort("total_tweets", descending=True).head(10)

    return [
        (row["date"], row["top_user"]) for row in top_10_dates.iter_rows(named=True)
    ]
