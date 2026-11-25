import csv
import os


def save_row(row, filename, header):
    """Add one row to the CSV file (write the header first if the file is new)."""
    new_file = not os.path.exists(filename)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(header)
        writer.writerow(row)


def read_csv(filename):
    """Return (header, data) from the CSV file, or (None, []) if there is no file yet."""
    if not os.path.exists(filename):
        return None, []
    with open(filename) as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]
