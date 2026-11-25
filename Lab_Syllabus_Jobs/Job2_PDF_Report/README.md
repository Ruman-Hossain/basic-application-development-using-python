# জব ২: Generate PDF Report from CSV File

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ৩ | **নম্বর:** ৪

## উদ্দেশ্য

একটি ছোট **মেনু-ভিত্তিক application**: মেনু থেকে ছাত্রদের তথ্য (Student_Id, Name, Roll, Semester, Shift, Department, Date of Birth, Phone) ইনপুট দিয়ে CSV তে রাখা, আর CSV পড়ে টেবিলসহ PDF রিপোর্ট তৈরি করা।

```
1. Add student   2. Make PDF report   3. Exit
```

সিলেবাসের ধাপ: 2.1 Setup → 2.2 Store student info into CSV (মেনু 1) → 2.3 Generate PDF report (মেনু 2)

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

### ফোল্ডারের গঠন

```
Job2_PDF_Report/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p2_pdf_report.py
├── 2_modular/
│   ├── main.py
│   └── report_tools/
│       ├── __init__.py
│       ├── csv_tools.py
│       └── pdf_tools.py
└── 3_colab/
    └── Job2_colab.ipynb
```

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job2_PDF_Report` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p2_pdf_report.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `report_tools` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job2_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

### এই জবের বিশেষ নোট

> **সতর্কতা:** package এর নাম `fpdf2`, কিন্তু কোডে `from fpdf import FPDF` লেখা হয়। পুরোনো `fpdf` (সংখ্যা ছাড়া) package install করবেন না। সেটিতে `new_x`, `new_y` নেই, তাই error দেবে।

কাজ শেষে Terminal এ `deactivate`।

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে)

### লাইন ১–৩: module আনা

```python
import csv
import os
from fpdf import FPDF
```

- **কী হচ্ছে:** `csv` (CSV লেখা-পড়া), `os` (ফাইল আছে কিনা যাচাই) আর `fpdf2` package থেকে `FPDF` class আনা হলো।
- **কেন `from ... import`:** পুরো module না এনে শুধু দরকারি class টি আনা হয়েছে। তাই কোডে `fpdf.FPDF()` না লিখে শুধু `FPDF()` লেখা যায়।
- **কেন `fpdf2`:** এটি ছোট, শুধু Python এ লেখা (বাইরের কোনো সফটওয়্যার লাগে না) এবং টেবিল-শিরোনাম আঁকা সহজ। তাই Windows, Linux ও Colab সব জায়গায় একইভাবে চলে।

### লাইন ৫–৬: ফাইলের নাম ও কলামের নাম

```python
FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]
```

- **কী হচ্ছে:** CSV ফাইলের নাম আর ৮টি কলামের নাম একটি list এ রাখা হলো।
- **কেন `HEADER` list:** একই list দুই কাজে লাগে: CSV এর প্রথম সারি (header), আর ইনপুট নেওয়ার সময় প্রশ্ন (`Student_Id:`, `Name:` ...)। কলাম যোগ বা বদলাতে হলে শুধু এই এক লাইন বদলালেই হবে।

### লাইন ৯–১২: একজন ছাত্রের তথ্য নেওয়া (লুপ দিয়ে)

```python
def add_student():
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
```

- **কী হচ্ছে:** `add_student` function। মেনুতে 1 দিলে চলে। খালি list `row` তৈরি করে `HEADER` এর প্রতিটি নামের জন্য একবার করে ইনপুট নেয় এবং `append()` দিয়ে list এ যোগ করে।
- **কেন লুপ:** ৮টি তথ্যের জন্য ৮ লাইন `input()` না লিখে এক লুপেই সব নেওয়া যায়। ইনপুটের ক্রম আর CSV কলামের ক্রম আপনা থেকেই মিলে যায়।
- **কেন সব string:** রোল ও ফোন নম্বরে কোনো হিসাব করা হবে না। সংখ্যা হিসেবে রাখলে ফোন নম্বরের শুরুর `0` হারিয়ে যেত।

### লাইন ১৩–১৮: CSV ফাইলে যোগ করা

```python
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow(row)
```

- **কী হচ্ছে:** ফাইল আগে না থাকলে প্রথমে header লেখে, তারপর ছাত্রের সারি যোগ করে।
- **কেন `"a"` (append) mode:** আগের ছাত্রদের তথ্য না মুছে নতুন ছাত্র শেষে যোগ হয়। তাই মেনু থেকে যতবার খুশি ছাত্র যোগ করা যায়, প্রোগ্রাম বন্ধ করে আবার চালালেও তথ্য থাকে।
- `newline=""` Windows এ ফাঁকা লাইন ঠেকায়। `with` ব্লক শেষে ফাইল নিজে থেকেই বন্ধ হয়।

### লাইন ১৯: সংরক্ষণের নিশ্চয়তা

```python
    print("Saved:", row[1])
