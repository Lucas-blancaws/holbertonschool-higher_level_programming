#!/usr/bin/python3

"""Module: Convert JSON string to Python object."""


def from_json_string(my_str):
    """Return Python object from JSON string."""
    import json
    return json.loads(my_str)
