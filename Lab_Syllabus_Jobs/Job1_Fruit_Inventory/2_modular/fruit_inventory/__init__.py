"""fruit_inventory package: save fruit data in a CSV file and show a summary."""

from .storage import FILE, add_item, read_items
from .report import print_summary

__all__ = ["FILE", "add_item", "read_items", "print_summary"]