```

- **কী হচ্ছে:** `row[1]` হলো list এর দ্বিতীয় উপাদান, অর্থাৎ ছাত্রের নাম (index 0 থেকে শুরু হয়)।

### লাইন ২২–২৫: PDF function ও ফাইল আছে কিনা যাচাই

```python
def make_pdf():
    if not os.path.exists(FILE):
        print("No student saved yet!")
        return
```

- **কী হচ্ছে:** `make_pdf` function। মেনুতে 2 দিলে চলে। প্রথমেই দেখে নেয় `students.csv` আছে কিনা।
- **কেন যাচাই:** কোনো ছাত্র যোগ না করেই 2 চাপলে ফাইলটি থাকে না, তখন `open()` এ `FileNotFoundError` হতো। তাই বার্তা দেখিয়ে মেনুতে ফেরত যাওয়া হয়।

### লাইন ২৬–২৯: CSV পড়া ও header-ডাটা আলাদা

```python
    with open(FILE) as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]
```

- **কী হচ্ছে:** `csv.reader(f)` প্রতিটি সারি list হিসেবে দেয়, `list()` দিয়ে সবগুলো একটি বড় list এ আনা হয়। `rows[0]` header, `rows[1:]` (slicing) বাকি সব ছাত্র।
- **কেন আলাদা:** PDF এ header সারি বোল্ড ও রঙিন হবে, ডাটা সারি সাধারণ। তাই দুটি আলাদাভাবে আঁকতে হবে।

### লাইন ৩১–৩২: PDF object ও পাতা তৈরি

```python
    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
```

- **কী হচ্ছে:** `FPDF` class থেকে একটি object (`pdf`) তৈরি হলো (অধ্যায় ৪: OOP)। `orientation="L"` মানে Landscape (আড়াআড়ি) পাতা, `format="A4"` কাগজের মাপ। `add_page()` প্রথম পাতা যোগ করে।
- **কেন Landscape:** ৮টি কলাম আছে। খাড়া (Portrait) A4 এ (২১০ mm চওড়া) সব কলাম ধরবে না। আড়াআড়ি A4 প্রায় ২৯৭ mm চওড়া।
- **কেন `add_page()` লাগে:** পাতা না থাকলে কিছু লেখা যায় না, error দেবে।

### লাইন ৩৩–৩৪: বড় শিরোনাম

```python
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Pabna Polytechnic Institute", align="C", new_x="LMARGIN", new_y="NEXT")
```

- **`set_font(ফন্ট, স্টাইল, সাইজ)`:** এর পরের সব লেখা Helvetica ফন্টে, `"B"` (Bold), ১৬ পয়েন্ট সাইজে হবে। স্টাইল `""` সাধারণ, `"I"` Italic, `"U"` underline।
- **`cell(প্রস্থ, উচ্চতা, লেখা, ...)`:** একটি আয়তাকার ঘরে লেখা বসায়।
  - প্রস্থ `0` মানে ডান মার্জিন পর্যন্ত পুরো লাইন।
  - `10` উচ্চতা (মিলিমিটার)।
  - `align="C"` মাঝখানে (Center)।
- **`new_x="LMARGIN", new_y="NEXT"`:** ঘর আঁকার পর কার্সর বাম মার্জিনে ও পরের লাইনে যাবে। না দিলে পরের লেখা একই লাইনে ডানে বসত।
- **কেন Helvetica:** এটি PDF এর built-in ফন্ট, আলাদা ফন্ট ফাইল লাগে না।

### লাইন ৩৫–৩৭: উপ-শিরোনাম ও ফাঁকা জায়গা

```python
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
```

- **কী হচ্ছে:** সাধারণ (বোল্ড নয়) ১২ সাইজে উপ-শিরোনাম লেখা হলো। `ln(5)` ৫ mm নিচে নামায়।
- **কেন `ln(5)`:** শিরোনাম ও টেবিলের মাঝে একটু ফাঁকা রাখার জন্য, দেখতে পরিষ্কার লাগে।

### লাইন ৩৯: কলামের প্রস্থ

```python
    widths = [28, 45, 25, 25, 20, 30, 35, 40]
