# জব ১: Inventory Management for Fruits Item

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ৩ | **নম্বর:** ৪

## উদ্দেশ্য

ব্যবহারকারীর কাছ থেকে ফলের নাম, একক দাম ও পরিমাণ নেওয়া হবে। মোট দাম হিসাব করে `fruits.csv` ফাইলে সংরক্ষণ করা হবে। শেষে CSV ফাইল থেকে পড়ে সারাংশ দেখানো হবে।

সিলেবাসের ধাপ: 1.1 Setup Environment → 1.2 Take item data from the user → 1.3 Store items data into CSV → 1.4 Print summary from stored CSV

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

### ফোল্ডারের গঠন

```
Job1_Fruit_Inventory/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p1_inventory.py
├── 2_modular/
│   ├── main.py
│   └── fruit_inventory/
│       ├── __init__.py
│       ├── report.py
│       └── storage.py
└── 3_colab/
    └── Job1_colab.ipynb
```

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job1_Fruit_Inventory` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p1_inventory.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `fruit_inventory` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job1_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

কাজ শেষে Terminal এ `deactivate`।

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে)

### লাইন ১–২: প্রয়োজনীয় module আনা

```python
import csv
import os
```

- **কী হচ্ছে:** Python এর সাথে আসা দুটি module প্রোগ্রামে আনা হচ্ছে।
- **কেন `csv`:** CSV ফাইলে সঠিকভাবে লেখা ও পড়ার জন্য। নিজে হাতে কমা বসালে ভুলের সম্ভাবনা থাকে। যেমন নামের ভিতরে কমা থাকলে কলাম ভেঙে যায়। `csv` module এগুলো নিজেই সামলায়।
- **কেন `os`:** ফাইলটি আগে থেকে আছে কিনা যাচাই করার জন্য (`os.path.exists`)।
- দুটিই built-in, তাই `pip install` লাগে না।

### লাইন ৪: ফাইলের নাম একটি ভেরিয়েবলে

```python
FILE = "fruits.csv"
```

- **কী হচ্ছে:** ফাইলের নাম `FILE` নামের ভেরিয়েবলে রাখা হলো।
- **কেন:** একই নাম প্রোগ্রামে কয়েকবার লাগে। নাম বদলাতে হলে শুধু এই এক লাইন বদলালেই হবে। বড় হাতের নাম (`FILE`) দিয়ে বোঝানো হয় এটি একটি ধ্রুবক (constant), প্রোগ্রাম চলার সময় বদলাবে না।

### লাইন ৬: ইনপুট নেওয়ার function শুরু

```python
def add_items():
```

- **কী হচ্ছে:** `add_items` নামে একটি function তৈরি হলো। এর ভিতরের কাজ: ইনপুট নেওয়া ও CSV তে লেখা।
- **কেন function:** কাজগুলো আলাদা ভাগে রাখলে কোড পড়তে ও ঠিক করতে সহজ হয় (অধ্যায় ১ এর জ্ঞান)। সারাংশের কাজ আলাদা function এ রাখা হয়েছে।

### লাইন ৭: ফাইল আগে ছিল কিনা যাচাই

```python
    new_file = not os.path.exists(FILE)
```

- **কী হচ্ছে:** `os.path.exists(FILE)` ফাইল থাকলে `True`, না থাকলে `False` দেয়। সামনে `not` থাকায় ফলাফল উল্টে যায়। ফলে ফাইল **না থাকলে** `new_file` হবে `True`।
- **কেন:** কলামের নাম (header) শুধু প্রথমবার লিখতে হবে। প্রোগ্রাম বারবার চালালে header যেন বারবার না আসে।
- **গুরুত্বপূর্ণ:** এই যাচাই অবশ্যই ফাইল খোলার **আগে** করতে হবে। কারণ পরের লাইনে `"a"` mode এ খুললে ফাইলটি তৈরি হয়ে যায়।

### লাইন ৮: ফাইল append mode এ খোলা

```python
    with open(FILE, "a", newline="") as f:
