import qrcode
from barcode import Code128
from barcode.writer import ImageWriter


def make_qr(data, filename):
    """Create a QR code image from the text and return the file name."""
    qrcode.make(data).save(filename)
    return filename


def make_barcode(code, name):
    """Create a Code 128 barcode PNG and return the saved file name."""
    return Code128(code, writer=ImageWriter()).save(name)
