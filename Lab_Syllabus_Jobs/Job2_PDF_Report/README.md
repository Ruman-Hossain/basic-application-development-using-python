# জব ২: Generate PDF Report from CSV File

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ৩ | **নম্বর:** ৪

## উদ্দেশ্য

ছাত্রদের তথ্য (Student_Id, Name, Roll, Semester, Shift, Department, Date of Birth, Phone) একটি CSV ফাইলে রাখা হবে। তারপর সেই CSV পড়ে টেবিলসহ একটি PDF রিপোর্ট তৈরি করা হবে।

সিলেবাসের ধাপ: 2.1 Setup → 2.2 Store student info into CSV → 2.3 Generate PDF report

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

### লাইন ১–২: module আনা

```python
import csv
from fpdf import FPDF
```

- **কী হচ্ছে:** `csv` (built-in) আনা হলো CSV লেখা-পড়ার জন্য। `fpdf2` package থেকে `FPDF` class আনা হলো।
- **কেন `from ... import`:** পুরো module না এনে শুধু দরকারি class টি আনা হয়েছে। তাই কোডে `fpdf.FPDF()` না লিখে শুধু `FPDF()` লেখা যায়।
- **কেন `fpdf2`:** এটি ছোট, শুধু Python এ লেখা (বাইরের কোনো সফটওয়্যার লাগে না) এবং টেবিল-শিরোনাম আঁকা সহজ। তাই Windows, Linux ও Colab সব জায়গায় একইভাবে চলে।

### লাইন ৪–১০: ছাত্রদের তথ্য একটি list এ

```python
students = [
    ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"],
    ["S001", "Rahim Uddin", "701234", "3rd", "1st", "CST", "12-05-2007", "01712345678"],
    ...
]
```

- **কী হচ্ছে:** `students` একটি **list এর list** (nested list)। প্রথম ভিতরের list টি কলামের নাম (header), পরের প্রতিটি list একজন ছাত্রের তথ্য।
- **কেন সব মান string (`"701234"`):** রোল ও ফোন নম্বরে কোনো হিসাব করা হবে না, শুধু দেখানো হবে। সংখ্যা হিসেবে রাখলে ফোন নম্বরের শুরুর `0` হারিয়ে যেত (`01712345678` → `1712345678`)।
- `#` দিয়ে শুরু হওয়া লাইন comment, Python এটি চালায় না। শুধু বোঝার জন্য লেখা।

### লাইন ১১–১৩: CSV ফাইলে লেখা

```python
with open("students.csv", "w", newline="") as f:
    csv.writer(f).writerows(students)
print("CSV saved: students.csv")
```

- **কী হচ্ছে:** `students.csv` লেখার জন্য খোলা হলো। `writerows()` (শেষে **s**) পুরো list এর সব সারি একবারে লেখে।
- **কেন `"w"` mode:** এখানে প্রতিবার একই তথ্য দিয়ে নতুন ফাইল বানানো হচ্ছে, তাই আগেরটি মুছে নতুন লেখা ঠিক আছে। (জব ১ এ `"a"` ছিল কারণ সেখানে রেকর্ড জমাতে হয়েছিল।)
- **কেন `writerows` (`writerow` নয়):** `writerow` একটি সারি লেখে। `writerows` অনেকগুলো সারি একসাথে লেখে, লুপ লাগে না।
- `newline=""` Windows এ ফাঁকা লাইন ঠেকায়। `with` ব্লক শেষে ফাইল বন্ধ হয়।

### লাইন ১৫–১৭: CSV ফাইল পড়া

```python
with open("students.csv") as f:
    rows = list(csv.reader(f))
```

- **কী হচ্ছে:** ফাইলটি পড়ার জন্য খোলা হলো (ডিফল্ট `"r"` mode)। `csv.reader(f)` প্রতিটি সারি একটি list হিসেবে দেয়। `list()` দিয়ে সবগুলো একটি বড় list এ নেওয়া হলো।
- **কেন `list()` এ রূপান্তর:** `csv.reader` একবারে একটি সারি দেয় এবং শুধু ফাইল খোলা থাকা অবস্থায় কাজ করে। list বানিয়ে নিলে ফাইল বন্ধ হওয়ার পরেও সব ডাটা ব্যবহার করা যায়, এবং `rows[0]` এর মতো index দিয়ে নেওয়া যায়।
- **কেন আবার পড়ছি:** সিলেবাসের কাজ হলো **CSV থেকে** রিপোর্ট বানানো। বাস্তবে CSV আগে থেকেই থাকবে (যেমন অফিস থেকে পাওয়া), তখন লাইন ৪–১৩ বাদ দিয়ে এখান থেকেই শুরু হবে।

### লাইন ১৮–১৯: header ও ডাটা আলাদা

```python
header = rows[0]
data = rows[1:]
```