```

- **কী হচ্ছে:** ৮টি কলামের প্রতিটির প্রস্থ (মিলিমিটারে) একটি list এ রাখা হলো। Name ও Phone এর লেখা লম্বা, তাই সেগুলো চওড়া।
- **কেন list এ:** লুপে `widths[i]` দিয়ে i নম্বর কলামের প্রস্থ সহজে পাওয়া যায়। মোট ২৪৮ mm, যা Landscape A4 এর লেখার জায়গার মধ্যে ধরে।

### লাইন ৪১–৪৫: header সারি আঁকা

```python
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(200, 220, 255)
    for i in range(len(header)):
        pdf.cell(widths[i], 9, header[i], border=1, align="C", fill=True)
    pdf.ln()
```

- **`set_fill_color(R, G, B)`:** ঘরের পেছনের রং ঠিক করে। (200, 220, 255) হালকা নীল।
- **`for i in range(len(header))`:** `len(header)` = 8, তাই `i` এর মান 0 থেকে 7। প্রতিবার একটি কলামের header ঘর আঁকা হয়।
- **কেন `range(len(...))` (সরাসরি `for h in header` নয়):** একই `i` দিয়ে `header[i]` (লেখা) ও `widths[i]` (প্রস্থ) দুটোই পাওয়া দরকার।
- **`border=1`:** ঘরের চারপাশে রেখা টানে, তাই টেবিলের মতো দেখায়।
- **`fill=True`:** উপরে ঠিক করা রং দিয়ে ঘর ভরাট করে।
- এখানে `new_x`/`new_y` দেওয়া হয়নি, তাই প্রতিটি ঘরের পরে কার্সর **ডানে** সরে। এতে ৮টি ঘর পাশাপাশি বসে।
- **`pdf.ln()`:** সারি শেষে পরের লাইনে নামায় (ডিফল্ট উচ্চতা শেষ ঘরের উচ্চতা)।

### লাইন ৪৭–৫১: ডাটা সারি আঁকা

```python
    pdf.set_font("Helvetica", "", 10)
    for row in data:
        for i in range(len(row)):
            pdf.cell(widths[i], 8, row[i], border=1, align="C")
        pdf.ln()
```

- **কী হচ্ছে:** সাধারণ ফন্টে প্রতিটি ছাত্রের সারি আঁকা হয়। এটি **nested loop**।
  - বাইরের লুপ: প্রতিটি ছাত্র (`row`)।
  - ভিতরের লুপ: সেই ছাত্রের প্রতিটি ঘর (`row[i]`)।
- **কেন এখানে `fill` নেই:** ডাটা সারি সাদা থাকবে, শুধু header রঙিন।
- **`pdf.ln()` ভিতরের লুপের বাইরে কেন:** একজন ছাত্রের ৮টি ঘর আঁকা শেষ হলে তবেই পরের লাইনে যাবে।

### লাইন ৫৩–৫৪: মোট ছাত্র সংখ্যা

```python
    pdf.ln(4)
    pdf.cell(0, 8, "Total students: " + str(len(data)))
```

- **কী হচ্ছে:** একটু ফাঁকা রেখে মোট ছাত্র সংখ্যা লেখা হয়।
- **কেন `str()`:** `len(data)` একটি সংখ্যা (3)। string এর সাথে সংখ্যা `+` দিয়ে জোড়া যায় না (`TypeError`), তাই আগে string বানাতে হয়।

### লাইন ৫৫–৫৬: PDF সংরক্ষণ

```python
    pdf.output("student_report.pdf")
    print("PDF created: student_report.pdf")
