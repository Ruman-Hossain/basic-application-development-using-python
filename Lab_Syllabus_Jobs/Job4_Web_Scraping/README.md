# জব ৪: Web Scraping

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ৩ | **নম্বর:** ৪

## উদ্দেশ্য

একটি অনলাইন বইয়ের দোকানের ওয়েবপেজ থেকে HTML সোর্স কোড এনে প্রতিটি বইয়ের নাম, দাম, রেটিং ও স্টক বের করা হবে। তারপর সেগুলো `books.csv` ফাইলে সংরক্ষণ করা হবে।

সিলেবাসের ধাপ: 4.1 Setup → 4.2 Get HTML source → 4.3 Extract data → 4.4 Save into CSV

## অনুশীলনের সাইট কেন books.toscrape.com

- সিলেবাসে rokomari.com এর উদাহরণ আছে। rokomari এর পেজের গঠন প্রায়ই বদলায় এবং তাদের ব্যবহারের শর্ত মানতে হয়।
- **books.toscrape.com** একটি নকল বইয়ের দোকান, যা শুধু scraping শেখার জন্যই তৈরি। এখানে অনুশীলন সম্পূর্ণ বৈধ এবং গঠন বদলায় না।
- একই কৌশলে অন্য সাইটেও কাজ হবে, শুধু tag ও class এর নাম (selector) Inspect করে বদলাতে হবে।

**নৈতিকতা:** কোনো সাইট scrape করার আগে তার `robots.txt` ও ব্যবহারের শর্ত দেখুন। অল্প সময়ে অনেক request পাঠাবেন না।

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

### ফোল্ডারের গঠন

```
Job4_Web_Scraping/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p4_scraping.py
├── 2_modular/
│   ├── main.py
│   └── scraper/
│       ├── __init__.py
│       ├── fetch.py
│       ├── parser.py
│       └── storage.py
└── 3_colab/
    └── Job4_colab.ipynb
```

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job4_Web_Scraping` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p4_scraping.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `scraper` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job4_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

### এই জবের বিশেষ নোট

> **ইন্টারনেট সংযোগ লাগবে** (তিন সমাধানেই)।

কাজ শেষে Terminal এ `deactivate`।

## ধাপ ০: Inspect দিয়ে HTML গঠন বোঝা (কোড লেখার আগে)

ব্রাউজারে https://books.toscrape.com খুলে যেকোনো বইয়ের উপর **Right click → Inspect** করুন। দেখবেন প্রতিটি বই এরকম একটি ব্লকের ভিতরে আছে:

```html
<article class="product_pod">
  <p class="star-rating Three"></p>
  <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
  <p class="price_color">£51.77</p>
  <p class="instock availability">In stock</p>
