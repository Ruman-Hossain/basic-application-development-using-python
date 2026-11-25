import csv


def save_csv(rows, filename):
    """Write a list of rows (first row = header) into a CSV file."""
    with open(filename, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def read_csv(filename):
    """Read a CSV file and return (header, data)."""
    with open(filename) as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]
