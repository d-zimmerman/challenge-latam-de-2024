"""This module contains the main function of the project."""

from logger import Logger

from app.constants import DATA_DIR, FILENAME
from src.q1_memory import q1_memory

module_logger = Logger.get_app_logger("MAIN")


def main() -> None:
    """Run main script of the app."""
    module_logger.info("Starting main.")

    result = q1_memory(DATA_DIR / FILENAME)
    module_logger.info(f"Q1-MEMORY result:\n{result}")

    module_logger.info("Ending main.")


if __name__ == "__main__":
    Logger()
    main()
