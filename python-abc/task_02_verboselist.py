#!/usr/bin/python3
"""VerboseList class extending list with notifications."""


class VerboseList(list):
    """Custom list that prints notifications when modified."""

    def append(self, item):
        """Add item and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend list and print a message with the number of new items."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Remove item and print a message."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index and print a message."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
