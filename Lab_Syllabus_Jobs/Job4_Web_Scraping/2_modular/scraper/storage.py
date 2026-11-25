import csv

HEADER = ["Book Name", "Price", "Rating", "Availability"]


def save_csv(rows, filename):
    """Save the book rows (with a header) into a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(rows)