- **কী হচ্ছে:** `rows[0]` প্রথম সারি (কলামের নাম)। `rows[1:]` **slicing**: index 1 থেকে শেষ পর্যন্ত, অর্থাৎ শুধু ছাত্রদের সারি।
- **কেন আলাদা:** PDF এ header সারি বোল্ড ও রঙিন হবে, ডাটা সারি সাধারণ। তাই দুটি আলাদাভাবে আঁকতে হবে।

### লাইন ২২–২৩: PDF object ও পাতা তৈরি

```python
pdf = FPDF(orientation="L", format="A4")
pdf.add_page()
```

- **কী হচ্ছে:** `FPDF` class থেকে একটি object (`pdf`) তৈরি হলো (অধ্যায় ৪: OOP)। `orientation="L"` মানে Landscape (আড়াআড়ি) পাতা, `format="A4"` কাগজের মাপ। `add_page()` প্রথম পাতা যোগ করে।
- **কেন Landscape:** ৮টি কলাম আছে। খাড়া (Portrait) A4 এ (২১০ mm চওড়া) সব কলাম ধরবে না। আড়াআড়ি A4 প্রায় ২৯৭ mm চওড়া।
- **কেন `add_page()` লাগে:** পাতা না থাকলে কিছু লেখা যায় না, error দেবে।

### লাইন ২৪–২৫: বড় শিরোনাম

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

### লাইন ২৬–২৮: উপ-শিরোনাম ও ফাঁকা জায়গা

```python
pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
```

- **কী হচ্ছে:** সাধারণ (বোল্ড নয়) ১২ সাইজে উপ-শিরোনাম লেখা হলো। `ln(5)` ৫ mm নিচে নামায়।
- **কেন `ln(5)`:** শিরোনাম ও টেবিলের মাঝে একটু ফাঁকা রাখার জন্য, দেখতে পরিষ্কার লাগে।

### লাইন ৩০: কলামের প্রস্থ

```python
widths = [28, 45, 25, 25, 20, 30, 35, 40]
```

- **কী হচ্ছে:** ৮টি কলামের প্রতিটির প্রস্থ (মিলিমিটারে) একটি list এ রাখা হলো। Name ও Phone এর লেখা লম্বা, তাই সেগুলো চওড়া।
- **কেন list এ:** লুপে `widths[i]` দিয়ে i নম্বর কলামের প্রস্থ সহজে পাওয়া যায়। মোট ২৪৮ mm, যা Landscape A4 এর লেখার জায়গার মধ্যে ধরে।

### লাইন ৩২–৩৬: header সারি আঁকা

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

### লাইন ৩৮–৪২: ডাটা সারি আঁকা

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

### লাইন ৪৪–৪৫: মোট ছাত্র সংখ্যা

```python
pdf.ln(4)
pdf.cell(0, 8, "Total students: " + str(len(data)))
```

- **কী হচ্ছে:** একটু ফাঁকা রেখে মোট ছাত্র সংখ্যা লেখা হয়।
- **কেন `str()`:** `len(data)` একটি সংখ্যা (3)। string এর সাথে সংখ্যা `+` দিয়ে জোড়া যায় না (`TypeError`), তাই আগে string বানাতে হয়।

### লাইন ৪৬–৪৭: PDF সংরক্ষণ

```python
pdf.output("student_report.pdf")
print("PDF created: student_report.pdf")
```

- **কী হচ্ছে:** এতক্ষণ সব কিছু মেমোরিতে আঁকা হচ্ছিল। `output()` সেটিকে ফাইল হিসেবে ডিস্কে লেখে।
- **কেন জরুরি:** `output()` না দিলে কোনো PDF ফাইল তৈরি হবে না।

---

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** **csv_tools.py** CSV লেখা-পড়া করে, **pdf_tools.py** PDF বানায়, আর **main.py** ডাটা দিয়ে দুটিকে ব্যবহার করে। make_pdf() এ শিরোনাম ও ফাইলের নাম parameter হিসেবে দেওয়া যায়, তাই একই function দিয়ে অন্য যেকোনো রিপোর্টও বানানো যাবে।

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
"""report_tools package: write/read CSV files and make a PDF table report."""

from .csv_tools import save_csv, read_csv
from .pdf_tools import make_pdf

__all__ = ["save_csv", "read_csv", "make_pdf"]
```

- csv_tools ও pdf_tools এর function গুলো relative import (`.`) দিয়ে এনে বাইরে export করে।
- এখন `from report_tools import save_csv, read_csv, make_pdf` লেখা যায়।

### `report_tools/csv_tools.py` — CSV লেখা ও পড়া

```python
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
```

- `save_csv(rows, filename)`: যেকোনো list এর list যেকোনো নামের CSV তে লেখে।
- `read_csv(filename)` দুটি মান একসাথে ফেরত দেয়: `return rows[0], rows[1:]`। Python এটিকে একটি **tuple** হিসেবে দেয়।

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
- ভিতরের কোড single file এর Step 3 এর মতোই।

### `main.py` — ডাটা ও প্রোগ্রাম চালানো

```python
from report_tools import save_csv, read_csv, make_pdf

