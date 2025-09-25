#!/usr/bin/python3
"""CountedIterator class to track number of iterations."""


class CountedIterator:
    """Iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)  # peut lever StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return how many items have been fetched so far."""
        return self.count

    def __iter__(self):
        """An iterator must return itself when iter() is called."""
        return self
