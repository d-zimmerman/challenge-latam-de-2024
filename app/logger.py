"""This module contains the definition and config of the logger of the app."""

import logging
import sys

from app.cfg import LoggerConfig


class Logger:
    """Logger Class."""

    def __init__(
        self,
        logger_name: str = LoggerConfig.LOGGER_NAME,
        log_file: str = LoggerConfig.LOGS_FILE,
        log_dir: str = LoggerConfig.LOGS_DIR,
    ):
        """Init method for Logger class.

        Parameters
        ----------
        logger_name : str
            Name to be given to the logger.
        log_file : str
            Filename where logs will be stored.
            Default: "app_logs"
        log_dir : str
            Directory name where log file will be stored.
            Default: Current directory.

        Returns
        -------
        logger: Logger object
            App logger
        """
        self.logger_name = logger_name
        self.log_file = log_file
        self.log_dir = log_dir
        self.setup_logger()

    def setup_logger(self):
        """Run App Logger setup.

        Parameters
        ----------
        logger_name : str
            Name to be given to the logger.
        log_file : str
            Filename where logs will be stored.
        log_dir : str
            Directory name where log file will be stored.

        Returns
        -------
        logger: Logger object
            App's logger object
        """
        logger = logging.getLogger(self.logger_name)
        logger.handlers.clear()
        logger.setLevel(logging.DEBUG)

        log_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - \n<<\n %(message)s \n>>\n"
        )

        # File Handler
        file_handler = logging.FileHandler(f"{self.log_dir}/{self.log_file}.log")
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(logging.INFO)

        # Stream Handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(log_formatter)
        stream_handler.setLevel(logging.ERROR)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

    @staticmethod
    def get_app_logger(module_name, logger_name: str = LoggerConfig.LOGGER_NAME):
        """Get App's logger.

        Parameters
        ----------
        module_name: str
            Module name.
        logger_name : str
            Name of the logger you want to invoke.

        Returns
        -------
        Logger
            Logger Object
        """
        return logging.getLogger(logger_name).getChild(module_name)
