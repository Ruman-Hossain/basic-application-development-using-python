from codes import make_qr, make_barcode, read_codes

if __name__ == "__main__":
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    data = student_id + " - " + name

    qr_file = make_qr(data, "student_qr.png")
    print("QR code saved:", qr_file)

    barcode_file = make_barcode(student_id, "student_barcode")
    print("Barcode saved:", barcode_file)

    for file in [qr_file, barcode_file]:
        for code_type, text in read_codes(file):
            print("Decoded from", file, "->", code_type, ":", text)
