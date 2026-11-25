# Python ব্যবহারিক: ৬টি জব — সহজ গাইড

**28531 Application Development Using Python** · ৩য় পর্ব, CST · পাবনা সরকারি পলিটেকনিক ইনস্টিটিউট
প্রস্তুতকারী: **মোঃ রুমান হোসেন**, ইন্সট্রাক্টর (CST)

> এটি [28531_Python_Jobs_Easy_Guide.pdf](28531_Python_Jobs_Easy_Guide.pdf) এর GitHub সংস্করণ। বিষয়বস্তু একই। কোডের বক্সের উপরে ডান কোণের **Copy** বোতাম দিয়ে সরাসরি কপি করা যায়।

## সূচি

- [ধাপ ১: একবারই যা install করবেন](#ধাপ-১-একবারই-যা-install-করবেন)
- [ধাপ ২: ফোল্ডার ও তিন ধরনের সমাধান](#ধাপ-২-ফোল্ডার-ও-তিন-ধরনের-সমাধান)
- [ধাপ ৩: Virtual Environment](#ধাপ-৩-virtual-environment)
- [Module ও Package: মূল ধারণা](#module-ও-package-মূল-ধারণা-অধ্যায়-৩)
- [জব ১: Fruit Inventory (CSV)](#জব-১-fruit-inventory-csv)
- [জব ২: CSV থেকে PDF Report](#জব-২-csv-থেকে-pdf-report)
- [জব ৩: QR Code ও Barcode](#জব-৩-qr-code-ও-barcode)
- [জব ৪: Web Scraping](#জব-৪-web-scraping)
- [জব ৫: Weather Report (API)](#জব-৫-weather-report-api)
- [জব ৬: Database App (Form + SQLite)](#জব-৬-database-app-form--sqlite)
- [Google Colab: সাধারণ নিয়ম](#google-colab-সাধারণ-নিয়ম)
- [সমস্যা হলে](#সমস্যা-হলে)

---

## ধাপ ১: একবারই যা install করবেন

1. **Python:** python.org/downloads থেকে ডাউনলোড করুন। install এর প্রথম পাতায় **“Add python.exe to PATH” অবশ্যই টিক দিন**, তারপর Install Now।
2. **VS Code:** code.visualstudio.com থেকে install করুন। Extensions (Ctrl+Shift+X) থেকে **Python** extension install করুন।
3. **যাচাই:** CMD খুলে লিখুন:

```bash
python --version
```

Python 3.9 বা নতুন version দেখালে ঠিক আছে।

## ধাপ ২: ফোল্ডার ও তিন ধরনের সমাধান

প্রতিটি জব **তিনভাবে** করা আছে। তিনটিই একই কাজ করে ও একই আউটপুট দেয়:

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে | নিজের কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ, `import` ও export (অধ্যায় ৩) | নিজের কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | .ipynb notebook, কোড আলাদা cell এ | ব্রাউজারে |

```
Lab_Syllabus_Jobs/
├── Job1_Fruit_Inventory/
│   ├── README.md
│   ├── requirements.txt
│   ├── 1_single_file/
│   │   └── p1_inventory.py
│   ├── 2_modular/
│   │   ├── main.py
│   │   └── fruit_inventory/
│   │       ├── __init__.py
│   │       ├── report.py
│   │       └── storage.py
│   └── 3_colab/
│       └── Job1_colab.ipynb
├── Job2_PDF_Report/      (একই গঠন, package: report_tools)
├── Job3_QR_Barcode/      (package: codes)
├── Job4_Web_Scraping/    (package: scraper)
├── Job5_Weather_Report/  (package: weather)
└── Job6_Database_App/    (package: student_db)
```

> **ফাইল বানানোর সহজ উপায়:** VS Code এ **File → Open Folder** দিয়ে জবের ফোল্ডার খুলুন। বাম পাশে **New Folder / New File** আইকনে ক্লিক করে নাম লিখুন, তারপর এই গাইড থেকে কোড কপি করে পেস্ট করুন এবং Ctrl+S দিয়ে save করুন।

## ধাপ ৩: Virtual Environment

Virtual environment হলো প্রতিটি প্রজেক্টের **নিজস্ব আলাদা Python**। package এর ভিতরেই install হয়, কম্পিউটারের মূল Python এ নয়। তাই এক প্রজেক্ট অন্যটিকে নষ্ট করে না।

VS Code এ **জবের ফোল্ডার** (যেমন `Job1_Fruit_Inventory`) খোলা অবস্থায় **Terminal → New Terminal** দিন। একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

**১. environment তৈরি (প্রথমবার শুধু)**

```bash
python -m venv venv
```

**২. environment চালু (প্রতিবার নতুন Terminal খুললে)**

| সিস্টেম | কমান্ড |
|---|---|
| Windows (CMD) | `venv\Scripts\activate` |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| Linux / Mac | `source venv/bin/activate` |

সফল হলে লাইনের শুরুতে **`(venv)`** দেখা যাবে। PowerShell এ “running scripts is disabled” error এলে একবার চালান:

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**৩. package install**

```bash
pip install -r requirements.txt
```

**৪. প্রোগ্রাম চালানো**

সমাধান ১ (single file):
```bash
cd 1_single_file
python p1_inventory.py
```

সমাধান ২ (module/package): `main.py` সবসময় `2_modular` ফোল্ডার থেকে চালাবেন:
```bash
cd ../2_modular
python main.py
```

**৫. কাজ শেষে environment বন্ধ**

```bash
deactivate
```

> **VS Code এর ▶ (Run) বোতাম ব্যবহার করলে:** Ctrl+Shift+P → **Python: Select Interpreter** → venv বেছে নিন।

## Module ও Package: মূল ধারণা (অধ্যায় ৩)

সমাধান ২ এ একই প্রোগ্রাম কয়েকটি ফাইলে ভাগ করা হয়েছে। প্রতিটি ফাইল একটি নির্দিষ্ট কাজ করে, আর `main.py` সেগুলো `import` করে ব্যবহার করে।

| শব্দ | মানে |
|---|---|
| module | একটি `.py` ফাইল। যেমন `storage.py`। |
| package | কয়েকটি module সহ একটি ফোল্ডার, যার ভিতরে `__init__.py` আছে। |
| import | অন্য module/package থেকে function বা ভেরিয়েবল আনা: `from package import function`। |
| export | package এর `__init__.py` তে import করে রাখা, যাতে বাইরে থেকে সহজে নেওয়া যায়। `__all__` তালিকায় নামগুলো লেখা থাকে। |
| relative import | `from .storage import ...`: ডট (.) মানে একই package এর ভিতরের ফাইল। |
| `if __name__ == "__main__":` | ফাইলটি সরাসরি চালালে (`python main.py`) নিচের কোড চলে। import করলে চলে না। |
| return | function এর ফলাফল ডাকার জায়গায় ফেরত পাঠানো। একাধিক মান ফেরত দিলে tuple হয়। |

উদাহরণ (জব ১): package থেকে function আনা

```python
from fruit_inventory import add_item, read_items, print_summary
```

এটি কাজ করে কারণ `fruit_inventory/__init__.py` ফাইলে লেখা আছে:

```python
from .storage import FILE, add_item, read_items
from .report import print_summary

__all__ = ["FILE", "add_item", "read_items", "print_summary"]
```

> **কেন module এ ভাগ করব?** কোড ছোট ছোট ফাইলে থাকলে পড়া সহজ হয়, পরিবর্তন করতে শুধু একটি ফাইল খুলতে হয়, অন্য প্রজেক্টে `import` করে আবার ব্যবহার করা যায়, আর প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯: Unit Testing)।

---

## জব ১: Fruit Inventory (CSV)

**কাজ:** মেনু-ভিত্তিক application: ফলের নাম, দাম ও পরিমাণ নিয়ে fruits.csv ফাইলে রাখে, যেকোনো সময় সারাংশ দেখায়। মেনু: 1 Add fruit, 2 Show summary, 3 Exit।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p1_inventory.py`](../Job1_Fruit_Inventory/1_single_file/p1_inventory.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job1_Fruit_Inventory/2_modular/main.py) + `fruit_inventory/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job1_colab.ipynb`](../Job1_Fruit_Inventory/3_colab/Job1_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** fruits.csv · **বিস্তারিত README:** [Job1_Fruit_Inventory/README.md](../Job1_Fruit_Inventory/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
# এই জবে বাইরের কোনো package লাগে না
```

### সমাধান ১: Single file (`1_single_file/p1_inventory.py`)

```python
import csv
import os

FILE = "fruits.csv"


def add_item():
    name = input("Fruit name: ").strip()
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
    total = price * qty
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
        writer.writerow([name, price, qty, total])
    print("Saved:", name, "| Total =", total, "Tk")


def show_summary():
    if not os.path.exists(FILE):
        print("No fruit saved yet!")
        return
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
    with open(FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
            grand_total += float(row["Total Price"])
            total_qty += int(row["Quantity"])
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")


while True:
    print("\n1. Add fruit   2. Show summary   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_item()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
```

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p1_inventory.py
```

যা দেখা যাবে:

```text
1. Add fruit   2. Show summary   3. Exit
Choose (1-3): 1
Fruit name: Apple
Unit price (Tk): 250
Quantity (kg): 5
Saved: Apple | Total = 1250.0 Tk

1. Add fruit   2. Show summary   3. Exit
Choose (1-3): 1
Fruit name: Mango
Unit price (Tk): 120
Quantity (kg): abc
Invalid number! Try again.

1. Add fruit   2. Show summary   3. Exit
Choose (1-3): 2

------ Fruit Inventory Summary ------
Apple         250.0 x   5 =   1250.0 Tk
-------------------------------------
Total quantity : 5 kg
Grand total    : 1250.0 Tk

1. Add fruit   2. Show summary   3. Exit
Choose (1-3): 3
Bye!
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

#### লাইন ১–২: প্রয়োজনীয় module আনা

```python
import csv
import os
```

- **কী হচ্ছে:** Python এর সাথে আসা দুটি module প্রোগ্রামে আনা হচ্ছে।
- **কেন `csv`:** CSV ফাইলে সঠিকভাবে লেখা ও পড়ার জন্য। নিজে হাতে কমা বসালে ভুলের সম্ভাবনা থাকে। যেমন নামের ভিতরে কমা থাকলে কলাম ভেঙে যায়। `csv` module এগুলো নিজেই সামলায়।
- **কেন `os`:** ফাইলটি আগে থেকে আছে কিনা যাচাই করার জন্য (`os.path.exists`)।
- দুটিই built-in, তাই `pip install` লাগে না।

#### লাইন ৪: ফাইলের নাম একটি ভেরিয়েবলে

```python
FILE = "fruits.csv"
```

- **কী হচ্ছে:** ফাইলের নাম `FILE` নামের ভেরিয়েবলে রাখা হলো।
- **কেন:** একই নাম প্রোগ্রামে কয়েকবার লাগে। নাম বদলাতে হলে শুধু এই এক লাইন বদলালেই হবে। বড় হাতের নাম (`FILE`) দিয়ে বোঝানো হয় এটি একটি ধ্রুবক (constant), প্রোগ্রাম চলার সময় বদলাবে না।

#### লাইন ৭: একটি ফল যোগ করার function শুরু

```python
def add_item():
```

- **কী হচ্ছে:** `add_item` নামে একটি function তৈরি হলো। কাজ: একটি ফলের তথ্য নেওয়া ও CSV তে লেখা। মেনুতে 1 দিলে এটি চলে।
- **কেন function:** প্রতিটি কাজ আলাদা function এ রাখলে কোড পড়তে ও ঠিক করতে সহজ হয় (অধ্যায় ১)। মেনু থেকে শুধু নাম ধরে ডাকলেই কাজ হয়।

#### লাইন ৮: ফলের নাম ইনপুট

```python
    name = input("Fruit name: ").strip()
```

- **কী হচ্ছে:** `input()` কীবোর্ড থেকে লেখা নেয়। `.strip()` লেখার শুরু ও শেষের অতিরিক্ত স্পেস সরিয়ে দেয়।
- **কেন `.strip()`:** কেউ ভুলে `" Apple "` লিখলেও ফাইলে পরিষ্কার `Apple` যাবে।

#### লাইন ৯–১৪: দাম ও পরিমাণ নেওয়া, ভুল ইনপুট সামলানো

```python
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
```

- **কী হচ্ছে:** `input()` সবসময় string দেয়। দামকে `float()` দিয়ে দশমিক সংখ্যায় আর পরিমাণকে `int()` দিয়ে পূর্ণসংখ্যায় রূপান্তর করা হয়।
- **কেন `float` ও `int`:** দামে দশমিক থাকতে পারে (যেমন 120.50), কিন্তু এখানে পরিমাণ পূর্ণ কেজিতে ধরা হয়েছে। string দিয়ে গুণ করা যায় না, তাই রূপান্তর লাগে।
- **কেন `try-except ValueError`:** কেউ সংখ্যার জায়গায় `abc` লিখলে `float()`/`int()` একটি `ValueError` দেয়। `try-except` না থাকলে প্রোগ্রাম সেখানেই বন্ধ হয়ে যেত। এখন একটি বার্তা দেখায় (অধ্যায় ৭: Exception Handling)।
- **কেন `return`:** ভুল তথ্য ফাইলে না লিখে function এখানেই শেষ হয় এবং প্রোগ্রাম আবার মেনুতে ফিরে যায়।

#### লাইন ১৫: মোট দাম হিসাব

```python
    total = price * qty
```

- **কী হচ্ছে:** একক দাম × পরিমাণ = মোট দাম।

#### লাইন ১৬: ফাইল আগে ছিল কিনা যাচাই

```python
    new_file = not os.path.exists(FILE)
```

- **কী হচ্ছে:** `os.path.exists(FILE)` ফাইল থাকলে `True`, না থাকলে `False` দেয়। সামনে `not` থাকায় ফলাফল উল্টে যায়। ফলে ফাইল **না থাকলে** `new_file` হবে `True`।
- **কেন:** কলামের নাম (header) শুধু প্রথমবার লিখতে হবে। প্রোগ্রাম বারবার চালালে header যেন বারবার না আসে।
- **গুরুত্বপূর্ণ:** এই যাচাই অবশ্যই ফাইল খোলার **আগে** করতে হবে। কারণ পরের লাইনে `"a"` mode এ খুললে ফাইলটি তৈরি হয়ে যায়।

#### লাইন ১৭: ফাইল append mode এ খোলা

```python
    with open(FILE, "a", newline="") as f:
```

- **কী হচ্ছে:** `fruits.csv` ফাইলটি খোলা হলো, আর এর নাম দেওয়া হলো `f`।
- **কেন `"a"` (append):** `"w"` mode দিলে প্রতিবার আগের সব ডাটা মুছে যেত। `"a"` আগের রেকর্ড রেখে শেষে নতুন রেকর্ড যোগ করে। ফাইল না থাকলে নতুন তৈরি করে।
- **কেন `newline=""`:** Windows এ এটা না দিলে প্রতিটি সারির পরে একটি ফাঁকা লাইন চলে আসে। `csv` module এর ডকুমেন্টেশনেও এটি দিতে বলা হয়েছে।
- **কেন `with`:** `with` ব্লক শেষ হলে ফাইল নিজে থেকেই বন্ধ (close) হয়ে যায়, এমনকি মাঝপথে error হলেও। এতে ডাটা নিরাপদে সংরক্ষিত হয়।

#### লাইন ১৮: CSV writer তৈরি

```python
        writer = csv.writer(f)
```

- **কী হচ্ছে:** খোলা ফাইলের জন্য একটি `writer` object তৈরি হলো।
- **কেন:** `writer.writerow()` দিয়ে একটি list দিলে সেটি কমা দিয়ে সঠিক CSV সারি বানিয়ে ফাইলে লেখে।

#### লাইন ১৯–২০: নতুন ফাইল হলে header লেখা

```python
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
```

- **কী হচ্ছে:** ফাইল নতুন হলে প্রথম সারিতে চারটি কলামের নাম লেখা হয়।
- **কেন:** header থাকলে Excel এ খুললে কলামের নাম দেখা যায়। পরে `DictReader` এই নামগুলো দিয়েই মান খুঁজবে।

#### লাইন ২১: একটি সারি CSV তে লেখা

```python
        writer.writerow([name, price, qty, total])
```

- **কী হচ্ছে:** চারটি মান একটি list আকারে দিয়ে ফাইলে এক সারিতে লেখা হয়। যেমন `Apple,250.0,5,1250.0`।
- **কেন list:** `writerow()` একটি list (বা tuple) চায়। list এর প্রতিটি উপাদান একটি কলাম হয়।

#### লাইন ২২: সংরক্ষণের নিশ্চয়তা দেখানো

```python
    print("Saved:", name, "| Total =", total, "Tk")
```

- **কী হচ্ছে:** ব্যবহারকারীকে জানানো হয় কোন ফল সংরক্ষিত হলো এবং তার মোট দাম কত।
- **কেন:** ফিডব্যাক পেলে ব্যবহারকারী বুঝতে পারে ইনপুট ঠিকভাবে গৃহীত হয়েছে। `print()` এ কমা দিয়ে একাধিক মান দিলে মাঝে নিজে থেকে স্পেস বসে।

#### লাইন ২৫–২৮: সারাংশের function ও ফাইল আছে কিনা যাচাই

```python
def show_summary():
    if not os.path.exists(FILE):
        print("No fruit saved yet!")
        return
```

- **কী হচ্ছে:** `show_summary` function শুরু। মেনুতে 2 দিলে এটি চলে। প্রথমেই দেখে নেয় `fruits.csv` আছে কিনা।
- **কেন যাচাই:** কেউ কোনো ফল যোগ না করেই 2 চাপলে ফাইলটি থাকে না। তখন `open()` একটি `FileNotFoundError` দিয়ে প্রোগ্রাম বন্ধ করে দিত। তাই আগেই বার্তা দেখিয়ে `return` দিয়ে মেনুতে ফেরত যাওয়া হয়।

#### লাইন ২৯–৩১: শিরোনাম ও শুরুর মান

```python
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
```

- **কী হচ্ছে:** `"\n"` একটি ফাঁকা লাইন দিয়ে শিরোনাম ছাপে। দুটি যোগফলের ভেরিয়েবল `0` দিয়ে শুরু হয়।
- **কেন 0 দিয়ে শুরু:** লুপে প্রতিটি সারির মান এগুলোর সাথে যোগ হবে। শুরুর মান না দিলে যোগ করা যায় না (`NameError`)।

#### লাইন ৩২–৩৩: CSV ফাইল পড়ার জন্য খোলা

```python
    with open(FILE) as f:
        reader = csv.DictReader(f)
```

- **কী হচ্ছে:** ফাইলটি পড়ার জন্য খোলা হলো। mode না দিলে ডিফল্ট `"r"` (read)। `csv.DictReader` প্রতিটি সারিকে একটি **dictionary** বানায়, যেখানে key হলো header এর কলামের নাম।
- **কেন `DictReader` (`csv.reader` নয়):** `row['Fruit']` এভাবে নাম দিয়ে মান পাওয়া যায়, `row[0]` এর মতো নম্বর মনে রাখতে হয় না। কলামের ক্রম বদলালেও কোড ঠিক থাকে, আর কোড পড়তে সহজ হয়।

#### লাইন ৩৪–৩৫: প্রতিটি সারি সুন্দর করে ছাপা

```python
        for row in reader:
            print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
```

- **কী হচ্ছে:** `for` লুপ ফাইলের প্রতিটি ডাটা সারি একটি একটি করে নেয়। header সারিটি `DictReader` নিজেই key হিসেবে ব্যবহার করে, তাই সেটি লুপে আসে না।
- **কেন f-string:** `f"...{ভেরিয়েবল}..."` দিয়ে লেখার ভিতরে সরাসরি মান বসানো যায়।
- **`:<10`, `:>8`, `:>3` কী:** ফরম্যাট নির্দেশ।
  - `:<10` মানে মোট ১০ ঘর জায়গা নিয়ে **বামে** সাজানো।
  - `:>8` মানে ৮ ঘর জায়গা নিয়ে **ডানে** সাজানো।
  - **কেন:** নাম ছোট-বড় হলেও সংখ্যাগুলো টেবিলের মতো এক লাইনে থাকে।

#### লাইন ৩৬–৩৭: যোগফল হিসাব

```python
            grand_total += float(row["Total Price"])
            total_qty += int(row["Quantity"])
```

- **কী হচ্ছে:** প্রতিটি সারির মোট দাম `grand_total` এ আর পরিমাণ `total_qty` তে যোগ হয়। `a += b` মানে `a = a + b`।
- **কেন `float()` ও `int()` আবার:** CSV ফাইল থেকে পড়া **সব মানই string** হিসেবে আসে (`"1250.0"`)। string যোগ করলে জোড়া লেগে যায় (`"1250.0" + "1200.0"` = `"1250.01200.0"`)। তাই আগে সংখ্যায় রূপান্তর করতে হয়।

#### লাইন ৩৮–৪০: সারাংশ ছাপা

```python
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")
```

- **কী হচ্ছে:** একটি বিভাজক রেখা, তারপর মোট পরিমাণ ও সর্বমোট দাম ছাপা হয়। লুপ শেষ হওয়ার পরে ছাপা হয় (indentation লক্ষ করুন), তাই একবারই আসে।

#### লাইন ৪৩–৫৪: মেনু: প্রোগ্রাম চালু রাখা ও পছন্দ অনুযায়ী কাজ

```python
while True:
    print("\n1. Add fruit   2. Show summary   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_item()
    elif choice == "2":
        show_summary()
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

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** কাজগুলো তিন ভাগে ভাগ করা হয়েছে। **storage.py** শুধু CSV ফাইলে লেখা-পড়া করে, **report.py** শুধু সারাংশ ছাপে, আর **main.py** মেনু দেখায় ও ব্যবহারকারীর ইনপুট নেয়। ফলে ফাইলের কাজ বদলাতে হলে শুধু storage.py খুলতে হয়।

```text
2_modular/
├── main.py
└── fruit_inventory/
    ├── __init__.py
    ├── report.py
    └── storage.py
```

#### `fruit_inventory/__init__.py` — package এর দরজা

```python
"""fruit_inventory package: save fruit data in a CSV file and show a summary."""

from .storage import FILE, add_item, read_items
from .report import print_summary

__all__ = ["FILE", "add_item", "read_items", "print_summary"]
```

- এই ফাইল থাকায় `fruit_inventory` ফোল্ডারটি একটি **package** হয়।
- `from .storage import ...`: শুরুর **ডট (.)** মানে “এই package এর ভিতরের storage.py থেকে”। একে **relative import** বলে।
- এখানে import করে রাখায় বাইরের ফাইল সরাসরি `from fruit_inventory import add_item` লিখতে পারে। এটাই package থেকে function **export** করা।
- `__all__` তালিকা বলে দেয় package থেকে কোন নামগুলো বাইরে ব্যবহারের জন্য দেওয়া হলো।

#### `fruit_inventory/storage.py` — CSV লেখা ও পড়া

```python
import csv
import os

FILE = "fruits.csv"
HEADER = ["Fruit", "Unit Price", "Quantity", "Total Price"]


def add_item(name, price, qty, file=FILE):
    """Save one fruit in the CSV file and return its total price."""
    new_file = not os.path.exists(file)
    total = price * qty
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow([name, price, qty, total])
    return total


def read_items(file=FILE):
    """Return all fruits as a list of dictionaries (empty list if no file yet)."""
    if not os.path.exists(file):
        return []
    with open(file) as f:
        return list(csv.DictReader(f))
```

- `add_item(name, price, qty, file=FILE)`: চারটি **parameter**। `file=FILE` হলো **default value**, না দিলে fruits.csv ধরে নেয়।
- function টি মোট দাম হিসাব করে, CSV তে লেখে এবং `return total` দিয়ে মোট দাম **ফেরত দেয়**। main.py সেই মান ছাপে।
- `read_items()`: ফাইল না থাকলে খালি list `[]` ফেরত দেয়, থাকলে প্রতিটি সারি dictionary হিসেবে একটি list এ দেয়। তাই ফল যোগের আগে সারাংশ চাইলেও error হয় না।
- `"""..."""` হলো **docstring**: function কী করে তার বর্ণনা। `help(add_item)` দিলে এটি দেখা যায়।

#### `fruit_inventory/report.py` — সারাংশ ছাপা

```python
def print_summary(items):
    """Print every fruit and the totals."""
    if not items:
        print("No fruit saved yet!")
        return
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
    for row in items:
        print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
        grand_total += float(row["Total Price"])
        total_qty += int(row["Quantity"])
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")
```

- `print_summary(items)` ফাইল খোলে না, শুধু তাকে দেওয়া list ছাপে। তাই ডাটা যেখান থেকেই আসুক (CSV, ডাটাবেস), এই function একই থাকে।
- `if not items:` খালি list মানে কোনো ফল নেই, তখন বার্তা দেখিয়ে `return`।

#### `main.py` — মেনু ও ইনপুট

```python
from fruit_inventory import add_item, read_items, print_summary


def take_item():
    """Take one fruit from the user and save it."""
    name = input("Fruit name: ").strip()
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
    total = add_item(name, price, qty)
    print("Saved:", name, "| Total =", total, "Tk")


if __name__ == "__main__":
    while True:
        print("\n1. Add fruit   2. Show summary   3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            take_item()
        elif choice == "2":
            print_summary(read_items())
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")
```

- `from fruit_inventory import add_item, read_items, print_summary`: package থেকে তিনটি function আনা (**import**)।
- `take_item()` শুধু ইনপুট নেয় ও ভুল ইনপুট সামলায়। সংরক্ষণের কাজ `add_item()` কে দিয়ে করায়।
- মেনুর 2 এ `print_summary(read_items())`: আগে read_items() ডাটা ফেরত দেয়, সেটিই print_summary() এর argument হয়।
- `if __name__ == "__main__":` ফাইলটি সরাসরি চালালে (`python main.py`) মেনু চলে। অন্য ফাইল এটিকে import করলে চলে না।

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### সমাধান ৩: Google Colab (`3_colab/Job1_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job1_Fruit_Inventory/3_colab/Job1_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

> এই জবে বাইরের কোনো package লাগে না (শুধু built-in module), তাই install এর cell নেই।

**📝 Cell 1: module import ও ফাইলের নাম**  
csv ও os module আনা এবং ফাইলের নাম ঠিক করা।

```python
import csv
import os

FILE = "fruits.csv"
```

**📝 Cell 2: function ১: add_item() তৈরি**  
একটি ফলের তথ্য নিয়ে CSV তে লেখার function। এই cell চালালে কিছু দেখাবে না, শুধু function তৈরি হবে।

```python
def add_item():
    name = input("Fruit name: ").strip()
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
    total = price * qty
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
        writer.writerow([name, price, qty, total])
    print("Saved:", name, "| Total =", total, "Tk")
```

**📝 Cell 3: function ২: show_summary() তৈরি**  
CSV পড়ে সারাংশ দেখানোর function। এটিও শুধু তৈরি হবে।

```python
def show_summary():
    if not os.path.exists(FILE):
        print("No fruit saved yet!")
        return
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
    with open(FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
            grand_total += float(row["Total Price"])
            total_qty += int(row["Quantity"])
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")
```

**📝 Cell 4: মেনু চালানো**  
1 দিলে ফল যোগ, 2 দিলে সারাংশ, 3 দিলে প্রোগ্রাম শেষ।

```python
while True:
    print("\n1. Add fruit   2. Show summary   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_item()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
```

> function তৈরির cell চালালে কিছু দেখায় না, এটাই স্বাভাবিক। শেষ cell এ মেনু আসবে: 1 দিয়ে ফল যোগ, 2 দিয়ে সারাংশ, 3 দিয়ে শেষ। fruits.csv বাম পাশের 📁 Files এ পাবেন।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `PermissionError` | `fruits.csv` Excel এ খোলা আছে। Excel বন্ধ করে আবার চালান। |
| প্রতি সারির পরে ফাঁকা লাইন | `open()` এ `newline=""` দেওয়া হয়নি। |
| সারাংশে `ValueError` | কেউ হাতে CSV এডিট করে ভুল মান রেখেছে। ফাইল মুছে আবার চালান। |
| শুরু থেকে নতুন করে চাই | `fruits.csv` ফাইলটি মুছে দিন। |

### বাড়তি কাজ (অনুশীলন)

1. নাম দিয়ে একটি ফল খুঁজে তার তথ্য দেখান।
2. সবচেয়ে দামি ফল (সবচেয়ে বেশি Unit Price) বের করুন।
3. মেনুতে নতুন অপশন যোগ করুন: `4. Search fruit` (নাম দিয়ে খুঁজে তথ্য দেখানো)।
4. একই ফল আবার দিলে নতুন সারি না করে পরিমাণ যোগ করুন।

### ভাইভা প্রশ্ন ও উত্তর

1. **CSV এর পূর্ণরূপ কী?** Comma Separated Values।
2. **`"a"` mode কেন ব্যবহার করা হয়েছে?** আগের রেকর্ড না মুছে নতুন রেকর্ড শেষে যোগ করার জন্য। `"w"` দিলে আগের সব মুছে যেত।
3. **`newline=""` কেন দেওয়া হয়?** Windows এ CSV এর প্রতি সারির পরে অতিরিক্ত ফাঁকা লাইন আসা ঠেকাতে।
4. **`with open()` এর সুবিধা কী?** ব্লক শেষে ফাইল নিজে থেকেই বন্ধ হয়, error হলেও।
5. **`DictReader` ও `reader` এর পার্থক্য কী?** `reader` প্রতিটি সারি list দেয় (নম্বর দিয়ে মান নিতে হয়)। `DictReader` dictionary দেয় (কলামের নাম দিয়ে মান নেওয়া যায়)।
6. **সারাংশ দেখানোর আগে `os.path.exists(FILE)` কেন যাচাই করা হয়?** ফল যোগের আগেই সারাংশ চাইলে ফাইল থাকে না, তখন `FileNotFoundError` এড়াতে।
7. **CSV থেকে পড়া মান যোগ করার আগে `float()` কেন লাগে?** CSV থেকে সব মান string হিসেবে আসে। string যোগ করলে জোড়া লাগে, গাণিতিক যোগ হয় না।
8. **`try-except ValueError` না থাকলে কী হতো?** সংখ্যার জায়গায় অক্ষর দিলে প্রোগ্রাম error দিয়ে বন্ধ হয়ে যেত।
9. **মেনু কেন `while True` লুপের ভিতরে?** যাতে প্রোগ্রাম বন্ধ না হয়ে বারবার কাজ করা যায়। Exit (3) দিলে `break` দিয়ে লুপ শেষ হয়।
10. **`break` ও `continue` এর পার্থক্য কী?** `break` লুপ পুরোপুরি শেষ করে। `continue` বর্তমান ঘুরের বাকি অংশ বাদ দিয়ে লুপের শুরুতে ফিরে যায়।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।

[⬆ সূচিতে ফিরুন](#সূচি)

---

## জব ২: CSV থেকে PDF Report

**কাজ:** মেনু-ভিত্তিক application: ছাত্রদের তথ্য ইনপুট নিয়ে students.csv তে রাখে, তারপর সেখান থেকে টেবিলসহ student_report.pdf বানায়। মেনু: 1 Add student, 2 Make PDF report, 3 Exit।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p2_pdf_report.py`](../Job2_PDF_Report/1_single_file/p2_pdf_report.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job2_PDF_Report/2_modular/main.py) + `report_tools/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job2_colab.ipynb`](../Job2_PDF_Report/3_colab/Job2_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** students.csv, student_report.pdf · **বিস্তারিত README:** [Job2_PDF_Report/README.md](../Job2_PDF_Report/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
fpdf2>=2.7.0
```

### সমাধান ১: Single file (`1_single_file/p2_pdf_report.py`)

```python
import csv
import os
from fpdf import FPDF

FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]


def add_student():
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow(row)
    print("Saved:", row[1])


def make_pdf():
    if not os.path.exists(FILE):
        print("No student saved yet!")
        return
    with open(FILE) as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]

    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Pabna Polytechnic Institute", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    widths = [28, 45, 25, 25, 20, 30, 35, 40]

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
    pdf.output("student_report.pdf")
    print("PDF created: student_report.pdf")


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

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p2_pdf_report.py
```

যা দেখা যাবে:

```text
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
Choose (1-3): 2
PDF created: student_report.pdf

1. Add student   2. Make PDF report   3. Exit
Choose (1-3): 3
Bye!
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

#### লাইন ১–৩: module আনা

```python
import csv
import os
from fpdf import FPDF
```

- **কী হচ্ছে:** `csv` (CSV লেখা-পড়া), `os` (ফাইল আছে কিনা যাচাই) আর `fpdf2` package থেকে `FPDF` class আনা হলো।
- **কেন `from ... import`:** পুরো module না এনে শুধু দরকারি class টি আনা হয়েছে। তাই কোডে `fpdf.FPDF()` না লিখে শুধু `FPDF()` লেখা যায়।
- **কেন `fpdf2`:** এটি ছোট, শুধু Python এ লেখা (বাইরের কোনো সফটওয়্যার লাগে না) এবং টেবিল-শিরোনাম আঁকা সহজ। তাই Windows, Linux ও Colab সব জায়গায় একইভাবে চলে।

#### লাইন ৫–৬: ফাইলের নাম ও কলামের নাম

```python
FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]
```

- **কী হচ্ছে:** CSV ফাইলের নাম আর ৮টি কলামের নাম একটি list এ রাখা হলো।
- **কেন `HEADER` list:** একই list দুই কাজে লাগে: CSV এর প্রথম সারি (header), আর ইনপুট নেওয়ার সময় প্রশ্ন (`Student_Id:`, `Name:` ...)। কলাম যোগ বা বদলাতে হলে শুধু এই এক লাইন বদলালেই হবে।

#### লাইন ৯–১২: একজন ছাত্রের তথ্য নেওয়া (লুপ দিয়ে)

```python
def add_student():
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
```

- **কী হচ্ছে:** `add_student` function। মেনুতে 1 দিলে চলে। খালি list `row` তৈরি করে `HEADER` এর প্রতিটি নামের জন্য একবার করে ইনপুট নেয় এবং `append()` দিয়ে list এ যোগ করে।
- **কেন লুপ:** ৮টি তথ্যের জন্য ৮ লাইন `input()` না লিখে এক লুপেই সব নেওয়া যায়। ইনপুটের ক্রম আর CSV কলামের ক্রম আপনা থেকেই মিলে যায়।
- **কেন সব string:** রোল ও ফোন নম্বরে কোনো হিসাব করা হবে না। সংখ্যা হিসেবে রাখলে ফোন নম্বরের শুরুর `0` হারিয়ে যেত।

#### লাইন ১৩–১৮: CSV ফাইলে যোগ করা

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

#### লাইন ১৯: সংরক্ষণের নিশ্চয়তা

```python
    print("Saved:", row[1])
```

- **কী হচ্ছে:** `row[1]` হলো list এর দ্বিতীয় উপাদান, অর্থাৎ ছাত্রের নাম (index 0 থেকে শুরু হয়)।

#### লাইন ২২–২৫: PDF function ও ফাইল আছে কিনা যাচাই

```python
def make_pdf():
    if not os.path.exists(FILE):
        print("No student saved yet!")
        return
```

- **কী হচ্ছে:** `make_pdf` function। মেনুতে 2 দিলে চলে। প্রথমেই দেখে নেয় `students.csv` আছে কিনা।
- **কেন যাচাই:** কোনো ছাত্র যোগ না করেই 2 চাপলে ফাইলটি থাকে না, তখন `open()` এ `FileNotFoundError` হতো। তাই বার্তা দেখিয়ে মেনুতে ফেরত যাওয়া হয়।

#### লাইন ২৬–২৯: CSV পড়া ও header-ডাটা আলাদা

```python
    with open(FILE) as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]
```

- **কী হচ্ছে:** `csv.reader(f)` প্রতিটি সারি list হিসেবে দেয়, `list()` দিয়ে সবগুলো একটি বড় list এ আনা হয়। `rows[0]` header, `rows[1:]` (slicing) বাকি সব ছাত্র।
- **কেন আলাদা:** PDF এ header সারি বোল্ড ও রঙিন হবে, ডাটা সারি সাধারণ। তাই দুটি আলাদাভাবে আঁকতে হবে।

#### লাইন ৩১–৩২: PDF object ও পাতা তৈরি

```python
    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
```

- **কী হচ্ছে:** `FPDF` class থেকে একটি object (`pdf`) তৈরি হলো (অধ্যায় ৪: OOP)। `orientation="L"` মানে Landscape (আড়াআড়ি) পাতা, `format="A4"` কাগজের মাপ। `add_page()` প্রথম পাতা যোগ করে।
- **কেন Landscape:** ৮টি কলাম আছে। খাড়া (Portrait) A4 এ (২১০ mm চওড়া) সব কলাম ধরবে না। আড়াআড়ি A4 প্রায় ২৯৭ mm চওড়া।
- **কেন `add_page()` লাগে:** পাতা না থাকলে কিছু লেখা যায় না, error দেবে।

#### লাইন ৩৩–৩৪: বড় শিরোনাম

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

#### লাইন ৩৫–৩৭: উপ-শিরোনাম ও ফাঁকা জায়গা

```python
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
```

- **কী হচ্ছে:** সাধারণ (বোল্ড নয়) ১২ সাইজে উপ-শিরোনাম লেখা হলো। `ln(5)` ৫ mm নিচে নামায়।
- **কেন `ln(5)`:** শিরোনাম ও টেবিলের মাঝে একটু ফাঁকা রাখার জন্য, দেখতে পরিষ্কার লাগে।

#### লাইন ৩৯: কলামের প্রস্থ

```python
    widths = [28, 45, 25, 25, 20, 30, 35, 40]
```

- **কী হচ্ছে:** ৮টি কলামের প্রতিটির প্রস্থ (মিলিমিটারে) একটি list এ রাখা হলো। Name ও Phone এর লেখা লম্বা, তাই সেগুলো চওড়া।
- **কেন list এ:** লুপে `widths[i]` দিয়ে i নম্বর কলামের প্রস্থ সহজে পাওয়া যায়। মোট ২৪৮ mm, যা Landscape A4 এর লেখার জায়গার মধ্যে ধরে।

#### লাইন ৪১–৪৫: header সারি আঁকা

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

#### লাইন ৪৭–৫১: ডাটা সারি আঁকা

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

#### লাইন ৫৩–৫৪: মোট ছাত্র সংখ্যা

```python
    pdf.ln(4)
    pdf.cell(0, 8, "Total students: " + str(len(data)))
```

- **কী হচ্ছে:** একটু ফাঁকা রেখে মোট ছাত্র সংখ্যা লেখা হয়।
- **কেন `str()`:** `len(data)` একটি সংখ্যা (3)। string এর সাথে সংখ্যা `+` দিয়ে জোড়া যায় না (`TypeError`), তাই আগে string বানাতে হয়।

#### লাইন ৫৫–৫৬: PDF সংরক্ষণ

```python
    pdf.output("student_report.pdf")
    print("PDF created: student_report.pdf")
```

- **কী হচ্ছে:** এতক্ষণ সব কিছু মেমোরিতে আঁকা হচ্ছিল। `output()` সেটিকে ফাইল হিসেবে ডিস্কে লেখে।
- **কেন জরুরি:** `output()` না দিলে কোনো PDF ফাইল তৈরি হবে না।

---

#### লাইন ৫৯–৭০: মেনু: প্রোগ্রাম চালু রাখা ও পছন্দ অনুযায়ী কাজ

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

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** **csv_tools.py** CSV এ সারি যোগ ও পড়ার কাজ করে, **pdf_tools.py** PDF বানায়, আর **main.py** মেনু দেখায়, ছাত্রের তথ্য নেয় ও দুটিকে ব্যবহার করে। make_pdf() এ শিরোনাম ও ফাইলের নাম parameter হিসেবে দেওয়া যায়, তাই একই function দিয়ে অন্য যেকোনো রিপোর্টও বানানো যাবে।

```text
2_modular/
├── main.py
└── report_tools/
    ├── __init__.py
    ├── csv_tools.py
    └── pdf_tools.py
```

#### `report_tools/__init__.py` — package এর দরজা

```python
"""report_tools package: save/read CSV rows and make a PDF table report."""

from .csv_tools import save_row, read_csv
from .pdf_tools import make_pdf

__all__ = ["save_row", "read_csv", "make_pdf"]
```

- csv_tools ও pdf_tools এর function গুলো relative import (`.`) দিয়ে এনে বাইরে export করে।
- এখন `from report_tools import save_row, read_csv, make_pdf` লেখা যায়।

#### `report_tools/csv_tools.py` — CSV এ সারি যোগ ও পড়া

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

#### `report_tools/pdf_tools.py` — PDF তৈরি

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

#### `main.py` — মেনু, ইনপুট ও রিপোর্ট

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

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### সমাধান ৩: Google Colab (`3_colab/Job2_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job2_PDF_Report/3_colab/Job2_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

**📝 Cell 1: package install**

```python
!pip install fpdf2
```

**📝 Cell 2: module import ও কলামের নাম**  
csv, os ও FPDF আনা; ফাইলের নাম ও ৮টি কলামের নাম ঠিক করা।

```python
import csv
import os
from fpdf import FPDF

FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]
```

**📝 Cell 3: function ১: add_student() তৈরি**  
একজন ছাত্রের ৮টি তথ্য নিয়ে CSV তে লেখার function। শুধু তৈরি হবে।

```python
def add_student():
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow(row)
    print("Saved:", row[1])
```

**📝 Cell 4: function ২: make_pdf() তৈরি**  
CSV পড়ে টেবিলসহ PDF বানানোর function। শুধু তৈরি হবে।

```python
def make_pdf():
    if not os.path.exists(FILE):
        print("No student saved yet!")
        return
    with open(FILE) as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]

    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Pabna Polytechnic Institute", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    widths = [28, 45, 25, 25, 20, 30, 35, 40]

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
    pdf.output("student_report.pdf")
    print("PDF created: student_report.pdf")
```

**📝 Cell 5: মেনু চালানো**  
1 দিলে ছাত্র যোগ, 2 দিলে PDF তৈরি, 3 দিলে শেষ।

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

**📝 Cell 6: PDF ডাউনলোড**  
মেনুতে 2 দিয়ে PDF তৈরির পরে এই cell চালালে student_report.pdf কম্পিউটারে নামবে।

```python
from google.colab import files
files.download("student_report.pdf")
```

> মেনুতে আগে 1 দিয়ে ছাত্র যোগ করুন, তারপর 2 দিয়ে PDF বানান, 3 দিয়ে মেনু থেকে বের হন। এরপর শেষ cell চালালে student_report.pdf কম্পিউটারে ডাউনলোড হবে।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ModuleNotFoundError: No module named 'fpdf'` | environment activate করা নেই বা package install হয়নি। activate করে `pip install -r requirements.txt` দিন। |
| `TypeError: ... unexpected keyword argument 'new_x'` | পুরোনো `fpdf` package install হয়েছে। `pip uninstall fpdf` তারপর `pip install -r requirements.txt`। |
| `PermissionError` | PDF বা CSV কোনো সফটওয়্যারে খোলা আছে। বন্ধ করে আবার চালান। |
| বাংলা নাম `?` বা error দেখায় | Helvetica তে বাংলা অক্ষর নেই। Nikosh/Kalpurush এর `.ttf` ফাইল ফোল্ডারে রেখে `pdf.add_font("Nikosh", "", "Nikosh.ttf")` ও `pdf.set_font("Nikosh", "", 10)` দিন। যুক্তাক্ষর ঠিকভাবে দেখাতে `pdf.set_text_shaping(True)` লাগতে পারে, যার জন্য `uharfbuzz` package install করতে হয়। |

### বাড়তি কাজ (অনুশীলন)

1. মেনুতে `4. Show all students` যোগ করুন, যা CSV এর সব ছাত্র স্ক্রিনে দেখাবে।
2. পাতার নিচে তারিখ ও "Signature" লেখা যোগ করুন।
3. Shift অনুযায়ী আলাদা দুটি টেবিল বানান।

### ভাইভা প্রশ্ন ও উত্তর

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

[⬆ সূচিতে ফিরুন](#সূচি)

---

## জব ৩: QR Code ও Barcode

**কাজ:** ছাত্রের ID ও নাম দিয়ে QR code ও barcode ছবি বানায়, তারপর ছবি থেকে পড়ে দেখায়।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p3_qr_barcode.py`](../Job3_QR_Barcode/1_single_file/p3_qr_barcode.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job3_QR_Barcode/2_modular/main.py) + `codes/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job3_colab.ipynb`](../Job3_QR_Barcode/3_colab/Job3_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** student_qr.png, student_barcode.png · **বিস্তারিত README:** [Job3_QR_Barcode/README.md](../Job3_QR_Barcode/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
qrcode[pil]>=7.4
python-barcode>=0.15.1
pyzbar>=0.1.9
Pillow>=9.0
```

> Windows এ pyzbar এ DLL error এলে Microsoft Visual C++ Redistributable 2013 install করুন। Colab এ আগে `!apt-get install -y libzbar0` চালাতে হবে।

### সমাধান ১: Single file (`1_single_file/p3_qr_barcode.py`)

```python
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
```

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p3_qr_barcode.py
```

যা দেখা যাবে:

```text
Enter Student ID: 701234
Enter Student Name: Rahim Uddin
QR code saved: student_qr.png
Barcode saved: student_barcode.png
Decoded from student_qr.png -> QRCODE : 701234 - Rahim Uddin
Decoded from student_barcode.png -> CODE128 : 701234
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

#### লাইন ১–৫: module আনা

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

#### লাইন ৮–১০: ইনপুট নেওয়া ও জোড়া লাগানো

```python
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
data = student_id + " - " + name
```

- **কী হচ্ছে:** ID ও নাম নেওয়া হলো। `+` দিয়ে দুটি string জুড়ে একটি লেখা বানানো হলো, যেমন `"701234 - Rahim Uddin"`।
- **কেন জোড়া:** QR code এ অনেক তথ্য রাখা যায়, তাই ID ও নাম দুটোই একসাথে রাখা হলো। মাঝে `" - "` দেওয়ায় পড়ার সময় আলাদা করে বোঝা যায়।
- **কেন `int()` করা হয়নি:** ID দিয়ে হিসাব হবে না, আর কোড বানাতে string ই লাগে।

#### লাইন ১৩–১৫: QR code তৈরি ও সংরক্ষণ

```python
qr_img = qrcode.make(data)
qr_img.save("student_qr.png")
print("QR code saved: student_qr.png")
```

- **`qrcode.make(data)`:** লেখাটিকে QR code এ রূপান্তর করে একটি ছবি object দেয়। size ও error correction নিজে থেকে ঠিক করে নেয়।
- **কেন `make()`:** এটি সবচেয়ে সহজ উপায়, এক লাইনে QR বানায়। রং বা সাইজ বদলাতে চাইলে `qrcode.QRCode()` class ব্যবহার করা যায় (বাড়তি কাজ দেখুন)।
- **`.save("student_qr.png")`:** ছবিটি PNG ফাইলে লেখে। এটি না দিলে ছবি শুধু মেমোরিতে থাকত।

#### লাইন ১৮–১৯: barcode তৈরি ও সংরক্ষণ

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

#### লাইন ২২–২৫: দুটি ছবি থেকে decode

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

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** **generator.py** কোড ও ছবি তৈরি করে, **reader.py** ছবি থেকে কোড পড়ে। main.py জানেই না কোন লাইব্রেরি দিয়ে QR বানানো হচ্ছে। পরে লাইব্রেরি বদলালে শুধু generator.py বদলাতে হবে।

```text
2_modular/
├── main.py
└── codes/
    ├── __init__.py
    ├── generator.py
    └── reader.py
```

#### `codes/__init__.py` — package এর দরজা

```python
"""codes package: create QR codes and barcodes, and read them back."""

from .generator import make_qr, make_barcode
from .reader import read_codes

__all__ = ["make_qr", "make_barcode", "read_codes"]
```

- `make_qr`, `make_barcode`, `read_codes` তিনটি function export করে।

#### `codes/generator.py` — QR ও barcode তৈরি

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

#### `codes/reader.py` — ছবি থেকে পড়া

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

#### `main.py` — ইনপুট ও চালানো

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

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### সমাধান ৩: Google Colab (`3_colab/Job3_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job3_QR_Barcode/3_colab/Job3_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

**📝 Cell 1: package install**

```python
!apt-get update -qq
!apt-get install -y libzbar0
!pip install qrcode[pil] python-barcode pyzbar Pillow
```

**📝 Cell 2: module import**  
QR, barcode, decode ও ছবির module আনা।

```python
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image
```

**📝 Cell 3: ধাপ ১: ID ও নাম ইনপুট**  
ID ও নাম চাইবে।

```python
# Step 1: take student id and name
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
data = student_id + " - " + name
```

**📝 Cell 4: ধাপ ২: QR code তৈরি**  
student_qr.png তৈরি হবে।

```python
# Step 2: create QR code
qr_img = qrcode.make(data)
qr_img.save("student_qr.png")
print("QR code saved: student_qr.png")
```

**📝 Cell 5: ধাপ ৩: Barcode তৈরি**  
student_barcode.png তৈরি হবে।

```python
# Step 3: create barcode (Code 128)
barcode_file = Code128(student_id, writer=ImageWriter()).save("student_barcode")
print("Barcode saved:", barcode_file)
```

**📝 Cell 6: ধাপ ৪: দুটি ছবি decode**  
ছবি থেকে পড়া তথ্য দেখাবে।

```python
# Step 4: decode both images
for file in ["student_qr.png", barcode_file]:
    results = decode(Image.open(file))
    for r in results:
        print("Decoded from", file, "->", r.type, ":", r.data.decode("utf-8"))
```

**📝 Cell 7: তৈরি হওয়া ছবি দেখা**

```python
from IPython.display import Image as Show, display
display(Show("student_qr.png", width=200))
display(Show("student_barcode.png", width=350))
```

> Colab এ pyzbar এর জন্য সিস্টেমে libzbar0 লাগে। তাই প্রথম cell এ আগে `apt-get update`, তারপর install।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ImportError: Unable to find zbar shared library` | ZBar সিস্টেমে নেই। Linux এ `sudo apt install libzbar0`, Mac এ `brew install zbar`, Colab এ `!apt-get update -qq` তারপর `!apt-get install -y libzbar0`। |
| Windows এ `FileNotFoundError` / DLL error (pyzbar) | Visual C++ Redistributable 2013 install করুন। |
| `ModuleNotFoundError: No module named 'barcode'` | `python-barcode` install হয়নি (নাম `barcode` নয়)। `pip install -r requirements.txt` দিন। |
| decode এ কিছুই ছাপে না | ছবি অস্পষ্ট বা খুব ছোট। barcode এ শুধু ছোট ID দিন। |

### বাড়তি কাজ (অনুশীলন)

1. `qrcode.QRCode(box_size=10, border=4)` ও `make_image(fill_color="darkblue", back_color="white")` দিয়ে রঙিন QR বানান।
2. একাধিক ছাত্রের ID একটি লুপে নিয়ে প্রত্যেকের জন্য আলাদা নামে QR বানান।
3. মোবাইলে তোলা একটি barcode এর ছবি decode করে দেখুন।

### ভাইভা প্রশ্ন ও উত্তর

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

[⬆ সূচিতে ফিরুন](#সূচি)

---

## জব ৪: Web Scraping

**কাজ:** books.toscrape.com থেকে বইয়ের নাম, দাম, রেটিং ও স্টক নিয়ে books.csv তে রাখে। ইন্টারনেট লাগবে।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p4_scraping.py`](../Job4_Web_Scraping/1_single_file/p4_scraping.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job4_Web_Scraping/2_modular/main.py) + `scraper/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job4_colab.ipynb`](../Job4_Web_Scraping/3_colab/Job4_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** books.csv · **বিস্তারিত README:** [Job4_Web_Scraping/README.md](../Job4_Web_Scraping/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
requests>=2.28
beautifulsoup4>=4.11
```

### সমাধান ১: Single file (`1_single_file/p4_scraping.py`)

```python
import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

# Step 1: get HTML source code
response = requests.get(url, timeout=10)
response.encoding = "utf-8"
print("Status code:", response.status_code)

# Step 2: parse HTML
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print("Books found on this page:", len(books))

# Step 3: extract data
rows = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    stock = book.find("p", class_="instock availability").get_text(strip=True)
    rows.append([title, price, rating, stock])

for r in rows[:4]:
    print(r)

# Step 4: save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Book Name", "Price", "Rating", "Availability"])
    writer.writerows(rows)
print("Saved", len(rows), "books to books.csv")
```

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p4_scraping.py
```

যা দেখা যাবে:

```text
Status code: 200
Books found on this page: 20
['A Light in the Attic', '£51.77', 'Three', 'In stock']
['Tipping the Velvet', '£53.74', 'One', 'In stock']
['Soumission', '£50.10', 'One', 'In stock']
['Sharp Objects', '£47.82', 'Four', 'In stock']
Saved 20 books to books.csv
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

#### লাইন ১–৩: module আনা

```python
import csv
import requests
from bs4 import BeautifulSoup
```

- **`csv`:** শেষে ফলাফল CSV তে লেখার জন্য (built-in)।
- **`requests`:** ইন্টারনেট থেকে ওয়েবপেজ আনার জন্য। এটি ব্রাউজারের মতো সার্ভারে request পাঠায় এবং HTML ফেরত আনে। Python এর built-in `urllib` এর চেয়ে এটি অনেক সহজ।
- **`BeautifulSoup`:** HTML লেখাকে খোঁজার উপযোগী গঠনে (tree) রূপান্তর করে, যাতে ট্যাগ ও class দিয়ে তথ্য খুঁজে নেওয়া যায়। package এর নাম `beautifulsoup4`, কিন্তু import এর নাম `bs4`।
- **দুটি লাইব্রেরি কেন:** `requests` শুধু HTML **আনে**। `BeautifulSoup` সেই HTML থেকে তথ্য **খোঁজে**। কাজ ভাগ করা আছে।

#### লাইন ৫: ওয়েবসাইটের ঠিকানা

```python
url = "https://books.toscrape.com/"
```

- **কী হচ্ছে:** যে পেজ থেকে তথ্য নেওয়া হবে তার URL একটি ভেরিয়েবলে রাখা হলো, যাতে পরে সহজে বদলানো যায়।

#### লাইন ৮: HTML সোর্স আনা

```python
response = requests.get(url, timeout=10)
```

- **কী হচ্ছে:** `requests.get()` সার্ভারে একটি **GET request** পাঠায় (ব্রাউজারে ঠিকানা লিখে Enter চাপার মতো)। সার্ভারের উত্তর `response` object এ আসে।
- **কেন `timeout=10`:** সার্ভার উত্তর না দিলে প্রোগ্রাম চিরকাল অপেক্ষা করবে না, ১০ সেকেন্ড পরে error দিয়ে থামবে।

#### লাইন ৯: encoding ঠিক করা

```python
response.encoding = "utf-8"
```

- **কী হচ্ছে:** পেজের লেখা UTF-8 হিসেবে পড়তে বলা হলো।
- **কেন:** এই সাইটের সার্ভার encoding ঠিকভাবে জানায় না। তখন requests ভুল encoding ধরে নেয় এবং `£` চিহ্ন ভেঙে `Â£` দেখায়। UTF-8 বলে দিলে সঠিক দেখায়।

#### লাইন ১০: status code দেখা

```python
print("Status code:", response.status_code)
```

- **কী হচ্ছে:** সার্ভারের উত্তরের ধরন বোঝার সংখ্যা ছাপা হয়।
- **কেন:** `200` মানে সফল। `404` মানে পেজ নেই, `403` মানে প্রবেশ নিষেধ, `500` মানে সার্ভারের সমস্যা। ফলাফল খালি এলে প্রথমেই এটি দেখতে হয়।

#### লাইন ১৩: HTML পার্স করা

```python
soup = BeautifulSoup(response.text, "html.parser")
```

- **কী হচ্ছে:** `response.text` হলো পুরো HTML একটি লম্বা string আকারে। BeautifulSoup সেটিকে ট্যাগের গাছে (tree) সাজিয়ে `soup` object বানায়।
- **কেন `"html.parser"`:** এটি Python এর সাথে আসা parser, আলাদা install লাগে না। (`lxml` আরও দ্রুত, কিন্তু আলাদা install লাগে।)

#### লাইন ১৪–১৫: সব বই খুঁজে বের করা

```python
books = soup.find_all("article", class_="product_pod")
print("Books found on this page:", len(books))
```

- **`find_all(ট্যাগ, class_=...)`:** যে সব `<article>` ট্যাগের class `product_pod`, সবগুলো একটি list হিসেবে দেয়। প্রতিটি উপাদান একটি বইয়ের পুরো ব্লক।
- **কেন `class_` (শেষে আন্ডারস্কোর):** `class` Python এর সংরক্ষিত শব্দ (keyword), class তৈরিতে ব্যবহৃত হয়। তাই BeautifulSoup `class_` লিখতে বলে।
- **কেন `len(books)` ছাপা:** কতগুলো বই পাওয়া গেল তা দেখে নিশ্চিত হওয়া যায় যে খোঁজা ঠিক কাজ করছে। এই সাইটে প্রতি পেজে ২০টি বই।

#### লাইন ১৮–২৪: প্রতিটি বই থেকে তথ্য বের করা

```python
rows = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    stock = book.find("p", class_="instock availability").get_text(strip=True)
    rows.append([title, price, rating, stock])
```

- **`rows = []`:** ফলাফল জমানোর জন্য একটি খালি list।
- **`for book in books`:** প্রতিটি বইয়ের ব্লক একটি একটি করে নেওয়া হয়। `book` এর ভিতরে খুঁজলে শুধু সেই বইয়ের তথ্যই পাওয়া যায়।
- **`book.h3.a["title"]`:**
  - `book.h3` ব্লকের ভিতরের প্রথম `<h3>` দেয়, আর `.a` তার ভিতরের `<a>` দেয়।
  - `["title"]` দিয়ে `<a>` ট্যাগের `title` attribute এর মান নেওয়া হয়।
  - **কেন `.text` নয়:** `<a>` এর লেখা ছোট করে কাটা ("A Light in the ..."), অথচ `title` এ পূর্ণ নাম আছে।
- **`find("p", class_="price_color").text`:** `find()` প্রথম মিল পাওয়া **একটি** ট্যাগ দেয় (`find_all` এর মতো list নয়)। `.text` ট্যাগের ভিতরের লেখা দেয় (`£51.77`)।
- **`["class"][1]`:** একটি ট্যাগের class একাধিক হতে পারে, তাই BeautifulSoup class কে **list** হিসেবে দেয়: `["star-rating", "Three"]`। `[1]` দিয়ে দ্বিতীয় উপাদান `"Three"`, অর্থাৎ রেটিং পাওয়া যায়।
- **`get_text(strip=True)`:** স্টকের লেখার চারপাশে অনেক ফাঁকা জায়গা ও নতুন লাইন আছে। `strip=True` সেগুলো বাদ দিয়ে শুধু `"In stock"` দেয়।
- **`rows.append([...])`:** একটি বইয়ের চারটি তথ্য একটি list করে `rows` এ যোগ হয়। শেষে `rows` হবে list এর list, যা সরাসরি CSV তে লেখা যায়।

#### লাইন ২৬–২৭: প্রথম ৪টি দেখানো

```python
for r in rows[:4]:
    print(r)
```

- **কী হচ্ছে:** `rows[:4]` slicing, শুধু প্রথম ৪টি বই (index 0 থেকে 3)।
- **কেন সব নয়:** ২০টি ছাপলে স্ক্রিন ভরে যায়। কয়েকটি দেখে নিশ্চিত হওয়াই যথেষ্ট, সব তথ্য CSV তে যাবে।

#### লাইন ৩০–৩৪: CSV ফাইলে সংরক্ষণ

```python
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Book Name", "Price", "Rating", "Availability"])
    writer.writerows(rows)
print("Saved", len(rows), "books to books.csv")
```

- **`"w"` mode:** প্রতিবার চালালে নতুন করে ফাইল লেখে, পুরোনো ফলাফল মুছে যায়। scraping এ সাধারণত সর্বশেষ তথ্যই চাই।
- **কেন `encoding="utf-8"`:** `£` চিহ্ন বা অন্য ভাষার অক্ষর থাকলে Windows এর ডিফল্ট encoding এ `UnicodeEncodeError` হতে পারে। UTF-8 সব অক্ষর ধরে।
- **`writerow` তারপর `writerows`:** প্রথমে header সারি একটি, তারপর সব বইয়ের সারি একবারে।
- শেষ লাইন জানায় মোট কতটি বই সংরক্ষিত হলো।

---

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** scraping এর তিনটি ধাপ তিনটি module এ: **fetch.py** পেজ আনে, **parser.py** তথ্য খোঁজে, **storage.py** CSV তে রাখে। সাইটের গঠন বদলালে শুধু parser.py বদলাতে হবে।

```text
2_modular/
├── main.py
└── scraper/
    ├── __init__.py
    ├── fetch.py
    ├── parser.py
    └── storage.py
```

#### `scraper/__init__.py` — package এর দরজা

```python
"""scraper package: download a web page, find the books and save them to CSV."""

from .fetch import get_html
from .parser import parse_books
from .storage import save_csv

__all__ = ["get_html", "parse_books", "save_csv"]
```

- তিনটি module এর function export করে: `get_html`, `parse_books`, `save_csv`।

#### `scraper/fetch.py` — পেজ আনা

```python
import requests


def get_html(url):
    """Download a web page and return (status_code, html_text)."""
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8"
    return response.status_code, response.text
```

- `get_html(url)` দুটি মান ফেরত দেয়: `(status_code, html_text)`। main.py দুটিই ব্যবহার করে।

#### `scraper/parser.py` — HTML থেকে বইয়ের তথ্য

```python
from bs4 import BeautifulSoup


def parse_books(html):
    """Find every book in the HTML and return a list of [title, price, rating, stock]."""
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        stock = book.find("p", class_="instock availability").get_text(strip=True)
        rows.append([title, price, rating, stock])
    return rows
```

- `parse_books(html)` HTML লেখা নেয়, তথ্যের list ফেরত দেয়। এটি ইন্টারনেট ব্যবহার করে না, তাই সেভ করা HTML দিয়েও পরীক্ষা করা যায়।
- ভিতরের লুপ single file এর Step 3 এর মতোই।

#### `scraper/storage.py` — CSV তে সংরক্ষণ

```python
import csv

HEADER = ["Book Name", "Price", "Rating", "Availability"]


def save_csv(rows, filename):
    """Save the book rows (with a header) into a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(rows)
```

- `HEADER` module এর ধ্রুবক। `save_csv(rows, filename)` header ও সব সারি লেখে।

#### `main.py` — ধাপগুলো ক্রমানুসারে চালানো

```python
from scraper import get_html, parse_books, save_csv

URL = "https://books.toscrape.com/"

if __name__ == "__main__":
    status, html = get_html(URL)
    print("Status code:", status)

    rows = parse_books(html)
    print("Books found on this page:", len(rows))
    for r in rows[:4]:
        print(r)

    save_csv(rows, "books.csv")
    print("Saved", len(rows), "books to books.csv")
```

- `status, html = get_html(URL)` → `rows = parse_books(html)` → `save_csv(rows, ...)`: এক function এর ফলাফল পরের function এর ইনপুট।

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### সমাধান ৩: Google Colab (`3_colab/Job4_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job4_Web_Scraping/3_colab/Job4_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

**📝 Cell 1: package install**

```python
!pip install requests beautifulsoup4
```

**📝 Cell 2: module import ও URL**  
requests, BeautifulSoup ও csv আনা।

```python
import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
```

**📝 Cell 3: ধাপ ১: HTML সোর্স আনা**  
Status code 200 এলে সফল।

```python
# Step 1: get HTML source code
response = requests.get(url, timeout=10)
response.encoding = "utf-8"
print("Status code:", response.status_code)
```

**📝 Cell 4: ধাপ ২: HTML পার্স করে বই খোঁজা**  
কতগুলো বই পাওয়া গেল দেখাবে।

```python
# Step 2: parse HTML
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print("Books found on this page:", len(books))
```

**📝 Cell 5: ধাপ ৩: প্রতিটি বই থেকে তথ্য বের করা**  
rows list এ জমা হবে।

```python
# Step 3: extract data
rows = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    stock = book.find("p", class_="instock availability").get_text(strip=True)
    rows.append([title, price, rating, stock])
```

**📝 Cell 6: প্রথম ৪টি বই দেখা**

```python
for r in rows[:4]:
    print(r)
```

**📝 Cell 7: ধাপ ৪: CSV তে সংরক্ষণ**  
books.csv তৈরি হবে।

```python
# Step 4: save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Book Name", "Price", "Rating", "Availability"])
    writer.writerows(rows)
print("Saved", len(rows), "books to books.csv")
```

**📝 Cell 8: books.csv দেখা**

```python
!head -n 6 books.csv
```

> Colab এ ইন্টারনেট সবসময় থাকে।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ConnectionError` | ইন্টারনেট নেই বা সাইট বন্ধ। সংযোগ দেখুন। |
| `ReadTimeout` | সার্ভার ১০ সেকেন্ডে উত্তর দেয়নি। আবার চালান। |
| `Books found on this page: 0` | tag বা class এর নাম ভুল, বা সাইটের গঠন বদলেছে। Inspect করে মিলিয়ে নিন। |
| `'NoneType' object is not subscriptable` বা `has no attribute` | `find()` কিছু পায়নি এবং `None` দিয়েছে। class এর বানান মিলিয়ে নিন। |
| দামে `Â£` দেখায় | `response.encoding = "utf-8"` লাইনটি বাদ পড়েছে। |

### বাড়তি কাজ (অনুশীলন)

1. সব ৫০টি পেজ থেকে মোট ১০০০ বই সংগ্রহ করুন। পেজের ঠিকানা `https://books.toscrape.com/catalogue/page-2.html` এভাবে বদলায়। লুপে `page-1` থেকে `page-50` পর্যন্ত চালান, এবং প্রতি request এর মাঝে `time.sleep(1)` দিন।
2. দাম থেকে `£` বাদ দিয়ে `float` বানিয়ে সবচেয়ে সস্তা ৫টি বই দেখান।
3. রেটিং `"Three"` কে সংখ্যা `3` এ রূপান্তর করুন (dictionary ব্যবহার করে)।

### ভাইভা প্রশ্ন ও উত্তর

1. **Web scraping কী?** প্রোগ্রাম দিয়ে ওয়েবপেজের HTML থেকে প্রয়োজনীয় তথ্য স্বয়ংক্রিয়ভাবে বের করা।
2. **requests ও BeautifulSoup এর কাজের পার্থক্য কী?** requests সার্ভার থেকে HTML আনে। BeautifulSoup সেই HTML থেকে ট্যাগ খুঁজে তথ্য বের করে।
3. **Status code 200 ও 404 মানে কী?** 200 মানে সফল, 404 মানে পেজ পাওয়া যায়নি।
4. **`class_` এ আন্ডারস্কোর কেন?** `class` Python এর সংরক্ষিত শব্দ, তাই সরাসরি ব্যবহার করা যায় না।
5. **`find()` ও `find_all()` এর পার্থক্য কী?** `find()` প্রথম মিলটি দেয় (না পেলে `None`)। `find_all()` সব মিল একটি list এ দেয়।
6. **বইয়ের নাম `.text` দিয়ে না নিয়ে `["title"]` দিয়ে কেন নেওয়া হলো?** লিংকের লেখা কাটা থাকে, পূর্ণ নাম `title` attribute এ আছে।
7. **`timeout` কেন দেওয়া হয়?** সার্ভার উত্তর না দিলে প্রোগ্রাম যেন অনির্দিষ্টকাল অপেক্ষা না করে।
8. **Scraping এর নৈতিক নিয়ম কী?** robots.txt ও সাইটের শর্ত মানা, অতিরিক্ত request না পাঠানো, ব্যক্তিগত তথ্য সংগ্রহ না করা।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।

[⬆ সূচিতে ফিরুন](#সূচি)

---

## জব ৫: Weather Report (API)

**কাজ:** শহরের নাম দিলে OpenWeather API থেকে আবহাওয়া এনে দেখায়। ইন্টারনেট ও API key লাগবে।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p5_weather.py`](../Job5_Weather_Report/1_single_file/p5_weather.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job5_Weather_Report/2_modular/main.py) + `weather/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job5_colab.ipynb`](../Job5_Weather_Report/3_colab/Job5_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** (কোনো ফাইল নয়, স্ক্রিনে রিপোর্ট) · **বিস্তারিত README:** [Job5_Weather_Report/README.md](../Job5_Weather_Report/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
requests>=2.28
```

> openweathermap.org এ ফ্রি একাউন্ট খুলে **My API keys** থেকে key কপি করুন, এবং কোডের `your_api_key_here` এর জায়গায় বসান। নতুন key চালু হতে ঘণ্টা দুয়েক পর্যন্ত লাগতে পারে। আবহাওয়ার সংখ্যাগুলো চালানোর সময় অনুযায়ী বদলাবে।

### সমাধান ১: Single file (`1_single_file/p5_weather.py`)

```python
import requests

API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 1: take location from the user
city = input("Enter city name: ")

# Step 2: call the Open Weather API
params = {"q": city, "appid": API_KEY, "units": "metric"}
try:
    response = requests.get(URL, params=params, timeout=10)
except requests.exceptions.RequestException:
    print("No internet connection!")
    raise SystemExit

data = response.json()

# Step 3: print basic weather data
if response.status_code == 200:
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
else:
    print("Error:", data.get("message"))
```

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p5_weather.py
```

যা দেখা যাবে:

```text
Enter city name: Dhaka
----- Weather Report -----
City        : Dhaka , BD
Temperature : 26.99 °C
Feels like  : 28.5 °C
Humidity    : 65 %
Condition   : haze
Wind speed  : 2.06 m/s
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

#### লাইন ১: module আনা

```python
import requests
```

- **কেন `requests`:** API ও ইন্টারনেটে HTTP request পাঠানোর জন্য। এটি JSON উত্তরকে সরাসরি dictionary তে রূপান্তর করার সুবিধাও দেয় (`.json()`)।

#### লাইন ৩–৪: API key ও ঠিকানা

```python
API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"
```

- **`API_KEY`:** OpenWeather আমাদের চেনে এই key দিয়ে। key ছাড়া বা ভুল key দিলে সার্ভার ডাটা দেয় না (401 error)।
- **`URL`:** API এর **endpoint**, অর্থাৎ যে নির্দিষ্ট ঠিকানায় "বর্তমান আবহাওয়া" চাওয়া হয়। `2.5` API এর version।
- **কেন বড় হাতের নাম:** এগুলো ধ্রুবক (constant), প্রোগ্রাম চলার সময় বদলায় না।

#### লাইন ৭: শহরের নাম ইনপুট

```python
city = input("Enter city name: ")
```

- **কী হচ্ছে:** ব্যবহারকারী শহরের নাম ইংরেজিতে দেবে, যেমন `Dhaka`, `Pabna`, `London`।

#### লাইন ১০: request এর parameter

```python
params = {"q": city, "appid": API_KEY, "units": "metric"}
```

- **কী হচ্ছে:** API কে যা জানাতে হবে তা একটি dictionary তে রাখা হলো।
  - `q` (query) = শহরের নাম।
  - `appid` = API key।
  - `units` = এককের ধরন।
- **কেন `"units": "metric"`:** না দিলে তাপমাত্রা **Kelvin** এ আসে (যেমন 300.14)। `metric` দিলে **সেলসিয়াস** (°C) ও বাতাসের গতি m/s এ আসে।
- **কেন dictionary (URL হাতে লিখে নয়):** `requests` নিজেই এগুলো দিয়ে সঠিক URL বানায়: `...weather?q=Dhaka&appid=KEY&units=metric`। শহরের নামে স্পেস থাকলে (যেমন `New York`) সেটিও ঠিকভাবে encode করে (`New%20York`)। হাতে লিখলে এসব ভুলের সম্ভাবনা থাকে।

#### লাইন ১১–১৫: API তে request পাঠানো ও ইন্টারনেট সমস্যা সামলানো

```python
try:
    response = requests.get(URL, params=params, timeout=10)
except requests.exceptions.RequestException:
    print("No internet connection!")
    raise SystemExit
```

- **`requests.get(URL, params=params, timeout=10)`:** সার্ভারে GET request পাঠায়। `timeout=10` মানে ১০ সেকেন্ডে উত্তর না এলে থামবে।
- **কেন `try-except`:** ইন্টারনেট না থাকলে, timeout হলে বা DNS এ সমস্যা হলে `requests` একটি exception দেয়। না ধরলে লম্বা ভীতিকর error বার্তা দেখিয়ে প্রোগ্রাম বন্ধ হতো।
- **কেন `RequestException`:** এটি requests এর সব নেটওয়ার্ক error এর **মূল (parent) class**। এটি ধরলে `ConnectionError`, `Timeout` সব একসাথে ধরা পড়ে (অধ্যায় ৭)।
- **`raise SystemExit`:** উত্তরই আসেনি, তাই পরের কোড চালানোর মানে নেই। এটি প্রোগ্রাম পরিষ্কারভাবে থামায়।

#### লাইন ১৭: JSON কে dictionary তে রূপান্তর

```python
data = response.json()
```

- **কী হচ্ছে:** সার্ভারের পাঠানো JSON লেখাকে Python **dictionary** তে রূপান্তর করে।
- **কেন:** dictionary হলে `data["main"]["temp"]` এভাবে সহজে মান নেওয়া যায়। (`response.text` দিলে শুধু একটি লম্বা string পাওয়া যেত।)
- error হলেও (ভুল শহর, ভুল key) সার্ভার JSON পাঠায়, যার ভিতরে `message` থাকে। তাই এখানে এটি নিরাপদ।

#### লাইন ২০: সফল কিনা যাচাই

```python
if response.status_code == 200:
```

- **কী হচ্ছে:** `200` মানে সফলভাবে আবহাওয়ার ডাটা এসেছে।
- **কেন যাচাই:** ভুল শহরে `404`, ভুল key তে `401` আসে, আর তখন JSON এ `main`, `wind` এসব key থাকে না। যাচাই ছাড়া `data["main"]` লিখলে `KeyError` হতো।

#### লাইন ২১–২৭: আবহাওয়ার রিপোর্ট ছাপা

```python
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
```

- **`data["name"]`:** শহরের নাম (সরাসরি key)।
- **`data["sys"]["country"]`:** **nested dictionary**। `sys` এর ভিতরে আরেকটি dictionary আছে, তার `country` key থেকে দেশের কোড (`BD`)।
- **`data["main"]["temp"]`, `["feels_like"]`, `["humidity"]`:** `main` dictionary থেকে তাপমাত্রা, অনুভূত তাপমাত্রা ও আর্দ্রতা (%)।
- **`data["weather"][0]["description"]`:** `weather` একটি **list** (একাধিক অবস্থা থাকতে পারে), তাই `[0]` দিয়ে প্রথম উপাদান নেওয়া হয়। সেটি একটি dictionary, তার `description` (যেমন `haze`, `clear sky`)।
- **`data["wind"]["speed"]`:** বাতাসের গতি m/s এ।
- **কেন কোলন একই কলামে:** লেবেলের পরে স্পেস দিয়ে সমান করা হয়েছে, যাতে রিপোর্ট টেবিলের মতো সুন্দর দেখায়।

#### লাইন ২৮–২৯: ব্যর্থ হলে সার্ভারের বার্তা

```python
else:
    print("Error:", data.get("message"))
```

- **কী হচ্ছে:** সফল না হলে সার্ভার JSON এ `message` key তে কারণ লিখে পাঠায়। সেটি ছাপা হয়।
- **কেন `.get("message")` (`["message"]` নয়):** `.get()` key না থাকলে error না দিয়ে `None` দেয়। error এর উত্তরে `message` না থাকলেও প্রোগ্রাম ক্র্যাশ করবে না।

---

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** **config.py** এ শুধু API key ও URL (সেটিং), **api.py** সার্ভারের সাথে যোগাযোগ করে, **display.py** রিপোর্ট ছাপে। API key বদলাতে কোড না ঘেঁটে শুধু config.py খুলতে হয়।

```text
2_modular/
├── main.py
└── weather/
    ├── __init__.py
    ├── api.py
    ├── config.py
    └── display.py
```

#### `weather/__init__.py` — package এর দরজা

```python
"""weather package: get current weather from the OpenWeather API and show it."""

from .api import get_weather
from .display import print_report

__all__ = ["get_weather", "print_report"]
```

- `get_weather` ও `print_report` export করে। config বাইরে দেওয়া হয়নি, কারণ সেটি package এর ভিতরের ব্যবহারের জন্য।

#### `weather/config.py` — সেটিং (API key)

```python
API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"
```

- **এখানে `your_api_key_here` এর জায়গায় নিজের key বসান।** শুধু ভেরিয়েবল আছে, কোনো function নেই।

#### `weather/api.py` — API তে request

```python
import requests

from .config import API_KEY, URL


def get_weather(city):
    """Ask the API for a city's weather. Returns (status_code, data_dictionary)."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(URL, params=params, timeout=10)
    return response.status_code, response.json()
```

- `from .config import API_KEY, URL`: একই package এর config.py থেকে relative import।
- `get_weather(city)` `(status_code, data)` ফেরত দেয়। ইন্টারনেট error এখানে ধরা হয় না, main.py ধরে। কারণ error এর সময় কী দেখাতে হবে, সেই সিদ্ধান্ত main এর।

#### `weather/display.py` — রিপোর্ট ছাপা

```python
def print_report(data):
    """Print the basic weather data from the API dictionary."""
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
```

- `print_report(data)` dictionary থেকে মান নিয়ে ছাপে। ছাপার ধরন বদলাতে শুধু এই ফাইল বদলাতে হবে।

#### `main.py` — ইনপুট, error সামলানো ও চালানো

```python
import requests

from weather import get_weather, print_report

if __name__ == "__main__":
    city = input("Enter city name: ")
    try:
        status, data = get_weather(city)
    except requests.exceptions.RequestException:
        print("No internet connection!")
        raise SystemExit

    if status == 200:
        print_report(data)
    else:
        print("Error:", data.get("message"))
```

- `import requests` এখানেও লাগে, কারণ `requests.exceptions.RequestException` ধরা হচ্ছে।
- `status, data = get_weather(city)`: ফেরত আসা দুটি মান ভাগ করা। status 200 হলে `print_report(data)`, নাহলে error message।

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### সমাধান ৩: Google Colab (`3_colab/Job5_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job5_Weather_Report/3_colab/Job5_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

**📝 Cell 1: package install**

```python
!pip install requests
```

**📝 Cell 2: module import ও API key**  
চালানোর আগে your_api_key_here এর জায়গায় নিজের key বসান।

```python
import requests

API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"
```

**📝 Cell 3: ধাপ ১: শহরের নাম ইনপুট**  
শহরের নাম ইংরেজিতে দিন, যেমন Dhaka।

```python
# Step 1: take location from the user
city = input("Enter city name: ")
```

**📝 Cell 4: ধাপ ২: API তে request পাঠানো**  
সার্ভার থেকে JSON এনে dictionary বানানো।

```python
# Step 2: call the Open Weather API
params = {"q": city, "appid": API_KEY, "units": "metric"}
try:
    response = requests.get(URL, params=params, timeout=10)
except requests.exceptions.RequestException:
    print("No internet connection!")
    raise SystemExit

data = response.json()
```

**📝 Cell 5: ধাপ ৩: আবহাওয়ার রিপোর্ট দেখানো**

```python
# Step 3: print basic weather data
if response.status_code == 200:
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
else:
    print("Error:", data.get("message"))
```

> প্রথম কোড cell এ `your_api_key_here` এর জায়গায় নিজের API key বসিয়ে তারপর চালান।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `Error: Invalid API key` | key ভুল কপি হয়েছে, অথবা নতুন key এখনও সক্রিয় হয়নি। কিছুক্ষণ পরে আবার চেষ্টা করুন। |
| তাপমাত্রা ২৯৯ এর মতো বড় সংখ্যা | `units=metric` নেই, তাই Kelvin আসছে (°C = K − 273.15)। |
| `Error: city not found` | শহরের বানান ভুল। ইংরেজিতে সঠিক বানান দিন, প্রয়োজনে দেশ সহ: `Pabna,BD`। |
| `No internet connection!` | ইন্টারনেট সংযোগ দেখুন। |

### বাড়তি কাজ (অনুশীলন)

1. একাধিক শহরের নাম একটি list এ রেখে লুপে সবার আবহাওয়া দেখান।
2. প্রতিটি ফলাফল তারিখ-সময় সহ একটি CSV ফাইলে সংরক্ষণ করুন (জব ১ এর মতো)।
3. তাপমাত্রা ৩৫ °C এর বেশি হলে "Heat alert!" সতর্কবার্তা দেখান।
4. API key কোডে না লিখে environment variable থেকে নিন: `import os` তারপর `API_KEY = os.environ.get("OWM_API_KEY")`।

### ভাইভা প্রশ্ন ও উত্তর

1. **API এর পূর্ণরূপ কী?** Application Programming Interface।
2. **JSON কী?** key-value আকারে ডাটা আদান-প্রদানের একটি লেখাভিত্তিক ফরম্যাট, যা Python dictionary এর মতো দেখতে।
3. **`units=metric` কেন দেওয়া হয়?** সেলসিয়াসে তাপমাত্রা পেতে। না দিলে Kelvin আসে।
4. **API key কেন লাগে?** সার্ভার কে ব্যবহার করছে তা চেনে এবং ব্যবহারের সীমা (limit) নিয়ন্ত্রণ করে।
5. **`response.json()` কী করে?** JSON উত্তরকে Python dictionary তে রূপান্তর করে।
6. **`data["weather"][0]` এ `[0]` কেন?** `weather` একটি list, তাই প্রথম উপাদানটি নিতে হয়।
7. **`data.get("message")` ও `data["message"]` এর পার্থক্য কী?** key না থাকলে `.get()` `None` দেয়, কিন্তু `[...]` `KeyError` দেয়।
8. **status code 401 ও 404 এর অর্থ কী?** 401: অনুমতি নেই (ভুল API key)। 404: খোঁজা জিনিস পাওয়া যায়নি (ভুল শহর)।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।

[⬆ সূচিতে ফিরুন](#সূচি)

---

## জব ৬: Database App (Form + SQLite)

**কাজ:** ফর্ম দিয়ে ছাত্রের তথ্য student.db তে Save করে, Roll দিয়ে Search করে।

| সমাধান | ফাইল | চালাবেন |
|---|---|---|
| ১. Single file | [`1_single_file/p6_database_app.py`](../Job6_Database_App/1_single_file/p6_database_app.py) | কম্পিউটারে |
| ২. Module / Package | [`2_modular/main.py`](../Job6_Database_App/2_modular/main.py) + `student_db/` | কম্পিউটারে |
| ৩. Google Colab | [`3_colab/Job6_colab.ipynb`](../Job6_Database_App/3_colab/Job6_colab.ipynb) | ব্রাউজারে |

**তৈরি হবে:** student.db · **বিস্তারিত README:** [Job6_Database_App/README.md](../Job6_Database_App/README.md)

**requirements.txt** (জবের ফোল্ডারে, তিন সমাধানের জন্যই)

```text
# এই জবে বাইরের কোনো package লাগে না
```

> এটি একটি window (GUI) খোলে, তাই **লোকাল কম্পিউটারে** চালান। Google Colab এ window খোলে না। Colab এর জন্য `3_colab/p6_console_colab.py` (মেনু সংস্করণ) দেওয়া আছে।

### সমাধান ১: Single file (`1_single_file/p6_database_app.py`)

```python
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Step 1: database and table
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()

# Step 4: button functions
def save_data():
    roll = e_roll.get().strip()
    name = e_name.get().strip()
    if roll == "" or name == "":
        messagebox.showwarning("Missing", "Roll and Name are required")
        return
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, e_dept.get(), e_phone.get()))
        conn.commit()
        messagebox.showinfo("Saved", "Student saved successfully")
        clear_form()
        show_all()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "This roll already exists")

def search_data():
    roll = e_roll.get().strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        clear_form()
        e_roll.insert(0, row[0])
        e_name.insert(0, row[1])
        e_dept.insert(0, row[2])
        e_phone.insert(0, row[3])
    else:
        messagebox.showinfo("Not found", "No student with roll " + roll)

def clear_form():
    for entry in (e_roll, e_name, e_dept, e_phone):
        entry.delete(0, tk.END)

def show_all():
    listbox.delete(0, tk.END)
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        listbox.insert(tk.END, " | ".join(row))

# Step 2: design the form
root = tk.Tk()
root.title("Student Database")
root.geometry("460x400")

labels = ["Roll", "Name", "Department", "Phone"]
entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=10, pady=6, sticky="w")
    entry = tk.Entry(root, width=30, font=("Arial", 11))
    entry.grid(row=i, column=1, padx=10, pady=6)
    entries.append(entry)
e_roll, e_name, e_dept, e_phone = entries

# Step 3: command buttons
frame = tk.Frame(root)
frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Save", width=10, command=save_data).pack(side="left", padx=5)
tk.Button(frame, text="Search", width=10, command=search_data).pack(side="left", padx=5)
tk.Button(frame, text="Clear", width=10, command=clear_form).pack(side="left", padx=5)

listbox = tk.Listbox(root, width=55, height=8)
listbox.grid(row=5, column=0, columnspan=2, padx=10)
show_all()

root.mainloop()
conn.close()
```

চালানো (জবের ফোল্ডারে venv চালু অবস্থায়):

```bash
cd 1_single_file
python p6_database_app.py
```

যা দেখা যাবে:

```text
Save   → "Student saved successfully"
একই Roll আবার Save → "This roll already exists"
Roll/Name খালি Save → "Roll and Name are required"
Search 701234 → ফর্মে তথ্য ভরে যায়
Search 709999 → "No student with roll 709999"
```

### সমাধান ১ এর কোডের ব্যাখ্যা (লাইন/ব্লক ধরে): কী হচ্ছে ও কেন

> **কোডের ক্রম লক্ষ করুন:** Step 1 (ডাটাবেস) → Step 4 (function) → Step 2 (ফর্ম) → Step 3 (বোতাম)। function গুলো বোতামের **আগে** লেখা হয়েছে, কারণ লাইন ৭১–৭৩ এ `command=save_data` লেখার সময় `save_data` নামটি আগেই তৈরি থাকতে হবে।

#### লাইন ১–৩: module আনা

```python
import sqlite3
import tkinter as tk
from tkinter import messagebox
```

- **`sqlite3`:** ডাটাবেস তৈরি, ডাটা রাখা ও খোঁজার জন্য।
- **`import tkinter as tk`:** `as tk` মানে ছোট ডাকনাম। প্রতিবার `tkinter.Label` না লিখে `tk.Label` লেখা যায়।
- **`from tkinter import messagebox`:** ছোট বার্তার পপআপ (তথ্য, সতর্কতা, error) দেখানোর জন্য। এটি tkinter এর একটি আলাদা submodule, তাই আলাদা করে import করতে হয়।

#### লাইন ৬–৭: ডাটাবেসের সাথে সংযোগ

```python
conn = sqlite3.connect("student.db")
cur = conn.cursor()
```

- **`sqlite3.connect("student.db")`:** `student.db` ফাইলের সাথে সংযোগ (connection) তৈরি করে। ফাইল না থাকলে **নিজেই নতুন তৈরি করে**।
- **`conn.cursor()`:** একটি cursor object দেয়, যা দিয়ে SQL কমান্ড চালানো ও ফলাফল আনা হয়।
- **connection ও cursor দুটো কেন:** connection হলো ডাটাবেসের সাথে "লাইন", যা দিয়ে `commit` ও `close` হয়। cursor হলো সেই লাইনে কাজ করার "হাত", যা দিয়ে `execute` ও `fetch` হয়।

#### লাইন ৮–১৩: টেবিল তৈরি

```python
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()
```

- **`execute()`:** একটি SQL কমান্ড চালায়।
- **`"""..."""` (তিন উদ্ধৃতি):** একাধিক লাইনের string, তাই লম্বা SQL সুন্দর করে লেখা যায়।
- **`CREATE TABLE IF NOT EXISTS`:** টেবিল না থাকলে তৈরি করে। থাকলে কিছু করে না। **কেন:** প্রোগ্রাম দ্বিতীয়বার চালালে "table already exists" error হবে না, আর আগের ডাটাও মুছবে না।
- **`roll TEXT PRIMARY KEY`:** roll প্রতিটি রেকর্ডের অনন্য পরিচয়। একই roll দুবার ঢোকানো যাবে না। **কেন TEXT:** roll দিয়ে হিসাব হয় না, আর শুরুতে ০ থাকলে সংখ্যায় তা হারিয়ে যেত।
- **`name TEXT NOT NULL`:** নাম ছাড়া রেকর্ড রাখা যাবে না।
- **`conn.commit()`:** পরিবর্তন স্থায়ীভাবে ফাইলে লেখে। **commit না দিলে প্রোগ্রাম বন্ধ হলে পরিবর্তন হারিয়ে যায়।**

#### লাইন ১৬–২১: Save function — খালি ইনপুট যাচাই

```python
def save_data():
    roll = e_roll.get().strip()
    name = e_name.get().strip()
    if roll == "" or name == "":
        messagebox.showwarning("Missing", "Roll and Name are required")
        return
```

- **`e_roll.get()`:** Entry বক্সে ব্যবহারকারী যা লিখেছে তা string হিসেবে দেয়। `.strip()` শুরু-শেষের স্পেস সরায়।
- **কেন নিজে যাচাই:** ডাটাবেস খালি string (`""`) কে NULL ধরে না, তাই `NOT NULL` থাকা সত্ত্বেও খালি নাম ঢুকে যেত। এজন্য আগেই কোডে যাচাই করা হয়।
- **`messagebox.showwarning(শিরোনাম, বার্তা)`:** হলুদ সতর্কতা চিহ্নসহ পপআপ দেখায়।
- **`return`:** function এখানেই শেষ। নিচের সংরক্ষণের কোড আর চলবে না।

#### লাইন ২২–৩০: Save function — ডাটাবেসে রাখা

```python
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, e_dept.get(), e_phone.get()))
        conn.commit()
        messagebox.showinfo("Saved", "Student saved successfully")
        clear_form()
        show_all()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "This roll already exists")
```

- **`INSERT INTO students VALUES (?, ?, ?, ?)`:** টেবিলে একটি নতুন সারি যোগ করে। চারটি `?` হলো **placeholder**। দ্বিতীয় argument এর tuple থেকে মান ক্রমানুসারে বসে।
- **কেন `?` (string জোড়া দিয়ে নয়):** কেউ ফর্মে `'); DROP TABLE students; --` এর মতো কিছু লিখলে string জোড়া দিলে সেটি SQL কমান্ড হিসেবে চলে যেত। একে **SQL injection** বলে। `?` দিলে sqlite3 মানটিকে শুধু ডাটা হিসেবে ধরে, তাই নিরাপদ। এটি ডাটাবেস প্রোগ্রামিং এর অবশ্য পালনীয় নিয়ম।
- **`conn.commit()`:** নতুন রেকর্ড স্থায়ী করে।
- **`showinfo`:** নীল "i" চিহ্নসহ সফলতার বার্তা।
- **`clear_form()` ও `show_all()`:** সংরক্ষণের পরে ফর্ম খালি করে এবং তালিকায় নতুন রেকর্ড দেখায়।
- **কেন `try-except sqlite3.IntegrityError`:** একই roll আবার দিলে `PRIMARY KEY` নিয়ম ভাঙে এবং sqlite3 `IntegrityError` দেয়। না ধরলে প্রোগ্রাম error দিত। এখন লাল error পপআপ (`showerror`) দেখায়।

#### লাইন ৩২–৪৩: Search function

```python
def search_data():
    roll = e_roll.get().strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        clear_form()
        e_roll.insert(0, row[0])
        e_name.insert(0, row[1])
        e_dept.insert(0, row[2])
        e_phone.insert(0, row[3])
    else:
        messagebox.showinfo("Not found", "No student with roll " + roll)
```

- **`SELECT * FROM students WHERE roll = ?`:** যে সারির roll মিলে তার সব কলাম (`*`) খোঁজে।
- **কেন `(roll,)` (শেষে কমা):** parameter সবসময় tuple হতে হয়। একটি মানের tuple লিখতে শেষে কমা দিতে হয়। `(roll)` শুধু বন্ধনী, tuple নয়।
- **`fetchone()`:** ফলাফলের প্রথম সারি একটি tuple হিসেবে দেয়, যেমন `('701235', 'Sumaiya Akter', 'CST', '01812345678')`। কিছু না পেলে `None` দেয়।
- **কেন `fetchone` (`fetchall` নয়):** roll PRIMARY KEY, তাই সর্বোচ্চ একটি সারিই মিলবে।
- **`if row:`:** `None` হলে false, tuple হলে true। খুব সংক্ষেপে "পাওয়া গেছে কিনা" যাচাই।
- **`clear_form()` তারপর `insert(0, ...)`:** আগে বক্সগুলো খালি করে, তারপর প্রতিটি বক্সের শুরুতে (index 0) পাওয়া মান বসায়। আগে খালি না করলে নতুন লেখা পুরোনো লেখার সাথে জুড়ে যেত।
- **না পেলে:** "Not found" বার্তা।

#### লাইন ৪৫–৪৭: Clear function

```python
def clear_form():
    for entry in (e_roll, e_name, e_dept, e_phone):
        entry.delete(0, tk.END)
```

- **কী হচ্ছে:** চারটি Entry বক্স একটি tuple এ রেখে লুপ চালানো হলো। প্রতিটি থেকে `delete(0, tk.END)` সব লেখা মুছে দেয়।
- **`delete(শুরু, শেষ)`:** `0` প্রথম অক্ষর, `tk.END` শেষ অক্ষর পর্যন্ত, অর্থাৎ সব মুছে যায়।
- **কেন লুপ:** চারবার একই লাইন না লিখে এক জায়গায় লিখলে কোড ছোট হয় এবং নতুন field যোগ করা সহজ হয়।

#### লাইন ৪৯–৫২: সব রেকর্ড তালিকায় দেখানো

```python
def show_all():
    listbox.delete(0, tk.END)
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        listbox.insert(tk.END, " | ".join(row))
```

- **`listbox.delete(0, tk.END)`:** তালিকার পুরোনো সব লাইন মুছে দেয়। **কেন:** না মুছলে প্রতিবার Save এর পরে একই রেকর্ড আবার যোগ হয়ে ডুপ্লিকেট দেখাত।
- **`ORDER BY roll`:** roll অনুযায়ী ছোট থেকে বড় ক্রমে সাজানো ফলাফল দেয়।
- **`for row in cur.execute(...)`:** `execute()` cursor ফেরত দেয়, আর cursor এর উপর সরাসরি লুপ চালানো যায়। প্রতিবার একটি সারি (tuple) আসে।
- **`" | ".join(row)`:** tuple এর সব মান মাঝে `" | "` দিয়ে জুড়ে একটি লেখা বানায়: `701234 | Rahim Uddin | CST | 01712345678`। (`join` শুধু string জুড়তে পারে। এখানে সব কলাম TEXT, তাই কাজ করে।)
- **`listbox.insert(tk.END, ...)`:** লেখাটি তালিকার শেষে যোগ করে।

#### লাইন ৫৫–৫৭: মূল window তৈরি

```python
root = tk.Tk()
root.title("Student Database")
root.geometry("460x400")
```

- **`tk.Tk()`:** প্রোগ্রামের মূল window তৈরি করে। সব widget (label, button) এর ভিতরেই বসবে।
- **`title()`:** window এর উপরের বারে নাম।
- **`geometry("প্রস্থxউচ্চতা")`:** window এর আকার পিক্সেলে। মাঝে ইংরেজি ছোট হাতের `x`।

#### লাইন ৫৯–৬৬: Label ও Entry (field) তৈরি

```python
labels = ["Roll", "Name", "Department", "Phone"]
entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=10, pady=6, sticky="w")
    entry = tk.Entry(root, width=30, font=("Arial", 11))
    entry.grid(row=i, column=1, padx=10, pady=6)
    entries.append(entry)
e_roll, e_name, e_dept, e_phone = entries
```

- **কেন লুপ:** চারটি field এর জন্য একই ধরনের কোড চারবার না লিখে list ও লুপ ব্যবহার করা হয়েছে।
- **`enumerate(labels)`:** প্রতিটি উপাদানের সাথে তার ক্রমিক নম্বরও দেয়: `(0, "Roll")`, `(1, "Name")`... `i` সারির নম্বর হিসেবে কাজে লাগে।
- **`tk.Label(root, text=..., font=...)`:** স্থির লেখা (ব্যবহারকারী বদলাতে পারে না)।
- **`tk.Entry(root, width=30, ...)`:** এক লাইনের লেখার বক্স। `width=30` মানে প্রায় ৩০ অক্ষর চওড়া।
- **`.grid(row=i, column=...)`:** widget কে টেবিলের মতো সারি-কলামে বসায়। Label কলাম 0 তে (বামে), Entry কলাম 1 এ (ডানে)।
  - `padx`, `pady` চারপাশে ফাঁকা জায়গা।
  - `sticky="w"` (west) Label কে বাম দিকে সাঁটিয়ে রাখে।
- **কেন `grid` (`pack` নয়):** ফর্মে লেবেল আর বক্স সারিবদ্ধ রাখতে grid সবচেয়ে সুবিধাজনক।
- **কেন Label এ ভেরিয়েবল নেই কিন্তু Entry তে আছে:** Label এর সাথে পরে কোনো কাজ নেই। Entry থেকে পরে `.get()` দিয়ে লেখা নিতে হবে, তাই প্রতিটি Entry `entries` list এ রাখা হয়েছে।
- **`e_roll, e_name, e_dept, e_phone = entries`:** **unpacking**। list এর চারটি Entry ক্রমানুসারে চারটি নামের ভেরিয়েবলে যায়, যাতে function গুলোতে অর্থবোধক নামে ব্যবহার করা যায়।

#### লাইন ৬৯–৭৩: Command button

```python
frame = tk.Frame(root)
frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Save", width=10, command=save_data).pack(side="left", padx=5)
tk.Button(frame, text="Search", width=10, command=search_data).pack(side="left", padx=5)
tk.Button(frame, text="Clear", width=10, command=clear_form).pack(side="left", padx=5)
```

- **`tk.Frame`:** একটি অদৃশ্য ধারক (container)। তিনটি বোতাম একসাথে রাখার জন্য।
- **`columnspan=2`:** Frame টি দুটি কলাম জুড়ে বসে, তাই বোতামগুলো মাঝখানে থাকে।
- **`tk.Button(..., command=save_data)`:** বোতাম চাপলে যে function চলবে তার **নাম** দেওয়া হয়।
- **কেন `save_data` এর পরে `()` নেই:** `command=save_data()` লিখলে function টি window তৈরির সময়েই একবার চলে যেত, বোতাম চাপার জন্য অপেক্ষা করত না। আমরা function টি **হাতে তুলে দিচ্ছি**, এখনই **চালাচ্ছি না**।
- **`.pack(side="left")`:** Frame এর ভিতরে বোতামগুলো বাম থেকে পাশাপাশি বসায়।
- **কেন Frame এর ভিতরে `pack`:** একই container এ `grid` ও `pack` একসাথে ব্যবহার করা যায় না। root এ grid ব্যবহার হয়েছে, তাই আলাদা Frame এ pack ব্যবহার করা হয়েছে।

#### লাইন ৭৫–৭৭: তালিকা বক্স

```python
listbox = tk.Listbox(root, width=55, height=8)
listbox.grid(row=5, column=0, columnspan=2, padx=10)
show_all()
```

- **`tk.Listbox`:** একাধিক লাইনের তালিকা দেখানোর widget। `height=8` মানে একসাথে ৮টি লাইন দেখা যায়।
- **`show_all()`:** প্রোগ্রাম চালু হতেই ডাটাবেসে আগে থেকে থাকা রেকর্ডগুলো তালিকায় দেখায়।

#### লাইন ৭৯–৮০: window চালু রাখা ও সংযোগ বন্ধ

```python
root.mainloop()
conn.close()
```

- **`root.mainloop()`:** window টি খোলা রাখে এবং ক্লিক, টাইপ ইত্যাদি **event এর জন্য অপেক্ষা করে**। এটি না দিলে window এক মুহূর্তে খুলে বন্ধ হয়ে যেত। ব্যবহারকারী window বন্ধ (✕) না করা পর্যন্ত প্রোগ্রাম এই লাইনেই থাকে।
- **`conn.close()`:** window বন্ধ হলে ডাটাবেসের সংযোগ বন্ধ করে। এটি ভালো অভ্যাস, এতে ফাইল লক হয়ে থাকে না।

---

### সমাধান ২: Module / Package (`2_modular/`)

**মূল ধারণা:** **database.py** শুধু ডাটাবেসের কাজ করে (কোনো window নেই), **gui.py** শুধু ফর্ম দেখায় এবং database এর function ডাকে। একই database.py Colab এর মেনু সংস্করণেও ব্যবহার করা যায়। এটাই module এর আসল সুবিধা।

```text
2_modular/
├── main.py
└── student_db/
    ├── __init__.py
    ├── database.py
    └── gui.py
```

#### `student_db/__init__.py` — package এর দরজা

```python
"""student_db package: SQLite database functions and a tkinter form that uses them."""

from .database import create_table, save_student, find_student, all_students

__all__ = ["create_table", "save_student", "find_student", "all_students"]
```

- ডাটাবেসের চারটি function export করে। gui কে আলাদা রাখা হয়েছে, কারণ GUI ছাড়াও (যেমন Colab এ) ডাটাবেস ব্যবহার করা যায়।

#### `student_db/database.py` — ডাটাবেসের কাজ

```python
import sqlite3

DB_FILE = "student.db"


def create_table():
    """Create the students table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
                      roll TEXT PRIMARY KEY,
                      name TEXT NOT NULL,
                      department TEXT,
                      phone TEXT)""")
    conn.commit()
    conn.close()


def save_student(roll, name, department, phone):
    """Insert one student. Return True if saved, False if the roll already exists."""
    conn = sqlite3.connect(DB_FILE)
    try:
        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                     (roll, name, department, phone))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def find_student(roll):
    """Return the student row as a tuple, or None if not found."""
    conn = sqlite3.connect(DB_FILE)
    row = conn.execute("SELECT * FROM students WHERE roll = ?", (roll,)).fetchone()
    conn.close()
    return row


def all_students():
    """Return a list of all student rows sorted by roll."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute("SELECT * FROM students ORDER BY roll").fetchall()
    conn.close()
    return rows
```

- প্রতিটি function নিজে সংযোগ খোলে ও বন্ধ করে (`connect` → কাজ → `close`)। তাই কোনো global connection লাগে না।
- `save_student()`: সফল হলে `True`, একই roll থাকলে `False` ফেরত দেয়। `try / except / finally`: `finally` অংশ সফল বা ব্যর্থ, দুই ক্ষেত্রেই চলে, তাই সংযোগ সবসময় বন্ধ হয়।
- `find_student(roll)` একটি সারি বা `None`। `all_students()` সব সারির list (`fetchall()`)।

#### `student_db/gui.py` — ফর্ম (GUI)

```python
import tkinter as tk
from tkinter import messagebox

from .database import create_table, save_student, find_student, all_students


def run_app():
    """Build the student form window and start it."""
    create_table()

    root = tk.Tk()
    root.title("Student Database")
    root.geometry("460x400")

    labels = ["Roll", "Name", "Department", "Phone"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=10, pady=6, sticky="w")
        entry = tk.Entry(root, width=30, font=("Arial", 11))
        entry.grid(row=i, column=1, padx=10, pady=6)
        entries.append(entry)
    e_roll, e_name, e_dept, e_phone = entries

    listbox = tk.Listbox(root, width=55, height=8)

    def clear_form():
        for entry in entries:
            entry.delete(0, tk.END)

    def show_all():
        listbox.delete(0, tk.END)
        for row in all_students():
            listbox.insert(tk.END, " | ".join(row))

    def save_data():
        roll = e_roll.get().strip()
        name = e_name.get().strip()
        if roll == "" or name == "":
            messagebox.showwarning("Missing", "Roll and Name are required")
            return
        if save_student(roll, name, e_dept.get(), e_phone.get()):
            messagebox.showinfo("Saved", "Student saved successfully")
            clear_form()
            show_all()
        else:
            messagebox.showerror("Error", "This roll already exists")

    def search_data():
        roll = e_roll.get().strip()
        row = find_student(roll)
        if row:
            clear_form()
            for entry, value in zip(entries, row):
                entry.insert(0, value)
        else:
            messagebox.showinfo("Not found", "No student with roll " + roll)

    frame = tk.Frame(root)
    frame.grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Save", width=10, command=save_data).pack(side="left", padx=5)
    tk.Button(frame, text="Search", width=10, command=search_data).pack(side="left", padx=5)
    tk.Button(frame, text="Clear", width=10, command=clear_form).pack(side="left", padx=5)

    listbox.grid(row=5, column=0, columnspan=2, padx=10)
    show_all()

    root.mainloop()
```

- `from .database import ...`: একই package এর database.py থেকে relative import।
- `run_app()` এর **ভিতরেই** save_data, search_data ইত্যাদি function লেখা হয়েছে (**nested function**)। এরা run_app এর ভেরিয়েবল (entries, listbox) সরাসরি ব্যবহার করতে পারে, global ভেরিয়েবল লাগে না।
- `if save_student(...):` function এর True/False ফলাফল দিয়েই বার্তা বাছাই। GUI এ কোনো SQL নেই।
- `for entry, value in zip(entries, row):` **zip()** দুটি list জোড়ায় জোড়ায় মেলায়: প্রথম বক্সে প্রথম মান, দ্বিতীয় বক্সে দ্বিতীয় মান...

#### `main.py` — প্রোগ্রাম শুরু

```python
from student_db.gui import run_app

if __name__ == "__main__":
    run_app()
```

- `from student_db.gui import run_app`: package এর ভিতরের নির্দিষ্ট module (gui) থেকে সরাসরি import।
- main.py মাত্র কয়েক লাইন। পুরো প্রোগ্রাম package এর ভিতরে, main শুধু শুরু করে।

চালানো:

```bash
cd 2_modular
python main.py
```

> আউটপুট সমাধান ১ এর মতোই হবে (পরীক্ষিত)। `main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package টি খুঁজে পায়।

### Colab এর জন্য আলাদা ফাইল: `3_colab/p6_console_colab.py`

Colab এর জন্য (মেনু দিয়ে, একই ডাটাবেস)। Colab এ নিচের notebook এ এই কোডটিই cell এ ভাগ করা আছে।

```python
import sqlite3

# Step 1: database and table
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()

# Step 2: functions for save, search and show
def save_data():
    roll = input("Roll: ").strip()
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    phone = input("Phone: ").strip()
    if roll == "" or name == "":
        print("Missing: Roll and Name are required")
        return
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, dept, phone))
        conn.commit()
        print("Saved: Student saved successfully")
    except sqlite3.IntegrityError:
        print("Error: This roll already exists")

def search_data():
    roll = input("Enter roll to search: ").strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        print("Found:", " | ".join(row))
    else:
        print("Not found: No student with roll " + roll)

def show_all():
    print("------ All Students ------")
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        print(" | ".join(row))

# Step 3: menu (works in Google Colab, where no GUI window can open)
while True:
    print("\n1. Save   2. Search   3. Show all   4. Exit")
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        save_data()
    elif choice == "2":
        search_data()
    elif choice == "3":
        show_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

conn.close()
print("Bye!")
```

### সমাধান ৩: Google Colab (`3_colab/Job6_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

- **পদ্ধতি ক (সহজ):** colab.research.google.com → **File → Upload notebook** → `Job6_Database_App/3_colab/Job6_colab.ipynb` আপলোড → প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।
- **পদ্ধতি খ (নিজে বানিয়ে):** **File → New notebook**। নিচের প্রতিটি কোড **+ Code** দিয়ে নতুন cell এ পেস্ট করে ক্রমানুসারে চালান।

notebook টি দেখতে এমন:

> > Colab এ কোনো স্ক্রিন নেই, তাই tkinter এর window খোলে না। এখানে একই ডাটাবেস মেনু দিয়ে চালানো হচ্ছে। GUI সংস্করণ `p6_database_app.py` লোকাল কম্পিউটারে চালান।

> এই জবে বাইরের কোনো package লাগে না (শুধু built-in module), তাই install এর cell নেই।

**📝 Cell 1: module import ও ডাটাবেস টেবিল**  
student.db ও students টেবিল তৈরি হবে।

```python
import sqlite3

# Step 1: database and table
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()
```

**📝 Cell 2: function ১: save_data() তৈরি**  
নতুন ছাত্র সংরক্ষণের function। শুধু তৈরি হবে।

```python
# Step 2: functions for save, search and show
def save_data():
    roll = input("Roll: ").strip()
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    phone = input("Phone: ").strip()
    if roll == "" or name == "":
        print("Missing: Roll and Name are required")
        return
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, dept, phone))
        conn.commit()
        print("Saved: Student saved successfully")
    except sqlite3.IntegrityError:
        print("Error: This roll already exists")
```

**📝 Cell 3: function ২: search_data() তৈরি**  
roll দিয়ে খোঁজার function।

```python
def search_data():
    roll = input("Enter roll to search: ").strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        print("Found:", " | ".join(row))
    else:
        print("Not found: No student with roll " + roll)
```

**📝 Cell 4: function ৩: show_all() তৈরি**  
সব রেকর্ড দেখানোর function।

```python
def show_all():
    print("------ All Students ------")
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        print(" | ".join(row))
```

**📝 Cell 5: মেনু চালানো**  
1 Save, 2 Search, 3 Show all, 4 Exit। শেষে 4 দিন।

```python
# Step 3: menu (works in Google Colab, where no GUI window can open)
while True:
    print("\n1. Save   2. Search   3. Show all   4. Exit")
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        save_data()
    elif choice == "2":
        search_data()
    elif choice == "3":
        show_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

conn.close()
print("Bye!")
```

**📝 Cell 6: ডাটাবেসে কী আছে দেখা**

```python
import sqlite3
conn = sqlite3.connect("student.db")
for row in conn.execute("SELECT * FROM students"):
    print(row)
conn.close()
```

> Colab এ window (GUI) খোলে না, তাই এখানে **p6_console_colab.py** (মেনু সংস্করণ) ব্যবহার করুন। মেনুতে 1 Save, 2 Search, 3 Show all, 4 Exit।

### অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] সমাধান ১ চালিয়ে “যা দেখা যাবে” অংশের সাথে মিলিয়ে দেখুন।
- [ ] সমাধান ২ এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই কিনা দেখুন।
- [ ] সমাধান ২ এর প্রতিটি ফাইল খুলে বলুন কোন function কোথায় আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] Colab এ notebook চালান, প্রতিটি cell এর পরে কী হলো খেয়াল করুন।
- [ ] নিচের ভাইভা প্রশ্নগুলোর উত্তর নিজে বলুন, তারপর মিলিয়ে দেখুন।

### এই জবে সমস্যা হলে

| সমস্যা | কারণ ও সমাধান |
|---|---|
| window খোলার আগেই Save চলে যায় | `command=save_data()` লেখা হয়েছে। `()` বাদ দিন। |
| `database is locked` | `student.db` অন্য সফটওয়্যারে (যেমন DB Browser) খোলা আছে। বন্ধ করুন। |
| `ModuleNotFoundError: No module named 'tkinter'` (Linux) | `sudo apt install python3-tk` |
| Colab এ `TclError: no display name` | Colab এ GUI চলে না। `p6_console_colab.py` ব্যবহার করুন। |
| প্রোগ্রাম বন্ধ করলে ডাটা থাকে না | কোনো জায়গায় `conn.commit()` বাদ পড়েছে। |
| শুরু থেকে নতুন করে চাই | `student.db` ফাইলটি মুছে দিন। |

### বাড়তি কাজ (অনুশীলন)

1. **Update** বোতাম যোগ করুন: `UPDATE students SET name = ?, department = ?, phone = ? WHERE roll = ?`
2. **Delete** বোতাম যোগ করুন: `DELETE FROM students WHERE roll = ?`। মোছার আগে `messagebox.askyesno()` দিয়ে নিশ্চিত হয়ে নিন।
3. Listbox এ একটি লাইনে ক্লিক করলে সেই রেকর্ড ফর্মে ভরে যাবে (`listbox.bind("<<ListboxSelect>>", ...)`)।
4. Department এর জন্য Entry এর বদলে `ttk.Combobox` (CST, Civil, Electrical...) ব্যবহার করুন।

### ভাইভা প্রশ্ন ও উত্তর

1. **SQLite এর সুবিধা কী?** আলাদা সার্ভার লাগে না, পুরো ডাটাবেস একটি ফাইলে থাকে, এবং Python এর সাথেই আসে।
2. **PRIMARY KEY কেন ব্যবহার করা হয়েছে?** প্রতিটি রেকর্ড অনন্য রাখতে। একই roll দুবার ঢোকানো যায় না।
3. **`?` placeholder কেন ব্যবহার করা হয়?** SQL injection ঠেকাতে এবং নিরাপদে মান বসাতে।
4. **`commit()` না দিলে কী হবে?** পরিবর্তন স্থায়ীভাবে ফাইলে সংরক্ষিত হবে না।
5. **`fetchone()` ও `fetchall()` এর পার্থক্য কী?** `fetchone()` একটি সারি (বা `None`) দেয়, `fetchall()` সব সারির list দেয়।
6. **`command=save_data` এ `()` কেন দেওয়া হয় না?** `()` দিলে function তখনই চলে যেত। আমরা শুধু function টি বোতামকে দিচ্ছি, যাতে ক্লিক করলে চলে।
7. **`mainloop()` এর কাজ কী?** window খোলা রেখে ব্যবহারকারীর event (ক্লিক, টাইপ) এর জন্য অপেক্ষা করা।
8. **`grid` ও `pack` এর পার্থক্য কী?** `grid` সারি-কলামে সাজায়। `pack` উপর-নিচে বা পাশাপাশি সাজায়। একই container এ দুটি একসাথে ব্যবহার করা যায় না।
9. **`(roll,)` এ কমা কেন?** একটি মানের tuple বানাতে কমা লাগে। শুধু `(roll)` tuple নয়।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।

[⬆ সূচিতে ফিরুন](#সূচি)

---

## Google Colab: সাধারণ নিয়ম

Colab ব্রাউজারে চলে, প্রতিটি notebook Google এর আলাদা মেশিনে চলে। তাই এখানে venv লাগে না।

**পদ্ধতি ক: দেওয়া .ipynb ফাইল দিয়ে (সবচেয়ে সহজ)**

1. colab.research.google.com খুলে Google একাউন্টে লগইন করুন।
2. **File → Upload notebook** থেকে জবের `3_colab` ফোল্ডারের `JobN_colab.ipynb` আপলোড করুন।
3. উপর থেকে প্রতিটি cell একটি একটি করে চালান: **Shift + Enter**। ইনপুটের ঘর এলে মান লিখে Enter।
4. তৈরি ফাইল (CSV, PDF, PNG) বাম পাশের **📁 Files** এ পাওয়া যাবে। ডাউনলোড করতে ফাইলের পাশে ⋮ চাপুন।

**পদ্ধতি খ: নিজে নতুন notebook বানিয়ে**

| cell এর ধরন | কী হয় |
|---|---|
| package install (`!pip install ...`) | Colab এ package install হয়। শুরুতে `!` মানে এটি Terminal এর কমান্ড। |
| module import | প্রয়োজনীয় লাইব্রেরি আনা। |
| function তৈরি (`def ...`) | শুধু function তৈরি হয়, চালালে কিছু দেখায় না। |
| ধাপ / চালানো | আসল কাজ হয়, ইনপুট চায়, আউটপুট দেখায়। |

একটি notebook এর সব cell একই memory শেয়ার করে, তাই **উপর থেকে ক্রমানুসারে চালাতে হবে**। `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি; **Runtime → Run all** দিন।

> **জব ৬:** Colab এ window খোলে না, তাই মেনু সংস্করণ দেওয়া আছে। **সতর্কতা:** Colab বন্ধ হলে সব ফাইল মুছে যায়, দরকারি ফাইল ডাউনলোড করে রাখুন।

## সমস্যা হলে

| দেখাচ্ছে | যা করবেন |
|---|---|
| `'python' is not recognized` | Python install এ “Add to PATH” টিক দেওয়া হয়নি। installer আবার চালিয়ে ঠিক করুন, অথবা `python` এর বদলে `py` লিখুন। |
| `ModuleNotFoundError` | লাইনের শুরুতে `(venv)` নেই। আগে activate করুন, তারপর `pip install -r requirements.txt`। |
| Terminal এ চলে কিন্তু ▶ চাপলে চলে না | VS Code এ interpreter হিসেবে venv বেছে নিন (Ctrl+Shift+P → Python: Select Interpreter)। |
| `IndentationError` | কপির সময় লাইনের শুরুর স্পেস নষ্ট হয়েছে। গাইডের মতো করে স্পেস (৪টি) ঠিক করুন। |
| `PermissionError` | CSV/PDF ফাইলটি Excel বা অন্য সফটওয়্যারে খোলা। বন্ধ করে আবার চালান। |
| জব ৫: `Invalid API key` | key ঠিকমতো বসেনি বা এখনও চালু হয়নি। কিছুক্ষণ পর চেষ্টা করুন। |

[⬆ সূচিতে ফিরুন](#সূচি)