```

- **কী হচ্ছে:** `fruits.csv` ফাইলটি খোলা হলো, আর এর নাম দেওয়া হলো `f`।
- **কেন `"a"` (append):** `"w"` mode দিলে প্রতিবার আগের সব ডাটা মুছে যেত। `"a"` আগের রেকর্ড রেখে শেষে নতুন রেকর্ড যোগ করে। ফাইল না থাকলে নতুন তৈরি করে।
- **কেন `newline=""`:** Windows এ এটা না দিলে প্রতিটি সারির পরে একটি ফাঁকা লাইন চলে আসে। `csv` module এর ডকুমেন্টেশনেও এটি দিতে বলা হয়েছে।
- **কেন `with`:** `with` ব্লক শেষ হলে ফাইল নিজে থেকেই বন্ধ (close) হয়ে যায়, এমনকি মাঝপথে error হলেও। এতে ডাটা নিরাপদে সংরক্ষিত হয়।

### লাইন ৯: CSV writer তৈরি

```python
        writer = csv.writer(f)
```

- **কী হচ্ছে:** খোলা ফাইলের জন্য একটি `writer` object তৈরি হলো।
- **কেন:** `writer.writerow()` দিয়ে একটি list দিলে সেটি কমা দিয়ে সঠিক CSV সারি বানিয়ে ফাইলে লেখে।

### লাইন ১০–১১: নতুন ফাইল হলে header লেখা

```python
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
```

- **কী হচ্ছে:** ফাইল নতুন হলে প্রথম সারিতে চারটি কলামের নাম লেখা হয়।
- **কেন:** header থাকলে Excel এ খুললে কলামের নাম দেখা যায়। পরে `DictReader` এই নামগুলো দিয়েই মান খুঁজবে।

### লাইন ১২: বারবার ইনপুট নেওয়ার লুপ

```python
        while True:
```

- **কী হচ্ছে:** একটি অসীম লুপ শুরু হলো।
- **কেন:** কতগুলো ফল দেওয়া হবে আগে থেকে জানা নেই। তাই ব্যবহারকারী `q` না লেখা পর্যন্ত লুপ চলবে। লুপ থেকে বের হওয়া হবে `break` দিয়ে।

### লাইন ১৩: ফলের নাম ইনপুট

```python
            name = input("Fruit name (q to quit): ").strip()
```

- **কী হচ্ছে:** `input()` কীবোর্ড থেকে লেখা নেয়। `.strip()` লেখার শুরু ও শেষের অতিরিক্ত স্পেস সরিয়ে দেয়।
- **কেন `.strip()`:** কেউ ভুলে `" Apple "` লিখলেও ফাইলে পরিষ্কার `Apple` যাবে।

### লাইন ১৪–১৫: `q` দিলে লুপ শেষ

```python
            if name.lower() == "q":
                break
```

- **কী হচ্ছে:** নাম `q` হলে `break` দিয়ে লুপ থেকে বের হওয়া হয়।
- **কেন `.lower()`:** লেখাটিকে ছোট হাতের করে তুলনা করা হয়। ফলে `Q` বা `q` দুটোতেই কাজ করে।

### লাইন ১৬–২১: দাম ও পরিমাণ নেওয়া, ভুল ইনপুট সামলানো

```python
            try:
                price = float(input("Unit price (Tk): "))
                qty = int(input("Quantity (kg): "))
            except ValueError:
                print("Invalid number! Try again.")
                continue