students = [
    ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"],
    ["S001", "Rahim Uddin", "701234", "3rd", "1st", "CST", "12-05-2007", "01712345678"],
    ["S002", "Sumaiya Akter", "701235", "3rd", "1st", "CST", "03-09-2007", "01812345678"],
    ["S003", "Karim Hasan", "701236", "3rd", "2nd", "CST", "21-01-2008", "01912345678"],
]

if __name__ == "__main__":
    save_csv(students, "students.csv")
    print("CSV saved: students.csv")

    header, data = read_csv("students.csv")
    make_pdf(header, data, "student_report.pdf",
             "Pabna Polytechnic Institute", "Student Information Report - CST")
    print("PDF created: student_report.pdf")
```

- `header, data = read_csv("students.csv")`: ফেরত আসা tuple দুটি ভেরিয়েবলে ভাগ হয় (**unpacking**)।
- `make_pdf(...)` এ argument গুলো ক্রমানুসারে parameter এ যায়। লম্বা লাইন দুই লাইনে ভাঙা হয়েছে, বন্ধনীর ভিতরে থাকায় সমস্যা নেই।
- `if __name__ == "__main__":` সরাসরি চালালে তবেই কাজ শুরু।

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
| Cell 2: module import | csv ও fpdf2 থেকে FPDF আনা। |
| Cell 3: ধাপ ১: ছাত্রদের তথ্য CSV তে লেখা | students.csv তৈরি হবে। |
| Cell 4: ধাপ ২: CSV ফাইল পড়া | header ও data আলাদা হবে। দেখতে চাইলে পরের লাইনে print(header) লিখে চালান। |
| Cell 5: ধাপ ৩: PDF পাতা ও শিরোনাম | Landscape A4 পাতা, বড় শিরোনাম ও উপ-শিরোনাম। |
| Cell 6: ধাপ ৪: header সারি (রঙিন) | কলামের প্রস্থ ঠিক করে হালকা নীল header সারি আঁকা। |
| Cell 7: ধাপ ৫: ছাত্রদের সারি | nested loop দিয়ে প্রতিটি ছাত্রের সারি আঁকা। |
| Cell 8: ধাপ ৬: মোট সংখ্যা ও PDF সংরক্ষণ | student_report.pdf তৈরি হবে। |
| Cell 9: PDF ডাউনলোড | student_report.pdf কম্পিউটারে নামবে। |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট (পরীক্ষিত)

এই জবে কীবোর্ড ইনপুট নেই। ইনপুট হলো CSV এর তথ্য।

কনসোল আউটপুট:
```
CSV saved: students.csv
PDF created: student_report.pdf
```

`student_report.pdf` দেখতে এমন (Landscape A4):

```
                    Pabna Polytechnic Institute            (বোল্ড, মাঝখানে)
                  Student Information Report - CST

| Student_Id | Name          | Roll   | Semester | Shift | Department | Date of Birth | Phone       |  ← হালকা নীল
| S001       | Rahim Uddin   | 701234 | 3rd      | 1st   | CST        | 12-05-2007    | 01712345678 |
| S002       | Sumaiya Akter | 701235 | 3rd      | 1st   | CST        | 03-09-2007    | 01812345678 |
| S003       | Karim Hasan   | 701236 | 3rd      | 2nd   | CST        | 21-01-2008    | 01912345678 |

Total students: 3
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

1. হাতে লেখা ডাটা বাদ দিয়ে একটি বিদ্যমান CSV (যেমন Excel থেকে save করা) পড়ে রিপোর্ট বানান।
2. পাতার নিচে তারিখ ও "Signature" লেখা যোগ করুন।
3. Shift অনুযায়ী আলাদা দুটি টেবিল বানান।

## ভাইভা প্রশ্ন ও উত্তর

1. **`fpdf2` install করলে import এ কী লিখতে হয়?** `from fpdf import FPDF`।
2. **Landscape কেন নেওয়া হয়েছে?** ৮টি কলাম Portrait A4 এ ধরে না, Landscape এ চওড়া জায়গা পাওয়া যায়।
3. **`cell()` এ `border=1` মানে কী?** ঘরের চারপাশে রেখা টানা।
4. **`cell()` এ প্রস্থ `0` দিলে কী হয়?** ঘরটি ডান মার্জিন পর্যন্ত পুরো লাইন জুড়ে হয়।
5. **`rows[1:]` কী দেয়?** header বাদে বাকি সব সারি (slicing)।
6. **`writerow` ও `writerows` এর পার্থক্য কী?** `writerow` একটি সারি লেখে, `writerows` অনেকগুলো সারি একবারে লেখে।
7. **`pdf.output()` না দিলে কী হবে?** PDF ফাইল তৈরি হবে না, সব কাজ মেমোরিতেই থেকে যাবে।
8. **ফোন নম্বর string হিসেবে কেন রাখা হয়েছে?** সংখ্যা হলে শুরুর ০ হারিয়ে যায় এবং এতে হিসাব করার কিছু নেই।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।
