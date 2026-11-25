"""codes package: create QR codes and barcodes, and read them back."""

from .generator import make_qr, make_barcode
from .reader import read_codes

__all__ = ["make_qr", "make_barcode", "read_codes"]