```

- **কী হচ্ছে:** `input()` সবসময় string দেয়। দামকে `float()` দিয়ে দশমিক সংখ্যায় আর পরিমাণকে `int()` দিয়ে পূর্ণসংখ্যায় রূপান্তর করা হয়।
- **কেন `float` ও `int`:** দামে দশমিক থাকতে পারে (যেমন 120.50), কিন্তু এখানে পরিমাণ পূর্ণ কেজিতে ধরা হয়েছে। string দিয়ে গুণ করা যায় না, তাই রূপান্তর লাগে।
- **কেন `try-except ValueError`:** কেউ সংখ্যার জায়গায় `abc` লিখলে `float()`/`int()` একটি `ValueError` দেয়। `try-except` না থাকলে প্রোগ্রাম সেখানেই বন্ধ হয়ে যেত। এখন একটি বার্তা দেখায় (অধ্যায় ৭: Exception Handling)।
- **কেন `continue`:** ভুল রেকর্ড ফাইলে না লিখে লুপের শুরুতে ফিরে যায় এবং আবার নাম চায়।

### লাইন ২২: মোট দাম হিসাব

```python
            total = price * qty
```

- **কী হচ্ছে:** একক দাম × পরিমাণ = মোট দাম।

### লাইন ২৩: একটি সারি CSV তে লেখা

```python
            writer.writerow([name, price, qty, total])
```

- **কী হচ্ছে:** চারটি মান একটি list আকারে দিয়ে ফাইলে এক সারিতে লেখা হয়। যেমন `Apple,250.0,5,1250.0`।
- **কেন list:** `writerow()` একটি list (বা tuple) চায়। list এর প্রতিটি উপাদান একটি কলাম হয়।

### লাইন ২৪: সংরক্ষণের নিশ্চয়তা দেখানো

```python
            print("Saved:", name, "| Total =", total, "Tk")
```

- **কী হচ্ছে:** ব্যবহারকারীকে জানানো হয় কোন ফল সংরক্ষিত হলো এবং তার মোট দাম কত।
- **কেন:** ফিডব্যাক পেলে ব্যবহারকারী বুঝতে পারে ইনপুট ঠিকভাবে গৃহীত হয়েছে। `print()` এ কমা দিয়ে একাধিক মান দিলে মাঝে নিজে থেকে স্পেস বসে।

### লাইন ২৬–২৯: সারাংশের function ও শুরুর মান

```python
def show_summary():
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
```

- **কী হচ্ছে:** সারাংশ দেখানোর আলাদা function শুরু। `"\n"` একটি ফাঁকা লাইন দিয়ে শিরোনাম ছাপে। দুটি যোগফলের ভেরিয়েবল `0` দিয়ে শুরু হয়।
- **কেন 0 দিয়ে শুরু:** লুপে প্রতিটি সারির মান এগুলোর সাথে যোগ হবে। শুরুর মান না দিলে যোগ করা যায় না (`NameError`)।

### লাইন ৩০–৩১: CSV ফাইল পড়ার জন্য খোলা

```python
    with open(FILE) as f:
        reader = csv.DictReader(f)
```

- **কী হচ্ছে:** ফাইলটি পড়ার জন্য খোলা হলো। mode না দিলে ডিফল্ট `"r"` (read)। `csv.DictReader` প্রতিটি সারিকে একটি **dictionary** বানায়, যেখানে key হলো header এর কলামের নাম।
- **কেন `DictReader` (`csv.reader` নয়):** `row['Fruit']` এভাবে নাম দিয়ে মান পাওয়া যায়, `row[0]` এর মতো নম্বর মনে রাখতে হয় না। কলামের ক্রম বদলালেও কোড ঠিক থাকে, আর কোড পড়তে সহজ হয়।

### লাইন ৩২–৩৩: প্রতিটি সারি সুন্দর করে ছাপা

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

### লাইন ৩৪–৩৫: যোগফল হিসাব

```python
            grand_total += float(row["Total Price"])
            total_qty += int(row["Quantity"])
