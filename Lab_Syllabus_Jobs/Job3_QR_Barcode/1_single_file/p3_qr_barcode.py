import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image

# Step 1: take student id and name
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
data = student_id + " - " + name

# Step 2: create QR code
qr_img = qrcode.make(data)
qr_img.save("student_qr.png")
print("QR code saved: student_qr.png")

# Step 3: create barcode (Code 128)
barcode_file = Code128(student_id, writer=ImageWriter()).save("student_barcode")
print("Barcode saved:", barcode_file)

# Step 4: decode both images
for file in ["student_qr.png", barcode_file]:
    results = decode(Image.open(file))
    for r in results:
        print("Decoded from", file, "->", r.type, ":", r.data.decode("utf-8"))
