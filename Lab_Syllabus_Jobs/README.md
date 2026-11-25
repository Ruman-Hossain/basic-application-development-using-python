# 28531 Application Development Using Python — ব্যবহারিক (৬টি জব)

**৩য় পর্ব, Computer Science & Technology** · BTEB Probidhan-2022
পাবনা সরকারি পলিটেকনিক ইনস্টিটিউট
প্রস্তুতকারী: মোঃ রুমান হোসেন, ইন্সট্রাক্টর (CST)

মোট ১৬ ক্লাস (৩ পিরিয়ড) · Continuous ২৫ নম্বর

---

## প্রতিটি জবের তিন ধরনের সমাধান

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ, `import`, package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook, কোড আলাদা আলাদা cell এ | ব্রাউজারে |

তিনটিই একই কাজ করে এবং একই আউটপুট দেয় (পরীক্ষিত)। শুরু করুন সমাধান ১ দিয়ে, তারপর সমাধান ২ এ দেখুন একই কোড কীভাবে module এ ভাগ করা যায়।

## ফোল্ডারের গঠন

```
Lab_Syllabus_Jobs/
├── README.md                  ← এই ফাইল (setup গাইড)
├── docs/28531_Python_Jobs_Easy_Guide.pdf  ← সব এক PDF এ
├── requirements.txt           ← সব জবের package একসাথে
├── Job1_Fruit_Inventory/
│   ├── README.md              ← তিন সমাধানের বাংলা ব্যাখ্যা
│   ├── requirements.txt
│   ├── 1_single_file/
│   │   └── p1_inventory.py
│   ├── 2_modular/
│   │   ├── main.py            ← এটি চালাবেন
│   │   └── fruit_inventory/   ← package
│   │       ├── __init__.py
│   │       ├── report.py
│   │       └── storage.py
│   └── 3_colab/
│       └── Job1_colab.ipynb
├── Job2_PDF_Report/           (একই গঠন, package: report_tools)
├── Job3_QR_Barcode/           (package: codes)
├── Job4_Web_Scraping/         (package: scraper)
├── Job5_Weather_Report/       (package: weather)
└── Job6_Database_App/         (package: student_db; 3_colab এ মেনু সংস্করণ)
```

## Module ও Package: মূল ধারণা (অধ্যায় ৩)

| শব্দ | মানে |
|---|---|
| module | একটি `.py` ফাইল। যেমন `storage.py`। |
| package | কয়েকটি module সহ একটি ফোল্ডার, যার ভিতরে `__init__.py` আছে। |
| import | অন্য module/package থেকে function বা ভেরিয়েবল আনা: `from package import function`। |
| export | package এর `__init__.py` তে import করে রাখা, যাতে বাইরে থেকে সহজে নেওয়া যায়। `__all__` তালিকায় নামগুলো লেখা থাকে। |
| relative import | `from .storage import ...`: ডট (.) মানে একই package এর ভিতরের ফাইল। |
| `if __name__ == "__main__":` | ফাইলটি সরাসরি চালালে (`python main.py`) নিচের কোড চলে। import করলে চলে না। |
| return | function এর ফলাফল ডাকার জায়গায় ফেরত পাঠানো। একাধিক মান ফেরত দিলে tuple হয়। |

## ৬টি জব এক নজরে

| জব | কী বানাব | লাইব্রেরি | ক্লাস | নম্বর | ইন্টারনেট |
|---|---|---|---|---|---|
| ১ Fruit Inventory | ইনপুট নিয়ে CSV তে সংরক্ষণ ও সারাংশ | csv, os (built-in) | ৩ | ৪ | লাগে না |
| ২ PDF Report | CSV থেকে ছাত্রদের তথ্যের PDF | csv, **fpdf2** | ৩ | ৪ | শুধু install এ |
| ৩ QR ও Barcode | তৈরি ও decode | **qrcode, python-barcode, pyzbar, Pillow** | ২ | ৪ | শুধু install এ |
| ৪ Web Scraping | ওয়েবসাইট থেকে বইয়ের তথ্য CSV তে | **requests, beautifulsoup4** | ৩ | ৪ | লাগবে |
| ৫ Weather Report | OpenWeather API থেকে আবহাওয়া | **requests** | ২ | ৪ | লাগবে + API key |
| ৬ Database App | ফর্ম দিয়ে Save ও Search | tkinter, sqlite3 (built-in) | ৩ | ৫ | লাগে না |

---

## কেন virtual environment (venv)

package সরাসরি সিস্টেমের মূল Python এ (global) install করলে কয়েকটি সমস্যা হয়:

- বিভিন্ন প্রজেক্টের আলাদা version লাগলে একটি অন্যটিকে নষ্ট করে।
- কোন প্রজেক্টে কোন package লাগে তা বোঝা যায় না।
- ল্যাবের শেয়ার করা কম্পিউটারে অন্যের কাজে সমস্যা হয়।