```

- **কী হচ্ছে:** প্রতিটি সারির মোট দাম `grand_total` এ আর পরিমাণ `total_qty` তে যোগ হয়। `a += b` মানে `a = a + b`।
- **কেন `float()` ও `int()` আবার:** CSV ফাইল থেকে পড়া **সব মানই string** হিসেবে আসে (`"1250.0"`)। string যোগ করলে জোড়া লেগে যায় (`"1250.0" + "1200.0"` = `"1250.01200.0"`)। তাই আগে সংখ্যায় রূপান্তর করতে হয়।

### লাইন ৩৬–৩৮: সারাংশ ছাপা

```python
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")
```

- **কী হচ্ছে:** একটি বিভাজক রেখা, তারপর মোট পরিমাণ ও সর্বমোট দাম ছাপা হয়। লুপ শেষ হওয়ার পরে ছাপা হয় (indentation লক্ষ করুন), তাই একবারই আসে।

### লাইন ৪০–৪১: function দুটি চালানো

```python
add_items()
show_summary()
```

- **কী হচ্ছে:** function তৈরি করলেই তা চলে না, ডাকতে (call) হয়। আগে ইনপুট নেওয়া ও সংরক্ষণ, তারপর ফাইল থেকে পড়ে সারাংশ।
- **কেন এই ক্রম:** সারাংশ ফাইল থেকে পড়ে। তাই আগে ফাইলে লেখা শেষ হতে হবে (`add_items` এর `with` ব্লক শেষ হলে ফাইল বন্ধ ও সংরক্ষিত হয়)।

---

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** কাজগুলো তিন ভাগে ভাগ করা হয়েছে। **storage.py** শুধু CSV ফাইলে লেখা-পড়া করে, **report.py** শুধু সারাংশ ছাপে, আর **main.py** ব্যবহারকারীর সাথে কথা বলে (ইনপুট নেয়)। ফলে ফাইলের কাজ বদলাতে হলে শুধু storage.py খুলতে হয়।

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

### `fruit_inventory/__init__.py` — package এর দরজা

```python
"""fruit_inventory package: save fruit data in a CSV file and show a summary."""

from .storage import FILE, add_item, read_items
from .report import print_summary

__all__ = ["FILE", "add_item", "read_items", "print_summary"]
```

- এই ফাইল থাকায় `fruit_inventory` ফোল্ডারটি একটি **package** হয়।
- `from .storage import ...`: শুরুর **ডট (.)** মানে “এই package এর ভিতরের storage.py থেকে”। একে **relative import** বলে।
- এখানে import করে রাখায় বাইরের ফাইল সরাসরি `from fruit_inventory import add_item` লিখতে পারে, `fruit_inventory.storage` পর্যন্ত যেতে হয় না। এটাই package থেকে function **export** করা।
- `__all__` তালিকা বলে দেয় package থেকে কোন নামগুলো বাইরে ব্যবহারের জন্য দেওয়া হলো।

### `fruit_inventory/storage.py` — CSV লেখা ও পড়া

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
    """Read all fruits from the CSV file as a list of dictionaries."""
    with open(file) as f:
        return list(csv.DictReader(f))
```

- `add_item(name, price, qty, file=FILE)`: চারটি **parameter**। `file=FILE` হলো **default value**, না দিলে fruits.csv ধরে নেয়।
- function টি মোট দাম হিসাব করে, CSV তে লেখে এবং `return total` দিয়ে মোট দাম **ফেরত দেয়**। main.py সেই মান ছাপে।
- `read_items()` পুরো ফাইল পড়ে `list(csv.DictReader(f))` ফেরত দেয়: প্রতিটি সারি একটি dictionary।
- `"""..."""` হলো **docstring**: function কী করে তার বর্ণনা। `help(add_item)` দিলে এটি দেখা যায়।

### `fruit_inventory/report.py` — সারাংশ ছাপা