</article>
```

কোড লেখা হয়েছে এই গঠন দেখে:
- প্রতিটি বই একটি `<article class="product_pod">` এর ভিতরে।
- নাম `<a>` ট্যাগের লেখায় **কাটা** ("A Light in the ..."), কিন্তু **`title` attribute এ পূর্ণ নাম** আছে।
- দাম `price_color` class এ।
- রেটিং লেখা হিসেবে নেই, আছে **class এর নামে** (`star-rating Three`)।

---

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে)

### লাইন ১–৩: module আনা

```python
import csv
import requests
from bs4 import BeautifulSoup
```

- **`csv`:** শেষে ফলাফল CSV তে লেখার জন্য (built-in)।
- **`requests`:** ইন্টারনেট থেকে ওয়েবপেজ আনার জন্য। এটি ব্রাউজারের মতো সার্ভারে request পাঠায় এবং HTML ফেরত আনে। Python এর built-in `urllib` এর চেয়ে এটি অনেক সহজ।
- **`BeautifulSoup`:** HTML লেখাকে খোঁজার উপযোগী গঠনে (tree) রূপান্তর করে, যাতে ট্যাগ ও class দিয়ে তথ্য খুঁজে নেওয়া যায়। package এর নাম `beautifulsoup4`, কিন্তু import এর নাম `bs4`।
- **দুটি লাইব্রেরি কেন:** `requests` শুধু HTML **আনে**। `BeautifulSoup` সেই HTML থেকে তথ্য **খোঁজে**। কাজ ভাগ করা আছে।

### লাইন ৫: ওয়েবসাইটের ঠিকানা

```python
url = "https://books.toscrape.com/"
```

- **কী হচ্ছে:** যে পেজ থেকে তথ্য নেওয়া হবে তার URL একটি ভেরিয়েবলে রাখা হলো, যাতে পরে সহজে বদলানো যায়।

### লাইন ৮: HTML সোর্স আনা

```python
response = requests.get(url, timeout=10)
```

- **কী হচ্ছে:** `requests.get()` সার্ভারে একটি **GET request** পাঠায় (ব্রাউজারে ঠিকানা লিখে Enter চাপার মতো)। সার্ভারের উত্তর `response` object এ আসে।
- **কেন `timeout=10`:** সার্ভার উত্তর না দিলে প্রোগ্রাম চিরকাল অপেক্ষা করবে না, ১০ সেকেন্ড পরে error দিয়ে থামবে।

### লাইন ৯: encoding ঠিক করা

```python
response.encoding = "utf-8"
```

- **কী হচ্ছে:** পেজের লেখা UTF-8 হিসেবে পড়তে বলা হলো।
- **কেন:** এই সাইটের সার্ভার encoding ঠিকভাবে জানায় না। তখন requests ভুল encoding ধরে নেয় এবং `£` চিহ্ন ভেঙে `Â£` দেখায়। UTF-8 বলে দিলে সঠিক দেখায়।

### লাইন ১০: status code দেখা

```python
print("Status code:", response.status_code)
```

- **কী হচ্ছে:** সার্ভারের উত্তরের ধরন বোঝার সংখ্যা ছাপা হয়।
- **কেন:** `200` মানে সফল। `404` মানে পেজ নেই, `403` মানে প্রবেশ নিষেধ, `500` মানে সার্ভারের সমস্যা। ফলাফল খালি এলে প্রথমেই এটি দেখতে হয়।

### লাইন ১৩: HTML পার্স করা

```python
soup = BeautifulSoup(response.text, "html.parser")
```

- **কী হচ্ছে:** `response.text` হলো পুরো HTML একটি লম্বা string আকারে। BeautifulSoup সেটিকে ট্যাগের গাছে (tree) সাজিয়ে `soup` object বানায়।
- **কেন `"html.parser"`:** এটি Python এর সাথে আসা parser, আলাদা install লাগে না। (`lxml` আরও দ্রুত, কিন্তু আলাদা install লাগে।)

### লাইন ১৪–১৫: সব বই খুঁজে বের করা

```python
books = soup.find_all("article", class_="product_pod")
print("Books found on this page:", len(books))
```

- **`find_all(ট্যাগ, class_=...)`:** যে সব `<article>` ট্যাগের class `product_pod`, সবগুলো একটি list হিসেবে দেয়। প্রতিটি উপাদান একটি বইয়ের পুরো ব্লক।
- **কেন `class_` (শেষে আন্ডারস্কোর):** `class` Python এর সংরক্ষিত শব্দ (keyword), class তৈরিতে ব্যবহৃত হয়। তাই BeautifulSoup `class_` লিখতে বলে।
- **কেন `len(books)` ছাপা:** কতগুলো বই পাওয়া গেল তা দেখে নিশ্চিত হওয়া যায় যে খোঁজা ঠিক কাজ করছে। এই সাইটে প্রতি পেজে ২০টি বই।

### লাইন ১৮–২৪: প্রতিটি বই থেকে তথ্য বের করা

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

### লাইন ২৬–২৭: প্রথম ৪টি দেখানো

```python
for r in rows[:4]:
    print(r)
```

- **কী হচ্ছে:** `rows[:4]` slicing, শুধু প্রথম ৪টি বই (index 0 থেকে 3)।
- **কেন সব নয়:** ২০টি ছাপলে স্ক্রিন ভরে যায়। কয়েকটি দেখে নিশ্চিত হওয়াই যথেষ্ট, সব তথ্য CSV তে যাবে।

### লাইন ৩০–৩৪: CSV ফাইলে সংরক্ষণ

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

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** scraping এর তিনটি ধাপ তিনটি module এ: **fetch.py** পেজ আনে, **parser.py** তথ্য খোঁজে, **storage.py** CSV তে রাখে। সাইটের গঠন বদলালে শুধু parser.py বদলাতে হবে।

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

### `scraper/__init__.py` — package এর দরজা

```python
"""scraper package: download a web page, find the books and save them to CSV."""

from .fetch import get_html
from .parser import parse_books
from .storage import save_csv

__all__ = ["get_html", "parse_books", "save_csv"]
```

- তিনটি module এর function export করে: `get_html`, `parse_books`, `save_csv`।

### `scraper/fetch.py` — পেজ আনা

```python
import requests


def get_html(url):
    """Download a web page and return (status_code, html_text)."""
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8"
    return response.status_code, response.text