```

- **কী হচ্ছে:** এতক্ষণ সব কিছু মেমোরিতে আঁকা হচ্ছিল। `output()` সেটিকে ফাইল হিসেবে ডিস্কে লেখে।
- **কেন জরুরি:** `output()` না দিলে কোনো PDF ফাইল তৈরি হবে না।

---

### লাইন ৫৯–৭০: মেনু: প্রোগ্রাম চালু রাখা ও পছন্দ অনুযায়ী কাজ

```python
while True:
    print("\n1. Add student   2. Make PDF report   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        make_pdf()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
```

- **কী হচ্ছে:** `while True` একটি অসীম লুপ। প্রতিবার মেনু দেখায়, ব্যবহারকারীর পছন্দ নেয় এবং সেই কাজ করে। 3 না দেওয়া পর্যন্ত প্রোগ্রাম চলতে থাকে।
- **কেন মেনু:** এটি একটি application, তাই একবার চালু করে বারবার কাজ করা যায়: যতবার খুশি তথ্য যোগ করা, যেকোনো সময় ফলাফল দেখা। বাস্তব সফটওয়্যার এভাবেই চলে।
- **`input(...).strip()`:** পছন্দের নম্বর লেখা হিসেবে নেয় এবং আগে-পরের স্পেস সরায়।
- **কেন `"1"` (উদ্ধৃতি চিহ্নসহ) দিয়ে তুলনা:** `input()` সবসময় string দেয়। `int()` এ রূপান্তর না করে সরাসরি string তুলনা করায় কেউ অক্ষর দিলেও `ValueError` হয় না, শুধু `else` অংশে "Invalid choice!" দেখায়।
- **`if / elif / else`:** পছন্দ অনুযায়ী ঠিক একটি অংশ চলে। `elif` মানে "নাহলে যদি"।
- **`break`:** 3 দিলে লুপ থেকে বের হয়ে প্রোগ্রাম শেষ হয়।
- **ক্রম লক্ষ করুন:** function গুলো উপরে আগে তৈরি করা হয়েছে, মেনু সবার নিচে। কারণ মেনু function গুলো ডাকে, তাই ডাকার আগে সেগুলো তৈরি থাকতে হবে।

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** **csv_tools.py** CSV এ সারি যোগ ও পড়ার কাজ করে, **pdf_tools.py** PDF বানায়, আর **main.py** মেনু দেখায়, ছাত্রের তথ্য নেয় ও দুটিকে ব্যবহার করে। make_pdf() এ শিরোনাম ও ফাইলের নাম parameter হিসেবে দেওয়া যায়, তাই একই function দিয়ে অন্য যেকোনো রিপোর্টও বানানো যাবে।

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

### `report_tools/__init__.py` — package এর দরজা

```python
"""report_tools package: save/read CSV rows and make a PDF table report."""

from .csv_tools import save_row, read_csv
from .pdf_tools import make_pdf

__all__ = ["save_row", "read_csv", "make_pdf"]
```

- csv_tools ও pdf_tools এর function গুলো relative import (`.`) দিয়ে এনে বাইরে export করে।
- এখন `from report_tools import save_row, read_csv, make_pdf` লেখা যায়।

### `report_tools/csv_tools.py` — CSV এ সারি যোগ ও পড়া

```python
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
```

- `save_row(row, filename, header)`: যেকোনো CSV ফাইলে একটি সারি যোগ করে; ফাইল নতুন হলে আগে header লেখে।
- `read_csv(filename)` দুটি মান একসাথে ফেরত দেয়: `return rows[0], rows[1:]` (একটি **tuple**)। ফাইল না থাকলে `(None, [])` দেয়, তাই error হয় না।

### `report_tools/pdf_tools.py` — PDF তৈরি

```python
from fpdf import FPDF

WIDTHS = [28, 45, 25, 25, 20, 30, 35, 40]


def make_pdf(header, data, filename, title, subtitle, widths=WIDTHS):
    """Make a landscape A4 PDF with a title and a table."""
    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, title, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, subtitle, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(200, 220, 255)
    for i in range(len(header)):
        pdf.cell(widths[i], 9, header[i], border=1, align="C", fill=True)
    pdf.ln()

    pdf.set_font("Helvetica", "", 10)
    for row in data:
        for i in range(len(row)):
            pdf.cell(widths[i], 8, row[i], border=1, align="C")
        pdf.ln()

    pdf.ln(4)
    pdf.cell(0, 8, "Total students: " + str(len(data)))
    pdf.output(filename)
```

- `WIDTHS` module এর ধ্রুবক (constant), কলামের প্রস্থ।
- `make_pdf(header, data, filename, title, subtitle, widths=WIDTHS)`: PDF এর সব কাজ এক function এ। শিরোনাম ও ফাইলের নাম বাইরে থেকে দেওয়া হয়, তাই function টি পুনর্ব্যবহারযোগ্য (reusable)।
- ভিতরের কোড single file এর make_pdf() এর মতোই।

### `main.py` — মেনু, ইনপুট ও রিপোর্ট

```python
from report_tools import save_row, read_csv, make_pdf

FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]


