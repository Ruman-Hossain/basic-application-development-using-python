# জব ৩: QR Code & Barcode Generator and Decoding

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ২ | **নম্বর:** ৪

## উদ্দেশ্য

ছাত্রের ID ও নাম নিয়ে একটি QR code তৈরি করা হবে, এবং ID দিয়ে একটি barcode (Code 128)। তারপর দুটি ছবি থেকেই তথ্য আবার পড়ে (decode করে) দেখানো হবে।

সিলেবাসের ধাপ: 3.1 Setup → 3.2 Take ID ও নাম → 3.3 Create QR ও Barcode → 3.4 Decode → 3.5 Print decoded data

## QR code বনাম Barcode

| বিষয় | QR code | Barcode (Code 128) |
|---|---|---|
| ধরন | 2D (বর্গাকার ছোপ) | 1D (খাড়া রেখা) |
| তথ্য ধারণ | অনেক তথ্য (লেখা, লিংক) | কম, সাধারণত ID/নম্বর |
| পূর্ণরূপ | Quick Response | — |
| ব্যবহার | মোবাইলে স্ক্যান, পেমেন্ট, লিংক | পণ্য, লাইব্রেরি কার্ড, ID কার্ড |

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

### ফোল্ডারের গঠন

```
Job3_QR_Barcode/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p3_qr_barcode.py
├── 2_modular/
│   ├── main.py
│   └── codes/
│       ├── __init__.py
│       ├── generator.py
│       └── reader.py
└── 3_colab/
    └── Job3_colab.ipynb
```

## কোন package কেন

