"""This module contains enums for the app."""

from strenum import StrEnum


class LoggerModuleEnum(StrEnum):
    """Enum class for the name of the logger's modules."""

    MAIN_APP = 'MAIN'
    TIME_PROFILER = 'C_PROFILER'
    MEMORY_PROFILE = 'MEMORY_PROFILE'
    Q1_TIME = "Q1-TIME"
    Q2_TIME = "Q2-TIME"
    Q3_TIME = "Q3-TIME"
    Q1_MEMORY = "Q1-MEMORY"
    Q2_MEMORY = "Q2-MEMORY"
    Q3_MEMORY = "Q3-MEMORY"
