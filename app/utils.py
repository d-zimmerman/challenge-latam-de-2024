"""This module contains auxiliary functions for the app."""

import cProfile
import io
import pstats

from logger import Logger


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
