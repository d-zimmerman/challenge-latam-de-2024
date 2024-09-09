"""This module contains configuration variables and classes for the project."""

import os


class LoggerConfig:  # pylint: disable=R0903
    """Logger configuration class.

    Contains configuration variables for the logger of the App.
    """

    LOGGER_NAME = os.environ.get("LOGGER_NAME")
    LOGS_DIR = os.environ.get("LOGS_DIR")
    LOGS_FILE = os.environ.get("LOGS_FILE")
