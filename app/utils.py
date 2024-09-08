"""This module contains auxiliary functions for the app."""

import cProfile
import io
import pstats

from logger import Logger
from memory_profiler import memory_usage, profile


def profile_function(func):
    """Run cProfile over the function."""
    profiler_logger = Logger.get_app_logger("cProfile")

    def wrapper(*args, **kwargs):
        """Wrap the function to run cProfile over it."""
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()

        # Crear un buffer de texto
        text_buffer = io.StringIO()
        # Generar estadísticas de cProfile y redirigir la salida al buffer
        profiler_stats = pstats.Stats(profiler, stream=text_buffer).sort_stats(
            'cumulative'
        )
        profiler_stats.print_stats()

        # Enviar los resultados del buffer al logger
        profiler_logger.info("cProfile results:\n%s", text_buffer.getvalue())

        return result

    return wrapper


def memory_profile_logging_wrapper(func):
    """Run Memory Profile over the function."""
    profiler_logger = Logger.get_app_logger("MemoryProfile")

    def wrapper(*args, **kwargs):
        """Wrap the function to run Memory Profile over it."""
        # Capturing output using StringIO
        stream = io.StringIO()
        mem_before = memory_usage()[0]
        profiler_logger.info(f"Memory before execution: {mem_before} MiB")

        # Overriding the stream in memory_profiler
        profiled_func = profile(stream=stream)(func)

        # Execute the function with memory profiling
        result = profiled_func(*args, **kwargs)

        mem_after = memory_usage()[0]
        profiler_logger.info(f"Memory after execution: {mem_after} MiB")
        profiler_logger.info(f"Memory consumption: {mem_after - mem_before} MiB")

        # Log the memory profiler results
        profiler_logger.info("Memory profiler results:\n%s", stream.getvalue())

        return result

    return wrapper
