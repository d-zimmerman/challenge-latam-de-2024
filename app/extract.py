"""This module contains extraction functions for the project."""

from typing import List, Tuple

import orjson


def read_json_file(file_path) -> List[Tuple[str, str]]:
    """Read a json file line by line using orjson.

        If line has any error, it's discarded.

    Parameters
    ----------
    file_path : str
        Path where the file is stored.

    Returns
    -------
    List[Tuple[str, str]]
        List with each parsed line.
    """
    data = []
    with open(file_path, 'r', encoding="utf-8") as json_file:
        for line in json_file:
            try:
                item = orjson.loads(line)  # pylint: disable=E1101
                if 'date' in item and 'user' in item and 'username' in item['user']:
                    data.append((item['date'], item['user']['username']))
            except orjson.JSONDecodeError:  # pylint: disable=E1101
                continue
    return data
