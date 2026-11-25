"""scraper package: download a web page, find the books and save them to CSV."""

from .fetch import get_html
from .parser import parse_books
from .storage import save_csv

__all__ = ["get_html", "parse_books", "save_csv"]
