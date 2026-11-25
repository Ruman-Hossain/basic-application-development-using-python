# 28531 — Application Development Using Python

**৩য় পর্ব, Computer Science & Technology (CST)** · BTEB Diploma in Engineering, Probidhan-2022
পাবনা সরকারি পলিটেকনিক ইনস্টিটিউট

প্রস্তুতকারী: **Md Ruman Hossain** (মোঃ রুমান হোসেন), Instructor (CST)

| অংশ | ক্লাস | নম্বর |
|---|---|---|
| Theory (১১টি অধ্যায়) | ৩২ | ৬০ |
| Practical (৬টি জব) | ১৬ (৩ পিরিয়ড) | ২৫ (Continuous) |

---

## সূচি

1. [Repository এর গঠন](#repository-এর-গঠন)
2. [Theory: অধ্যায়ভিত্তিক স্লাইড](#theory-অধ্যায়ভিত্তিক-স্লাইড)
3. [Lab: ৬টি জব, প্রতিটির ৪ ধরনের সমাধান](#lab-৬টি-জব-প্রতিটির-৪-ধরনের-সমাধান)
4. [কোথা থেকে শুরু করবেন](#কোথা-থেকে-শুরু-করবেন)

---

## Repository এর গঠন

```
basic-application-development-using-python/
├── README.md                 ← এই ফাইল (সূচি)
├── Theory/                   ← অধ্যায় ১–১১ এর স্লাইড (PDF ও PPTX)
├── Lab_Book/                 ← সমাধান ১: বই অনুযায়ী (Jupyter notebook + module প্রজেক্ট)
└── Lab_Syllabus_Jobs/        ← সমাধান ২, ৩, ৪: সিলেবাস অনুযায়ী সহজ পদ্ধতি
    ├── README.md             ← virtual environment সহ পূর্ণ setup গাইড
    ├── docs/                 ← Easy Guide: README (GitHub এ পড়ার জন্য) + PDF (প্রিন্ট/অফলাইন)
    └── Job1 … Job6/          ← প্রতিটিতে 1_single_file, 2_modular, 3_colab, README.md
```

---

## Theory: অধ্যায়ভিত্তিক স্লাইড

| অধ্যায় | বিষয় | ক্লাস/নম্বর | PDF | Slide (PPTX) |
|---|---|---|---|---|
| ০১ | Python Functions | ৪ / ৬ | [PDF](Theory/28531-Ch01-Python-Functions.pdf) | [PPTX](Theory/28531-Ch01-Python-Functions.pptx) |
| ০২ | File Operation in Python | ২ / ৪ | [PDF](Theory/28531-Ch02-File-Operation-in-Python.pdf) | [PPTX](Theory/28531-Ch02-File-Operation-in-Python.pptx) |
| ০৩ | Module, Package & Application Software | ২ / ৪ | [PDF](Theory/28531-Ch03-Module-Package-Application-Software.pdf) | [PPTX](Theory/28531-Ch03-Module-Package-Application-Software.pptx) |
| ০৪ | Basics of OOP | ৩ / ৬ | [PDF](Theory/28531-Ch04-Basics-of-OOP.pdf) | [PPTX](Theory/28531-Ch04-Basics-of-OOP.pptx) |
| ০৫ | Four Pillars of OOP | ৫ / ৯ | [PDF](Theory/28531-Ch05-Four-Pillars-of-OOP.pdf) | [PPTX](Theory/28531-Ch05-Four-Pillars-of-OOP.pptx) |
| ০৬ | Iterator, Generator & Decorator | ২ / ৪ | [PDF](Theory/28531-Ch06-Iterator-Generator-Decorator.pdf) | [PPTX](Theory/28531-Ch06-Iterator-Generator-Decorator.pptx) |
| ০৭ | Exception / Error Handling | ৪ / ৭ | [PDF](Theory/28531-Ch07-Exception-Error-Handling.pdf) | [PPTX](Theory/28531-Ch07-Exception-Error-Handling.pptx) |
| ০৮ | Logging in Python | ৩ / ৫ | [PDF](Theory/28531-Ch08-Logging-in-Python.pdf) | [PPTX](Theory/28531-Ch08-Logging-in-Python.pptx) |
| ০৯ | Unit Testing (unittest) | ৩ / ৬ | [PDF](Theory/28531-Ch09-Unit-Testing-unittest.pdf) | [PPTX](Theory/28531-Ch09-Unit-Testing-unittest.pptx) |
| ১০ | Python RegEx | ২ / ৪ | [PDF](Theory/28531-Ch10-Python-RegEx.pdf) | [PPTX](Theory/28531-Ch10-Python-RegEx.pptx) |
| ১১ | Application Software | ২ / ৫ | [PDF](Theory/28531-Ch11-Application-Software.pdf) | [PPTX](Theory/28531-Ch11-Application-Software.pptx) |

---

## Lab: ৬টি জব, প্রতিটির ৪ ধরনের সমাধান

প্রতিটি জব চারভাবে করা আছে। শিক্ষার্থী নিজের সুবিধামতো যেকোনোটি দিয়ে শুরু করতে পারে।

| # | সমাধানের ধরন | কোথায় | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|---|
| ১ | **বই অনুযায়ী (Lab Book)** | `Lab_Book/` | বইয়ের ধারা অনুযায়ী Jupyter notebook; জব ১ ও ২ এর logger সহ পূর্ণ module প্রজেক্ট | Jupyter / VS Code / Colab |
| ২ | **Single file** | `Lab_Syllabus_Jobs/JobN/1_single_file/` | সিলেবাসের ধাপ অনুযায়ী পুরো প্রোগ্রাম একটি ফাইলে | কম্পিউটারে (venv) |
| ৩ | **Module / Package** | `Lab_Syllabus_Jobs/JobN/2_modular/` | function আলাদা module এ, `import` ও `__init__.py` দিয়ে export (অধ্যায় ৩) | কম্পিউটারে (venv) |
| ৪ | **Google Colab** | `Lab_Syllabus_Jobs/JobN/3_colab/` | `.ipynb` notebook, প্রতিটি function ও ধাপ আলাদা cell এ | ব্রাউজারে |

### জবভিত্তিক সূচি

| জব | বিষয় | ক্লাস/নম্বর | ১. Lab Book | ২. Single file | ৩. Module / Package | ৪. Colab | বাংলা ব্যাখ্যা |
|---|---|---|---|---|---|---|---|
| ১ | Inventory Management for Fruits Item | ৩ / ৪ | [notebook](Lab_Book/practical-01-prepare-inventory-management-for-fruits-item.ipynb) · [project](Lab_Book/practical-01-prepare-inventory-management-for-fruits-item/) | [p1_inventory.py](Lab_Syllabus_Jobs/Job1_Fruit_Inventory/1_single_file/p1_inventory.py) | [2_modular](Lab_Syllabus_Jobs/Job1_Fruit_Inventory/2_modular/) | [Job1_colab.ipynb](Lab_Syllabus_Jobs/Job1_Fruit_Inventory/3_colab/Job1_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job1_Fruit_Inventory/README.md) |
| ২ | Generate PDF Report from CSV File | ৩ / ৪ | [notebook](Lab_Book/practical-02-generate-pdf-report-from-csv-file.ipynb) · [project](Lab_Book/practical-02-generate-pdf-report-from-csv-file/) | [p2_pdf_report.py](Lab_Syllabus_Jobs/Job2_PDF_Report/1_single_file/p2_pdf_report.py) | [2_modular](Lab_Syllabus_Jobs/Job2_PDF_Report/2_modular/) | [Job2_colab.ipynb](Lab_Syllabus_Jobs/Job2_PDF_Report/3_colab/Job2_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job2_PDF_Report/README.md) |
| ৩ | QR Code & Barcode Generator and Decoding | ২ / ৪ | [notebook](Lab_Book/practical-03-qr-code-and-barcode-generator-and-decoding.ipynb) | [p3_qr_barcode.py](Lab_Syllabus_Jobs/Job3_QR_Barcode/1_single_file/p3_qr_barcode.py) | [2_modular](Lab_Syllabus_Jobs/Job3_QR_Barcode/2_modular/) | [Job3_colab.ipynb](Lab_Syllabus_Jobs/Job3_QR_Barcode/3_colab/Job3_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job3_QR_Barcode/README.md) |
| ৪ | Web Scraping | ৩ / ৪ | [notebook](Lab_Book/practical-04-web-scrapping.ipynb) | [p4_scraping.py](Lab_Syllabus_Jobs/Job4_Web_Scraping/1_single_file/p4_scraping.py) | [2_modular](Lab_Syllabus_Jobs/Job4_Web_Scraping/2_modular/) | [Job4_colab.ipynb](Lab_Syllabus_Jobs/Job4_Web_Scraping/3_colab/Job4_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job4_Web_Scraping/README.md) |
| ৫ | Weather Report (Open Weather API) | ২ / ৪ | [notebook](Lab_Book/practical-05-weather-report.ipynb) | [p5_weather.py](Lab_Syllabus_Jobs/Job5_Weather_Report/1_single_file/p5_weather.py) | [2_modular](Lab_Syllabus_Jobs/Job5_Weather_Report/2_modular/) | [Job5_colab.ipynb](Lab_Syllabus_Jobs/Job5_Weather_Report/3_colab/Job5_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job5_Weather_Report/README.md) |
| ৬ | Database Design and Development | ৩ / ৫ | [notebook](Lab_Book/practical-06-database-design-and-development.ipynb) | [p6_database_app.py](Lab_Syllabus_Jobs/Job6_Database_App/1_single_file/p6_database_app.py) | [2_modular](Lab_Syllabus_Jobs/Job6_Database_App/2_modular/) | [Job6_colab.ipynb](Lab_Syllabus_Jobs/Job6_Database_App/3_colab/Job6_colab.ipynb) | [README](Lab_Syllabus_Jobs/Job6_Database_App/README.md) |

> **Lab Book বনাম Lab_Syllabus_Jobs:** `Lab_Book` বইয়ের উদাহরণ অনুসরণ করে। `Lab_Syllabus_Jobs` সরাসরি সিলেবাসের ধাপ (যেমন 1.1 Setup → 1.2 Take item data …) অনুসরণ করে, সহজ ভাষায় এবং প্রতিটি লাইনের বাংলা ব্যাখ্যাসহ। দুটি একসাথে পড়লে একই কাজের ভিন্ন ভিন্ন পদ্ধতি বোঝা যায়।

---

## কোথা থেকে শুরু করবেন

1. **একবারে সব এক জায়গায় পড়তে (Easy Guide):** GitHub এ পড়তে [README সংস্করণ](Lab_Syllabus_Jobs/docs/28531_Python_Jobs_Easy_Guide.md), প্রিন্ট বা অফলাইনে পড়তে [PDF সংস্করণ](Lab_Syllabus_Jobs/docs/28531_Python_Jobs_Easy_Guide.pdf)। দুটির বিষয়বস্তু একই। এতে Python install থেকে virtual environment, ৬টি জবের তিন সমাধানের কোড (সরাসরি কপি করা যায়), লাইন ধরে বাংলা ব্যাখ্যা ও ভাইভা প্রশ্ন সব আছে।
2. **কম্পিউটারে setup (virtual environment):** [Lab_Syllabus_Jobs/README.md](Lab_Syllabus_Jobs/README.md)
3. **Jupyter notebook চালাতে (Lab Book):** [Lab_Book/README.MD](Lab_Book/README.MD)
4. **নির্দিষ্ট জব:** উপরের জবভিত্তিক সূচি থেকে লিংকে ক্লিক করুন।

সংক্ষেপে (Windows), যেকোনো জবের ফোল্ডারে:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd 1_single_file
python p1_inventory.py
```

---

**Md Ruman Hossain**, Rangpur, Bangladesh · [GitHub](https://github.com/Ruman-Hossain) · [LinkedIn](https://www.linkedin.com/in/ruman-hossain/) · [Website](https://rumancsebrur.blogspot.com/)