| Package | কাজ |
|---|---|
| `qrcode[pil]` | QR code ছবি তৈরি করে। `[pil]` মানে ছবি বানানোর জন্য Pillow সহ install হবে। |
| `python-barcode` | Code 128 সহ বিভিন্ন barcode তৈরি করে। import এর নাম `barcode`। |
| `Pillow` | ছবি খোলা ও সংরক্ষণ। import এর নাম `PIL`। |
| `pyzbar` | ছবি থেকে QR/barcode পড়ে (decode)। এটি ZBar নামের একটি C লাইব্রেরি ব্যবহার করে। |

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job3_QR_Barcode` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p3_qr_barcode.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `codes` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job3_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

### এই জবের বিশেষ নোট

**pyzbar এর জন্য সিস্টেমে ZBar লাগে:**
- **Windows:** ZBar এর DLL pyzbar এর সাথেই আসে। শুধু DLL error দিলে Microsoft **Visual C++ Redistributable Packages for Visual Studio 2013** install করুন।
- **Linux (Ubuntu):** `sudo apt install libzbar0`
- **Mac:** `brew install zbar`
- **Colab:** notebook এর প্রথম cell নিজেই `libzbar0` install করে।

কাজ শেষে Terminal এ `deactivate`।

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে)

### লাইন ১–৫: module আনা

```python
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image
```

- **`import qrcode`:** QR code তৈরির পুরো module আনা হলো।
- **`from barcode import Code128`:** অনেক ধরনের barcode এর মধ্যে শুধু **Code 128** class আনা হলো। এটি অক্ষর ও সংখ্যা দুটোই ধরে, তাই ছাত্রের ID এর জন্য উপযুক্ত।
- **`from barcode.writer import ImageWriter`:** barcode কে **PNG ছবি** হিসেবে লেখার জন্য। না দিলে python-barcode ডিফল্টে SVG ফাইল বানায়, যা pyzbar পড়তে পারে না।
- **`from pyzbar.pyzbar import decode`:** ছবি থেকে কোড পড়ার function।
- **`from PIL import Image`:** ছবির ফাইল খোলার জন্য (Pillow)।

### লাইন ৮–১০: ইনপুট নেওয়া ও জোড়া লাগানো

```python
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
data = student_id + " - " + name
```

- **কী হচ্ছে:** ID ও নাম নেওয়া হলো। `+` দিয়ে দুটি string জুড়ে একটি লেখা বানানো হলো, যেমন `"701234 - Rahim Uddin"`।
- **কেন জোড়া:** QR code এ অনেক তথ্য রাখা যায়, তাই ID ও নাম দুটোই একসাথে রাখা হলো। মাঝে `" - "` দেওয়ায় পড়ার সময় আলাদা করে বোঝা যায়।
- **কেন `int()` করা হয়নি:** ID দিয়ে হিসাব হবে না, আর কোড বানাতে string ই লাগে।

### লাইন ১৩–১৫: QR code তৈরি ও সংরক্ষণ

```python
qr_img = qrcode.make(data)
qr_img.save("student_qr.png")
print("QR code saved: student_qr.png")
```

- **`qrcode.make(data)`:** লেখাটিকে QR code এ রূপান্তর করে একটি ছবি object দেয়। size ও error correction নিজে থেকে ঠিক করে নেয়।
- **কেন `make()`:** এটি সবচেয়ে সহজ উপায়, এক লাইনে QR বানায়। রং বা সাইজ বদলাতে চাইলে `qrcode.QRCode()` class ব্যবহার করা যায় (বাড়তি কাজ দেখুন)।
- **`.save("student_qr.png")`:** ছবিটি PNG ফাইলে লেখে। এটি না দিলে ছবি শুধু মেমোরিতে থাকত।

### লাইন ১৮–১৯: barcode তৈরি ও সংরক্ষণ

```python
barcode_file = Code128(student_id, writer=ImageWriter()).save("student_barcode")
print("Barcode saved:", barcode_file)
```

- **কী হচ্ছে:** এক লাইনে তিনটি কাজ হয়।
  1. `ImageWriter()` একটি PNG লেখক object তৈরি করে।
  2. `Code128(student_id, writer=...)` ID থেকে barcode object তৈরি করে।
  3. `.save("student_barcode")` ফাইল সংরক্ষণ করে।
- **কেন barcode এ শুধু ID:** barcode এ বেশি লেখা দিলে রেখা অনেক লম্বা হয়ে পড়তে অসুবিধা হয়। ID ই যথেষ্ট, কারণ ID দিয়ে ডাটাবেস থেকে বাকি তথ্য পাওয়া যায়।
- **কেন নামে `.png` লেখা হয়নি:** `save()` নিজেই শেষে `.png` যোগ করে, এবং পুরো ফাইলের নাম (`student_barcode.png`) **ফেরত দেয়**। সেই নাম `barcode_file` এ রাখা হলো, যা পরে decode এ লাগবে।

### লাইন ২২–২৫: দুটি ছবি থেকে decode

```python
for file in ["student_qr.png", barcode_file]:
    results = decode(Image.open(file))
    for r in results:
        print("Decoded from", file, "->", r.type, ":", r.data.decode("utf-8"))