```

- `get_html(url)` দুটি মান ফেরত দেয়: `(status_code, html_text)`। main.py দুটিই ব্যবহার করে।

### `scraper/parser.py` — HTML থেকে বইয়ের তথ্য

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

### `scraper/storage.py` — CSV তে সংরক্ষণ

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

### `main.py` — ধাপগুলো ক্রমানুসারে চালানো

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

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job4_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: package install |  |
| Cell 2: module import ও URL | requests, BeautifulSoup ও csv আনা। |
| Cell 3: ধাপ ১: HTML সোর্স আনা | Status code 200 এলে সফল। |
| Cell 4: ধাপ ২: HTML পার্স করে বই খোঁজা | কতগুলো বই পাওয়া গেল দেখাবে। |
| Cell 5: ধাপ ৩: প্রতিটি বই থেকে তথ্য বের করা | rows list এ জমা হবে। |
| Cell 6: প্রথম ৪টি বই দেখা |  |
| Cell 7: ধাপ ৪: CSV তে সংরক্ষণ | books.csv তৈরি হবে। |
| Cell 8: books.csv দেখা |  |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট

**ইনপুট:** কীবোর্ড ইনপুট নেই। ইনপুট হলো `url` (books.toscrape.com এর প্রথম পেজ)।

```
Status code: 200
Books found on this page: 20
['A Light in the Attic', '£51.77', 'Three', 'In stock']
['Tipping the Velvet', '£53.74', 'One', 'In stock']
['Soumission', '£50.10', 'One', 'In stock']
['Sharp Objects', '£47.82', 'Four', 'In stock']
Saved 20 books to books.csv
```

`books.csv` এর শুরু:

```
Book Name,Price,Rating,Availability
A Light in the Attic,£51.77,Three,In stock
Tipping the Velvet,£53.74,One,In stock
Soumission,£50.10,One,In stock
Sharp Objects,£47.82,Four,In stock
```

> **Excel এ খোলার টিপ:** Excel এ সরাসরি খুললে `£` চিহ্ন ভেঙে যেতে পারে। Excel এ **Data → From Text/CSV** দিয়ে UTF-8 বেছে খুলুন। অথবা কোডে `encoding="utf-8-sig"` দিন।

## অনুশীলনের ধাপ (নিজে নিজে করুন)

- [ ] **১.** `1_single_file` এর প্রোগ্রাম চালিয়ে নমুনা আউটপুটের সাথে মিলিয়ে দেখুন।
- [ ] **২.** `2_modular` এর `main.py` চালান। আউটপুট সমাধান ১ এর মতোই আসছে কিনা দেখুন।
- [ ] **৩.** module সংস্করণে প্রতিটি ফাইল খুলে বলুন কোন function কোন ফাইলে আছে, আর `main.py` কোথা থেকে কী import করছে।
- [ ] **৪.** Colab এ notebook আপলোড করে একটি একটি cell চালান। প্রতিটি cell এর পরে কী পরিবর্তন হলো খেয়াল করুন।
- [ ] **৫.** "বাড়তি কাজ" থেকে একটি কাজ বেছে নিন। module সংস্করণে নতুন function টি সঠিক module এ যোগ করুন এবং `__init__.py` থেকে export করুন।

## সমস্যা ও সমাধান

| সমস্যা | কারণ ও সমাধান |
|---|---|
| `ConnectionError` | ইন্টারনেট নেই বা সাইট বন্ধ। সংযোগ দেখুন। |
| `ReadTimeout` | সার্ভার ১০ সেকেন্ডে উত্তর দেয়নি। আবার চালান। |
| `Books found on this page: 0` | tag বা class এর নাম ভুল, বা সাইটের গঠন বদলেছে। Inspect করে মিলিয়ে নিন। |
| `'NoneType' object is not subscriptable` বা `has no attribute` | `find()` কিছু পায়নি এবং `None` দিয়েছে। class এর বানান মিলিয়ে নিন। |
| দামে `Â£` দেখায় | `response.encoding = "utf-8"` লাইনটি বাদ পড়েছে। |

## বাড়তি কাজ (অনুশীলন)

1. সব ৫০টি পেজ থেকে মোট ১০০০ বই সংগ্রহ করুন। পেজের ঠিকানা `https://books.toscrape.com/catalogue/page-2.html` এভাবে বদলায়। লুপে `page-1` থেকে `page-50` পর্যন্ত চালান, এবং প্রতি request এর মাঝে `time.sleep(1)` দিন।
2. দাম থেকে `£` বাদ দিয়ে `float` বানিয়ে সবচেয়ে সস্তা ৫টি বই দেখান।
3. রেটিং `"Three"` কে সংখ্যা `3` এ রূপান্তর করুন (dictionary ব্যবহার করে)।

## ভাইভা প্রশ্ন ও উত্তর

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
