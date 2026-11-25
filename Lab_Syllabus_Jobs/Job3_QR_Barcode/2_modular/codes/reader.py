from pyzbar.pyzbar import decode
from PIL import Image


def read_codes(filename):
    """Return a list of (type, text) for every code found in the image."""
    results = decode(Image.open(filename))
    return [(r.type, r.data.decode("utf-8")) for r in results]