```

- **বাইরের `for`:** দুটি ফাইলের নাম একটি list এ রেখে লুপ চালানো হলো, যাতে একই কোড দুবার লিখতে না হয়।
- **`Image.open(file)`:** Pillow দিয়ে ছবির ফাইল খোলে।
- **`decode(...)`:** ছবিতে যত QR/barcode আছে সব খুঁজে একটি **list** দেয়। একটি ছবিতে একাধিক কোড থাকতে পারে, তাই list।
- **ভিতরের `for r in results`:** পাওয়া প্রতিটি কোডের জন্য।
  - `r.type` কোডের ধরন (`QRCODE` বা `CODE128`)।
  - `r.data` ভিতরের তথ্য, কিন্তু **bytes** আকারে (`b'701234'`)।
- **কেন `.decode("utf-8")`:** bytes কে সাধারণ লেখা (string) এ রূপান্তর করে, যাতে `b'...'` ছাড়া পরিষ্কার দেখায়। (এখানে `decode` শব্দটি দুই জায়গায় আছে। pyzbar এর `decode()` ছবি পড়ে, আর bytes এর `.decode()` লেখায় রূপান্তর করে। দুটি আলাদা জিনিস।)
- **কেন নিজের বানানো ছবিই decode করছি:** এতে প্রমাণ হয় যে তৈরি করা কোড ঠিক আছে, যন্ত্রে স্ক্যান করলে একই তথ্য পাওয়া যাবে।

---

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** **generator.py** কোড ও ছবি তৈরি করে, **reader.py** ছবি থেকে কোড পড়ে। main.py জানেই না কোন লাইব্রেরি দিয়ে QR বানানো হচ্ছে। পরে লাইব্রেরি বদলালে শুধু generator.py বদলাতে হবে।

**নতুন শব্দগুলো:**

| শব্দ | মানে |
|---|---|
| module | একটি `.py` ফাইল। যেমন `storage.py`। |
| package | কয়েকটি module সহ একটি ফোল্ডার, যার ভিতরে `__init__.py` আছে। |
| import | অন্য module/package থেকে function বা ভেরিয়েবল আনা: `from package import function`। |
| export | package এর `__init__.py` তে import করে রাখা, যাতে বাইরে থেকে সহজে নেওয়া যায়। `__all__` তালিকায় নামগুলো লেখা থাকে। |
| relative import | `from .storage import ...`: ডট (.) মানে একই package এর ভিতরের ফাইল। |
| `if __name__ == "__main__":` | ফাইলটি সরাসরি চালালে (`python main.py`) নিচের কোড চলে। import করলে চলে না। |
| return | function এর ফলাফল ডাকার জায়গায় ফেরত পাঠানো। একাধিক মান ফেরত দিলে tuple হয়। |

### `codes/__init__.py` — package এর দরজা

```python
"""codes package: create QR codes and barcodes, and read them back."""

from .generator import make_qr, make_barcode
from .reader import read_codes

__all__ = ["make_qr", "make_barcode", "read_codes"]
```

- `make_qr`, `make_barcode`, `read_codes` তিনটি function export করে।

### `codes/generator.py` — QR ও barcode তৈরি

```python
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
```

- `make_qr(data, filename)`: `qrcode.make(data).save(filename)` এক লাইনে ছবি বানিয়ে সংরক্ষণ করে (**method chaining**), তারপর ফাইলের নাম ফেরত দেয়।
- `make_barcode(code, name)`: `save()` যে পূর্ণ নাম (.png সহ) ফেরত দেয়, সেটিই আবার return করে।

### `codes/reader.py` — ছবি থেকে পড়া

```python
from pyzbar.pyzbar import decode
from PIL import Image


def read_codes(filename):
    """Return a list of (type, text) for every code found in the image."""
    results = decode(Image.open(filename))
    return [(r.type, r.data.decode("utf-8")) for r in results]