```python
def print_summary(items):
    """Print every fruit and the totals."""
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

- `print_summary(items)` ফাইল খোলে না। সে শুধু তাকে দেওয়া list ছাপে। তাই ডাটা যেখান থেকেই আসুক (CSV, ডাটাবেস), এই function একই থাকে।

### `main.py` — প্রোগ্রাম শুরু ও ইনপুট

```python
from fruit_inventory import add_item, read_items, print_summary


def take_input():
    """Take fruit data from the user until q is entered."""
    while True:
        name = input("Fruit name (q to quit): ").strip()
        if name.lower() == "q":
            break
        try:
            price = float(input("Unit price (Tk): "))
            qty = int(input("Quantity (kg): "))
        except ValueError:
            print("Invalid number! Try again.")
            continue
        total = add_item(name, price, qty)
        print("Saved:", name, "| Total =", total, "Tk")


if __name__ == "__main__":
    take_input()
    print_summary(read_items())
```

- `from fruit_inventory import add_item, read_items, print_summary`: package থেকে তিনটি function আনা (**import**)।
- `take_input()` শুধু ইনপুট নেয় ও ভুল ইনপুট সামলায়। সংরক্ষণের কাজ `add_item()` কে দিয়ে করায়।
- `if __name__ == "__main__":` ফাইলটি সরাসরি চালালে (`python main.py`) নিচের অংশ চলে। অন্য ফাইল এটিকে import করলে চলে না।
- `print_summary(read_items())`: আগে read_items() ডাটা ফেরত দেয়, সেটিই print_summary() এর argument হয়।

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job1_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: module import ও ফাইলের নাম | csv ও os module আনা এবং ফাইলের নাম ঠিক করা। |
| Cell 2: function ১: add_items() তৈরি | ইনপুট নিয়ে CSV তে লেখার function। এই cell চালালে কিছু দেখাবে না, শুধু function তৈরি হবে। |
| Cell 3: function ২: show_summary() তৈরি | CSV পড়ে সারাংশ দেখানোর function। এটিও শুধু তৈরি হবে। |
| Cell 4: function দুটি চালানো | এখন ইনপুট চাইবে। শেষে q দিলে সারাংশ দেখাবে। |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট (পরীক্ষিত)

```
Fruit name (q to quit): Apple
Unit price (Tk): 250
Quantity (kg): 5
Saved: Apple | Total = 1250.0 Tk
Fruit name (q to quit): Mango
Unit price (Tk): 120
Quantity (kg): abc
Invalid number! Try again.
Fruit name (q to quit): Mango
Unit price (Tk): 120
Quantity (kg): 10
Saved: Mango | Total = 1200.0 Tk
Fruit name (q to quit): Banana
Unit price (Tk): 60
Quantity (kg): 12
Saved: Banana | Total = 720.0 Tk
Fruit name (q to quit): q