**Virtual environment** হলো প্রতিটি প্রজেক্টের জন্য একটি **আলাদা, নিজস্ব Python** (`venv` নামের ফোল্ডার)। এর ভিতরে install করা package শুধু সেই প্রজেক্টেই থাকে। কাজ শেষে ফোল্ডারটি মুছে দিলেই সব পরিষ্কার হয়ে যায়।

**`requirements.txt`** হলো প্রজেক্টের প্রয়োজনীয় package এর তালিকা। একটি কমান্ডেই সব install হয়, আর অন্য কম্পিউটারেও হুবহু একই পরিবেশ তৈরি করা যায়। এটি পেশাদার Python ডেভেলপারদের সাধারণ নিয়ম।

---

## পদ্ধতি ১: লোকাল কম্পিউটারে চালানো

### ধাপ ১: Python ইনস্টল (একবারই)

1. https://www.python.org/downloads/ থেকে Python 3.9 বা নতুন version ডাউনলোড করুন।
2. installer এর **প্রথম পাতায় নিচের "Add python.exe to PATH" অবশ্যই টিক দিন।**
3. **Install Now** চাপুন।
4. যাচাই: CMD খুলে লিখুন `python --version`। version নম্বর দেখালে ঠিক আছে।

সাথে **VS Code** (code.visualstudio.com) ও তার **Python extension** ইনস্টল করুন।

### ধাপ ২: জবের ফোল্ডারে যাওয়া

পুরো `28531_Python_Jobs` ফোল্ডারটি কম্পিউটারে কপি করুন। VS Code এ **File → Open Folder** দিয়ে একটি জবের ফোল্ডার (যেমন `Job2_PDF_Report`) খুলুন। তারপর **Terminal → New Terminal** দিন।

অথবা CMD তে:
```bash
cd D:\Python_Lab\28531_Python_Jobs\Job2_PDF_Report
```

### ধাপ ৩: virtual environment তৈরি (প্রতি জবে একবার)

```bash
python -m venv venv
```

- `python -m venv` মানে Python এর built-in `venv` module চালাও।
- শেষের `venv` হলো নতুন environment ফোল্ডারের নাম।
- এতে জবের ফোল্ডারের ভিতরে `venv/` নামে একটি ফোল্ডার তৈরি হবে।

### ধাপ ৪: environment চালু (activate) করা

প্রতিবার নতুন terminal খুললে এটি করতে হবে।

| সিস্টেম | কমান্ড |
|---|---|
| Windows (CMD) | `venv\Scripts\activate` |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| Linux / Mac | `source venv/bin/activate` |

সফল হলে terminal এর লাইনের শুরুতে **`(venv)`** দেখা যাবে। এর মানে এখন যা install হবে তা শুধু এই প্রজেক্টে থাকবে।

> **PowerShell এ "running scripts is disabled" error এলে** একবার এটি চালান:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
> অথবা VS Code এর terminal কে CMD এ বদলে নিন।

### ধাপ ৫: package install

```bash
pip install -r requirements.txt
```

- `-r` মানে ফাইল থেকে তালিকা পড়ো (read)।
- যাচাই করতে: `pip list` দিলে install হওয়া package গুলো দেখা যাবে।

### ধাপ ৬: প্রোগ্রাম চালানো

environment জবের ফোল্ডারে (যেমন `Job2_PDF_Report`) চালু থাকা অবস্থায়:

সমাধান ১ (single file):
```bash
cd 1_single_file
python p2_pdf_report.py
```

