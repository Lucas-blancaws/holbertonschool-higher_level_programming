#!/usr/bin/python3

"""Module: Return dict description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dict representation of an object."""
    return obj.__dict__