def take_student():
    """Ask every field of one student and save it."""
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
    save_row(row, FILE, HEADER)
    print("Saved:", row[1])


def create_report():
    """Read the CSV and make the PDF report."""
    header, data = read_csv(FILE)
    if not data:
        print("No student saved yet!")
        return
    make_pdf(header, data, "student_report.pdf",
             "Pabna Polytechnic Institute", "Student Information Report - CST")
    print("PDF created: student_report.pdf")


if __name__ == "__main__":
    while True:
        print("\n1. Add student   2. Make PDF report   3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            take_student()
        elif choice == "2":
            create_report()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")
```

- `HEADER` list দুই কাজে লাগে: ইনপুটের প্রশ্ন, আর CSV এর header (save_row কে দেওয়া হয়)।
- `take_student()` লুপ দিয়ে ৮টি তথ্য নেয় এবং `save_row()` দিয়ে সংরক্ষণ করে।
- `create_report()`: `header, data = read_csv(FILE)` ফেরত আসা tuple দুটি ভেরিয়েবলে ভাগ করে (**unpacking**)। `if not data:` কোনো ছাত্র না থাকলে বার্তা দেখায়, নাহলে `make_pdf()` ডাকে।
- `if __name__ == "__main__":` সরাসরি চালালে তবেই মেনু শুরু।

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job2_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: package install |  |
| Cell 2: module import ও কলামের নাম | csv, os ও FPDF আনা; ফাইলের নাম ও ৮টি কলামের নাম ঠিক করা। |
| Cell 3: function ১: add_student() তৈরি | একজন ছাত্রের ৮টি তথ্য নিয়ে CSV তে লেখার function। শুধু তৈরি হবে। |
| Cell 4: function ২: make_pdf() তৈরি | CSV পড়ে টেবিলসহ PDF বানানোর function। শুধু তৈরি হবে। |
| Cell 5: মেনু চালানো | 1 দিলে ছাত্র যোগ, 2 দিলে PDF তৈরি, 3 দিলে শেষ। |
| Cell 6: PDF ডাউনলোড | মেনুতে 2 দিয়ে PDF তৈরির পরে এই cell চালালে student_report.pdf কম্পিউটারে নামবে। |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট (পরীক্ষিত)

```
1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 2
No student saved yet!

1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 1
Student_Id: S001
Name: Rahim Uddin
Roll: 701234
Semester: 3rd
Shift: 1st
Department: CST
Date of Birth: 12-05-2007
Phone: 01712345678
Saved: Rahim Uddin

1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 1
Student_Id: S002
Name: Sumaiya Akter
Roll: 701235
Semester: 3rd
Shift: 1st
Department: CST
Date of Birth: 03-09-2007
Phone: 01812345678
Saved: Sumaiya Akter

1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 2
PDF created: student_report.pdf

1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 3
Bye!
```

তৈরি হওয়া `students.csv`:

```
Student_Id,Name,Roll,Semester,Shift,Department,Date of Birth,Phone
S001,Rahim Uddin,701234,3rd,1st,CST,12-05-2007,01712345678
S002,Sumaiya Akter,701235,3rd,1st,CST,03-09-2007,01812345678
```

`student_report.pdf` দেখতে এমন (Landscape A4):

```
                    Pabna Polytechnic Institute            (বোল্ড, মাঝখানে)
                  Student Information Report - CST

| Student_Id | Name          | Roll   | Semester | Shift | Department | Date of Birth | Phone       |  ← হালকা নীল
| S001       | Rahim Uddin   | 701234 | 3rd      | 1st   | CST        | 12-05-2007    | 01712345678 |
| S002       | Sumaiya Akter | 701235 | 3rd      | 1st   | CST        | 03-09-2007    | 01812345678 |

Total students: 2
```

## অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] **১.** `1_single_file` এর প্রোগ্রাম চালিয়ে নমুনা আউটপুটের সাথে মিলিয়ে দেখুন।
- [ ] **২.** `2_modular` এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই আসছে কিনা দেখুন।
- [ ] **৩.** module সংস্করণে প্রতিটি ফাইল খুলে বলুন কোন function কোন ফাইলে আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] **৪.** Colab এ notebook আপলোড করে একটি একটি cell চালান। প্রতিটি cell এর পরে কী পরিবর্তন হলো খেয়াল করুন।
- [ ] **৫.** "বাড়তি কাজ" থেকে একটি কাজ বেছে নিন। module সংস্করণে নতুন function টি সঠিক module এ যোগ করুন এবং `__init__.py` থেকে export করুন।

## সমস্যা ও সমাধান

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ModuleNotFoundError: No module named 'fpdf'` | environment activate করা নেই বা package install হয়নি। activate করে `pip install -r requirements.txt` দিন। |
| `TypeError: ... unexpected keyword argument 'new_x'` | পুরোনো `fpdf` package install হয়েছে। `pip uninstall fpdf` তারপর `pip install -r requirements.txt`। |
| `PermissionError` | PDF বা CSV কোনো সফটওয়্যারে খোলা আছে। বন্ধ করে আবার চালান। |
| বাংলা নাম `?` বা error দেখায় | Helvetica তে বাংলা অক্ষর নেই। Nikosh/Kalpurush এর `.ttf` ফাইল ফোল্ডারে রেখে `pdf.add_font("Nikosh", "", "Nikosh.ttf")` ও `pdf.set_font("Nikosh", "", 10)` দিন। যুক্তাক্ষর ঠিকভাবে দেখাতে `pdf.set_text_shaping(True)` লাগতে পারে, যার জন্য `uharfbuzz` package install করতে হয়। |

## বাড়তি কাজ (অনুশীলন)

1. মেনুতে `4. Show all students` যোগ করুন, যা CSV এর সব ছাত্র স্ক্রিনে দেখাবে।
2. পাতার নিচে তারিখ ও "Signature" লেখা যোগ করুন।
3. Shift অনুযায়ী আলাদা দুটি টেবিল বানান।

## ভাইভা প্রশ্ন ও উত্তর

1. **`fpdf2` install করলে import এ কী লিখতে হয়?** `from fpdf import FPDF`।
2. **Landscape কেন নেওয়া হয়েছে?** ৮টি কলাম Portrait A4 এ ধরে না, Landscape এ চওড়া জায়গা পাওয়া যায়।
3. **`cell()` এ `border=1` মানে কী?** ঘরের চারপাশে রেখা টানা।
4. **`cell()` এ প্রস্থ `0` দিলে কী হয়?** ঘরটি ডান মার্জিন পর্যন্ত পুরো লাইন জুড়ে হয়।
5. **`rows[1:]` কী দেয়?** header বাদে বাকি সব সারি (slicing)।
6. **`HEADER` list টি কোন দুই কাজে লাগে?** CSV এর প্রথম সারি লিখতে, আর ইনপুট নেওয়ার সময় প্রতিটি প্রশ্ন দেখাতে।
7. **মেনু কেন `while True` লুপের ভিতরে?** যাতে যতবার খুশি ছাত্র যোগ করে তারপর PDF বানানো যায়। Exit (3) দিলে `break` দিয়ে লুপ শেষ হয়।
8. **`pdf.output()` না দিলে কী হবে?** PDF ফাইল তৈরি হবে না, সব কাজ মেমোরিতেই থেকে যাবে।
9. **ফোন নম্বর string হিসেবে কেন রাখা হয়েছে?** সংখ্যা হলে শুরুর ০ হারিয়ে যায় এবং এতে হিসাব করার কিছু নেই।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।