সমাধান ২ (module/package):
```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python package খুঁজে পায়।

অথবা VS Code এ ফাইলটি খুলে উপরে ডানে ▶ (Run) চাপুন। নিচের ডান কোণে Python version এ `('venv': venv)` বেছে নেওয়া আছে কিনা দেখে নিন। না থাকলে **Ctrl+Shift+P → Python: Select Interpreter** থেকে `venv` টি বেছে নিন।

### ধাপ ৭: কাজ শেষে

```bash
deactivate
```

environment বন্ধ হবে। পরের বার শুধু ধাপ ৪ (activate) ও ধাপ ৬ (চালানো) করলেই হবে। environment পুরো মুছে নতুন করে চাইলে `venv` ফোল্ডারটি মুছে ধাপ ৩ থেকে শুরু করুন।

### সংক্ষেপে (Windows CMD)

```bash
cd Job2_PDF_Report
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd 1_single_file
python p2_pdf_report.py
cd ../2_modular
python main.py
deactivate
```

> **সব জবের জন্য একটি environment চাইলে:** মূল ফোল্ডার `28531_Python_Jobs` এ একবার environment তৈরি করে `pip install -r requirements.txt` দিন। মূল ফোল্ডারের `requirements.txt` এ সব জবের package একসাথে আছে। তবে প্রতি জবে আলাদা environment রাখাই শেখার জন্য ভালো অভ্যাস।

---

## পদ্ধতি ২: Google Colab এ চালানো

Google Colab হলো ব্রাউজারে চলা ফ্রি Python পরিবেশ। প্রতিটি notebook Google এর সার্ভারে **নিজস্ব আলাদা মেশিনে** চলে। তাই এখানে package install করলে তা ওই notebook এর ভিতরেই সীমিত থাকে, আলাদা venv লাগে না।

1. https://colab.research.google.com খুলুন এবং Google একাউন্টে লগইন করুন।
2. **File → Upload notebook** থেকে জবের `3_colab` ফোল্ডারের `JobN_colab.ipynb` আপলোড করুন।
3. উপর থেকে একটি একটি করে cell চালান (**Shift + Enter**)।
   - কোড **আলাদা আলাদা cell** এ ভাগ করা আছে: প্রথমে package install, তারপর module import, প্রতিটি function আলাদা cell এ, শেষে চালানোর cell।
   - function তৈরির cell চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
   - সব cell একই memory শেয়ার করে, তাই **উপর থেকে ক্রমানুসারে** চালাতে হবে। অথবা **Runtime → Run all** দিন।
   - `NameError` দেখালে বুঝবেন আগের কোনো cell চালানো হয়নি।
   - ইনপুটের বক্স এলে মান লিখে Enter চাপুন।
4. তৈরি হওয়া ফাইল (CSV, PDF, PNG) বাম পাশের **📁 Files** প্যানেলে পাওয়া যাবে। ডাউনলোড করতে ফাইলের পাশের ⋮ চাপুন।

**Colab এর সীমাবদ্ধতা:**

| বিষয় | ব্যাখ্যা |
|---|---|
| **জব ৬ এর GUI** | Colab এ কোনো স্ক্রিন নেই, তাই tkinter window খোলে না। Colab এর জন্য একই ডাটাবেসের মেনু-ভিত্তিক `p6_console_colab.py` দেওয়া আছে। GUI দেখাতে লোকাল কম্পিউটার ব্যবহার করুন। |
| **ফাইল মুছে যায়** | session শেষ হলে (কিছুক্ষণ নিষ্ক্রিয় থাকলে) সব তৈরি ফাইল মুছে যায়। দরকারি ফাইল ডাউনলোড করে রাখুন। |
| **জব ৩** | notebook নিজেই `libzbar0` install করে নেয়। |
| **জব ৫** | কোডের cell এ নিজের API key বসাতে হবে। |

---

## সাধারণ সমস্যা ও সমাধান

| সমস্যা | সমাধান |
|---|---|
| `'python' is not recognized` | Python install এর সময় "Add to PATH" টিক দেওয়া হয়নি। আবার installer চালিয়ে **Modify** দিয়ে ঠিক করুন, অথবা `py` লিখে দেখুন (`py -m venv venv`)। |
| `ModuleNotFoundError` | environment activate নেই (শুরুতে `(venv)` দেখা যাচ্ছে না), বা install হয়নি। activate করে `pip install -r requirements.txt` দিন। |
| VS Code এ ▶ চাপলে `ModuleNotFoundError`, কিন্তু terminal এ চলে | VS Code ভুল interpreter ব্যবহার করছে। **Python: Select Interpreter** থেকে `venv` বেছে নিন। |
| `pip` খুব ধীর বা ব্যর্থ | ইন্টারনেট সংযোগ দেখুন। ল্যাবে আগেই install করে রাখুন। |
| Linux এ `venv` তৈরি হয় না | `sudo apt install python3-venv` দিন। |

## জব রিপোর্টে যা থাকবে

১. জবের নাম ও উদ্দেশ্য · ২. প্রয়োজনীয় সফটওয়্যার/লাইব্রেরি · ৩. অ্যালগরিদম/ফ্লোচার্ট · ৪. কোড · ৫. ইনপুট-আউটপুটের স্ক্রিনশট · ৬. তৈরি হওয়া ফাইল · ৭. সমস্যা ও সমাধান · ৮. উপসংহার

## মূল্যায়ন চেকলিস্ট

- [ ] কোড ত্রুটি ছাড়া চলে
- [ ] ভুল ইনপুট সামলায়
- [ ] ফাইল/আউটপুট সঠিক
- [ ] প্রতিটি লাইনের কাজ ব্যাখ্যা করতে পারে
- [ ] জব রিপোর্ট সম্পূর্ণ

## রেফারেন্স

- Python: https://docs.python.org/3/
- venv: https://docs.python.org/3/library/venv.html
- fpdf2: https://py-pdf.github.io/fpdf2/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- OpenWeather API: https://openweathermap.org/current
- sqlite3: https://docs.python.org/3/library/sqlite3.html
- tkinter: https://docs.python.org/3/library/tkinter.html
