"""This module contains the main function of the project."""

from logger import Logger

module_logger = Logger.get_app_logger("MAIN")


def main() -> None:
    """Run main script of the app."""
    module_logger.info("Starting main.")

    module_logger.error("Ending main.")


if __name__ == "__main__":
    Logger()
    main()