```

- `read_codes(filename)` pyzbar এর জটিল ফলাফলকে সহজ list বানায়: প্রতিটি উপাদান `(type, text)`।
- `[(r.type, r.data.decode("utf-8")) for r in results]` হলো **list comprehension**: লুপ চালিয়ে এক লাইনে নতুন list তৈরি।

### `main.py` — ইনপুট ও চালানো

```python
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
```

- `from codes import make_qr, make_barcode, read_codes`: package থেকে import।
- `for code_type, text in read_codes(file):` প্রতিটি tuple কে সরাসরি দুটি ভেরিয়েবলে ভাগ করে নেয়।

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job3_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: package install |  |
| Cell 2: module import | QR, barcode, decode ও ছবির module আনা। |
| Cell 3: ধাপ ১: ID ও নাম ইনপুট | ID ও নাম চাইবে। |
| Cell 4: ধাপ ২: QR code তৈরি | student_qr.png তৈরি হবে। |
| Cell 5: ধাপ ৩: Barcode তৈরি | student_barcode.png তৈরি হবে। |
| Cell 6: ধাপ ৪: দুটি ছবি decode | ছবি থেকে পড়া তথ্য দেখাবে। |
| Cell 7: তৈরি হওয়া ছবি দেখা |  |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট (পরীক্ষিত)

```
Enter Student ID: 701234
Enter Student Name: Rahim Uddin
QR code saved: student_qr.png
Barcode saved: student_barcode.png
Decoded from student_qr.png -> QRCODE : 701234 - Rahim Uddin
Decoded from student_barcode.png -> CODE128 : 701234
```

তৈরি হওয়া ফাইল:
- `student_qr.png`: কালো-সাদা বর্গাকার QR code। মোবাইলের ক্যামেরা বা Google Lens দিয়ে স্ক্যান করলে `701234 - Rahim Uddin` দেখাবে।
- `student_barcode.png`: খাড়া রেখার barcode, নিচে `701234` লেখা।

## অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] **১.** `1_single_file` এর প্রোগ্রাম চালিয়ে নমুনা আউটপুটের সাথে মিলিয়ে দেখুন।
- [ ] **২.** `2_modular` এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই আসছে কিনা দেখুন।
- [ ] **৩.** module সংস্করণে প্রতিটি ফাইল খুলে বলুন কোন function কোন ফাইলে আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] **৪.** Colab এ notebook আপলোড করে একটি একটি cell চালান। প্রতিটি cell এর পরে কী পরিবর্তন হলো খেয়াল করুন।
- [ ] **৫.** "বাড়তি কাজ" থেকে একটি কাজ বেছে নিন। module সংস্করণে নতুন function টি সঠিক module এ যোগ করুন এবং `__init__.py` থেকে export করুন।

## সমস্যা ও সমাধান

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ImportError: Unable to find zbar shared library` | ZBar সিস্টেমে নেই। Linux এ `sudo apt install libzbar0`, Mac এ `brew install zbar`, Colab এ `!apt-get update -qq` তারপর `!apt-get install -y libzbar0`। |
| Windows এ `FileNotFoundError` / DLL error (pyzbar) | Visual C++ Redistributable 2013 install করুন। |
| `ModuleNotFoundError: No module named 'barcode'` | `python-barcode` install হয়নি (নাম `barcode` নয়)। `pip install -r requirements.txt` দিন। |
| decode এ কিছুই ছাপে না | ছবি অস্পষ্ট বা খুব ছোট। barcode এ শুধু ছোট ID দিন। |

## বাড়তি কাজ (অনুশীলন)

1. `qrcode.QRCode(box_size=10, border=4)` ও `make_image(fill_color="darkblue", back_color="white")` দিয়ে রঙিন QR বানান।
2. একাধিক ছাত্রের ID একটি লুপে নিয়ে প্রত্যেকের জন্য আলাদা নামে QR বানান।
3. মোবাইলে তোলা একটি barcode এর ছবি decode করে দেখুন।

## ভাইভা প্রশ্ন ও উত্তর

1. **QR এর পূর্ণরূপ কী?** Quick Response।
2. **QR code ও barcode এর মূল পার্থক্য কী?** QR code 2D এবং বেশি তথ্য ধরে। barcode 1D, সাধারণত শুধু নম্বর/ID রাখে।
3. **`ImageWriter` কেন দেওয়া হয়েছে?** barcode কে PNG ছবি হিসেবে সংরক্ষণের জন্য। না দিলে SVG হতো, যা pyzbar পড়তে পারে না।
4. **pyzbar এর `decode()` কী ফেরত দেয়?** ছবিতে পাওয়া সব কোডের একটি list, প্রতিটির `type` ও `data` সহ।
5. **`r.data.decode("utf-8")` কেন লাগে?** `r.data` bytes আকারে থাকে। `.decode()` তাকে সাধারণ string বানায়।
6. **Code 128 কেন বেছে নেওয়া হয়েছে?** এটি অক্ষর ও সংখ্যা দুটোই ধরে এবং বহুল ব্যবহৃত।
7. **`qrcode[pil]` এ `[pil]` মানে কী?** QR এর সাথে ছবি বানানোর জন্য Pillow package ও install হবে।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।
