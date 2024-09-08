"""This module contains the main function of the project."""

from logger import Logger

from app.constants import DATA_DIR, FILENAME
from src.q1_memory import q1_memory
from src.q1_time import q1_time

module_logger = Logger.get_app_logger("MAIN")


def main() -> None:
    """Run main script of the app."""
    module_logger.info("Starting main.")

    file_path = DATA_DIR / FILENAME

    result = q1_memory(file_path)
    module_logger.info(f"Q1-MEMORY result:\n{result}")

    result = q1_time(file_path)
    module_logger.info(f"Q1-TIME result:\n{result}")

    module_logger.info("Ending main.")


if __name__ == "__main__":
    Logger()
    main()