------ Fruit Inventory Summary ------
Apple         250.0 x   5 =   1250.0 Tk
Mango         120.0 x  10 =   1200.0 Tk
Banana         60.0 x  12 =    720.0 Tk
-------------------------------------
Total quantity : 27 kg
Grand total    : 3170.0 Tk
```

তৈরি হওয়া `fruits.csv`:

```
Fruit,Unit Price,Quantity,Total Price
Apple,250.0,5,1250.0
Mango,120.0,10,1200.0
Banana,60.0,12,720.0
```

> লক্ষ করুন: ভুল ইনপুট `abc` ফাইলে যায়নি। আবার চালালে নতুন ফল আগের রেকর্ডগুলোর নিচে যোগ হবে, এবং সারাংশে সব রেকর্ড আসবে।

## অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] **১.** `1_single_file` এর প্রোগ্রাম চালিয়ে নমুনা আউটপুটের সাথে মিলিয়ে দেখুন।
- [ ] **২.** `2_modular` এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই আসছে কিনা দেখুন।
- [ ] **৩.** module সংস্করণে প্রতিটি ফাইল খুলে বলুন কোন function কোন ফাইলে আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] **৪.** Colab এ notebook আপলোড করে একটি একটি cell চালান। প্রতিটি cell এর পরে কী পরিবর্তন হলো খেয়াল করুন।
- [ ] **৫.** "বাড়তি কাজ" থেকে একটি কাজ বেছে নিন। module সংস্করণে নতুন function টি সঠিক module এ যোগ করুন এবং `__init__.py` থেকে export করুন।

## সমস্যা ও সমাধান

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `PermissionError` | `fruits.csv` Excel এ খোলা আছে। Excel বন্ধ করে আবার চালান। |
| প্রতি সারির পরে ফাঁকা লাইন | `open()` এ `newline=""` দেওয়া হয়নি। |
| সারাংশে `ValueError` | কেউ হাতে CSV এডিট করে ভুল মান রেখেছে। ফাইল মুছে আবার চালান। |
| শুরু থেকে নতুন করে চাই | `fruits.csv` ফাইলটি মুছে দিন। |

## বাড়তি কাজ (অনুশীলন)

1. নাম দিয়ে একটি ফল খুঁজে তার তথ্য দেখান।
2. সবচেয়ে দামি ফল (সবচেয়ে বেশি Unit Price) বের করুন।
3. একই ফল আবার দিলে নতুন সারি না করে পরিমাণ যোগ করুন।

## ভাইভা প্রশ্ন ও উত্তর

1. **CSV এর পূর্ণরূপ কী?** Comma Separated Values।
2. **`"a"` mode কেন ব্যবহার করা হয়েছে?** আগের রেকর্ড না মুছে নতুন রেকর্ড শেষে যোগ করার জন্য। `"w"` দিলে আগের সব মুছে যেত।
3. **`newline=""` কেন দেওয়া হয়?** Windows এ CSV এর প্রতি সারির পরে অতিরিক্ত ফাঁকা লাইন আসা ঠেকাতে।
4. **`with open()` এর সুবিধা কী?** ব্লক শেষে ফাইল নিজে থেকেই বন্ধ হয়, error হলেও।
5. **`DictReader` ও `reader` এর পার্থক্য কী?** `reader` প্রতিটি সারি list দেয় (নম্বর দিয়ে মান নিতে হয়)। `DictReader` dictionary দেয় (কলামের নাম দিয়ে মান নেওয়া যায়)।
6. **CSV থেকে পড়া মান যোগ করার আগে `float()` কেন লাগে?** CSV থেকে সব মান string হিসেবে আসে। string যোগ করলে জোড়া লাগে, গাণিতিক যোগ হয় না।
7. **`try-except ValueError` না থাকলে কী হতো?** সংখ্যার জায়গায় অক্ষর দিলে প্রোগ্রাম error দিয়ে বন্ধ হয়ে যেত।
8. **`break` ও `continue` এর পার্থক্য কী?** `break` লুপ পুরোপুরি শেষ করে। `continue` বর্তমান ঘুরের বাকি অংশ বাদ দিয়ে লুপের শুরুতে ফিরে যায়।

**Module / Package সংক্রান্ত:**

- **module ও package এর পার্থক্য কী?** module একটি `.py` ফাইল। package হলো `__init__.py` সহ কয়েকটি module এর ফোল্ডার।
- **`__init__.py` এর কাজ কী?** ফোল্ডারটিকে package বানায়, এবং ভিতরের function গুলো import করে বাইরে ব্যবহারের জন্য (export) দেয়।
- **`from .storage import add_item` এ ডট (.) কেন?** একই package এর ভিতরের module থেকে আনার জন্য (relative import)।
- **`if __name__ == "__main__":` কেন লেখা হয়?** ফাইলটি সরাসরি চালালে তবেই নিচের কোড চলে, অন্য ফাইল import করলে চলে না।
- **module এ ভাগ করার সুবিধা কী?** কোড পড়া, পরিবর্তন করা, পুনর্ব্যবহার ও পরীক্ষা সহজ হয়।
