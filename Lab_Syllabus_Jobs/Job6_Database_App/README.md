# জব ৬: Database Design and Development

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ৩ | **নম্বর:** ৫

## উদ্দেশ্য

একটি ফর্ম (GUI) দিয়ে ছাত্রের তথ্য ডাটাবেসে **Save** করা হবে। Roll দিয়ে **Search** করা যাবে, ফর্ম **Clear** করা যাবে, এবং সব রেকর্ডের তালিকা দেখা যাবে।

সিলেবাসের ধাপ: 6.1 Setup → 6.2 Design a simple form → 6.3 Insert fields → 6.4 Add command buttons → 6.5 Write code for input, save and search

## দুটি built-in লাইব্রেরি

| লাইব্রেরি | কাজ | কেন এটি |
|---|---|---|
| `tkinter` | GUI: window, label, entry box, button | Python এর সাথেই আসে, install লাগে না। শেখার জন্য সবচেয়ে সহজ। |
| `sqlite3` | ডাটাবেস | আলাদা ডাটাবেস সার্ভার (MySQL এর মতো) চালাতে হয় না। পুরো ডাটাবেস একটি `.db` ফাইলে থাকে। |

## টেবিল ডিজাইন

```
students
┌────────────┬──────┬──────────────┐
│ field      │ type │ constraint   │
├────────────┼──────┼──────────────┤
│ roll       │ TEXT │ PRIMARY KEY  │  একই roll দুবার নয়
│ name       │ TEXT │ NOT NULL     │  নাম খালি রাখা যাবে না
│ department │ TEXT │ —            │
│ phone      │ TEXT │ —            │
└────────────┴──────┴──────────────┘
```

## ফর্মের নকশা

```
┌──────────── Student Database ────────────┐
│ Roll        [______________________]     │
│ Name        [______________________]     │
│ Department  [______________________]     │
│ Phone       [______________________]     │
│        [ Save ]  [ Search ]  [ Clear ]    │
│ ┌──────────────────────────────────────┐ │
│ │ 701234 | Rahim Uddin | CST | 017...  │ │
│ │ 701235 | Sumaiya Akter | CST | 018...│ │
│ └──────────────────────────────────────┘ │
└──────────────────────────────────────────┘
```

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

> জব ৬ এর ফর্ম (tkinter window) Colab এ খোলে না। তাই Colab এ একই ডাটাবেসের **মেনু সংস্করণ** (`p6_console_colab.py`) দেওয়া আছে।

### ফোল্ডারের গঠন

```
Job6_Database_App/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p6_database_app.py
├── 2_modular/
│   ├── main.py
│   └── student_db/
│       ├── __init__.py
│       ├── database.py
│       └── gui.py
└── 3_colab/
    ├── Job6_colab.ipynb
    └── p6_console_colab.py
```

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job6_Database_App` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p6_database_app.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `student_db` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job6_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

### এই জবের বিশেষ নোট

**tkinter (ফর্মের জন্য):**
- **Windows:** python.org এর installer এ tkinter থাকে। install এর সময় "tcl/tk and IDLE" টিক থাকতে হবে (ডিফল্টে থাকে)।
- **Linux (Ubuntu):** tkinter না থাকলে `sudo apt install python3-tk` দিন।

**Colab এ কেন আলাদা ফাইল:** Google Colab একটি দূরের সার্ভারে চলে, যার কোনো স্ক্রিন (display) নেই। তাই tkinter window **খোলা সম্ভব নয়** (`TclError: no display name` দেখায়)। এজন্য `3_colab/p6_console_colab.py` দেওয়া হয়েছে: **একই ডাটাবেস ও একই SQL**, শুধু ফর্মের বদলে মেনু থেকে ইনপুট নেওয়া হয়।

> GUI দেখাতে ও পরীক্ষায় জমা দিতে লোকাল কম্পিউটারে সমাধান ১ বা ২ চালান।

কাজ শেষে Terminal এ `deactivate`।

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে) `p6_database_app.py`

> **কোডের ক্রম লক্ষ করুন:** Step 1 (ডাটাবেস) → Step 4 (function) → Step 2 (ফর্ম) → Step 3 (বোতাম)। function গুলো বোতামের **আগে** লেখা হয়েছে, কারণ লাইন ৭১–৭৩ এ `command=save_data` লেখার সময় `save_data` নামটি আগেই তৈরি থাকতে হবে।

### লাইন ১–৩: module আনা

```python
import sqlite3
import tkinter as tk
from tkinter import messagebox
```

- **`sqlite3`:** ডাটাবেস তৈরি, ডাটা রাখা ও খোঁজার জন্য।
- **`import tkinter as tk`:** `as tk` মানে ছোট ডাকনাম। প্রতিবার `tkinter.Label` না লিখে `tk.Label` লেখা যায়।
- **`from tkinter import messagebox`:** ছোট বার্তার পপআপ (তথ্য, সতর্কতা, error) দেখানোর জন্য। এটি tkinter এর একটি আলাদা submodule, তাই আলাদা করে import করতে হয়।

### লাইন ৬–৭: ডাটাবেসের সাথে সংযোগ

```python
conn = sqlite3.connect("student.db")
cur = conn.cursor()
```

- **`sqlite3.connect("student.db")`:** `student.db` ফাইলের সাথে সংযোগ (connection) তৈরি করে। ফাইল না থাকলে **নিজেই নতুন তৈরি করে**।
- **`conn.cursor()`:** একটি cursor object দেয়, যা দিয়ে SQL কমান্ড চালানো ও ফলাফল আনা হয়।
- **connection ও cursor দুটো কেন:** connection হলো ডাটাবেসের সাথে "লাইন", যা দিয়ে `commit` ও `close` হয়। cursor হলো সেই লাইনে কাজ করার "হাত", যা দিয়ে `execute` ও `fetch` হয়।

### লাইন ৮–১৩: টেবিল তৈরি

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

### লাইন ১৬–২১: Save function — খালি ইনপুট যাচাই

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

### লাইন ২২–৩০: Save function — ডাটাবেসে রাখা

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

### লাইন ৩২–৪৩: Search function

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

### লাইন ৪৫–৪৭: Clear function

```python
def clear_form():
    for entry in (e_roll, e_name, e_dept, e_phone):
        entry.delete(0, tk.END)
```

- **কী হচ্ছে:** চারটি Entry বক্স একটি tuple এ রেখে লুপ চালানো হলো। প্রতিটি থেকে `delete(0, tk.END)` সব লেখা মুছে দেয়।
- **`delete(শুরু, শেষ)`:** `0` প্রথম অক্ষর, `tk.END` শেষ অক্ষর পর্যন্ত, অর্থাৎ সব মুছে যায়।
- **কেন লুপ:** চারবার একই লাইন না লিখে এক জায়গায় লিখলে কোড ছোট হয় এবং নতুন field যোগ করা সহজ হয়।

### লাইন ৪৯–৫২: সব রেকর্ড তালিকায় দেখানো

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

### লাইন ৫৫–৫৭: মূল window তৈরি

```python
root = tk.Tk()
root.title("Student Database")
root.geometry("460x400")
```

- **`tk.Tk()`:** প্রোগ্রামের মূল window তৈরি করে। সব widget (label, button) এর ভিতরেই বসবে।
- **`title()`:** window এর উপরের বারে নাম।
- **`geometry("প্রস্থxউচ্চতা")`:** window এর আকার পিক্সেলে। মাঝে ইংরেজি ছোট হাতের `x`।

### লাইন ৫৯–৬৬: Label ও Entry (field) তৈরি

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

### লাইন ৬৯–৭৩: Command button

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

### লাইন ৭৫–৭৭: তালিকা বক্স

```python
listbox = tk.Listbox(root, width=55, height=8)
listbox.grid(row=5, column=0, columnspan=2, padx=10)
show_all()
```

- **`tk.Listbox`:** একাধিক লাইনের তালিকা দেখানোর widget। `height=8` মানে একসাথে ৮টি লাইন দেখা যায়।
- **`show_all()`:** প্রোগ্রাম চালু হতেই ডাটাবেসে আগে থেকে থাকা রেকর্ডগুলো তালিকায় দেখায়।

### লাইন ৭৯–৮০: window চালু রাখা ও সংযোগ বন্ধ

```python
root.mainloop()
conn.close()
```

- **`root.mainloop()`:** window টি খোলা রাখে এবং ক্লিক, টাইপ ইত্যাদি **event এর জন্য অপেক্ষা করে**। এটি না দিলে window এক মুহূর্তে খুলে বন্ধ হয়ে যেত। ব্যবহারকারী window বন্ধ (✕) না করা পর্যন্ত প্রোগ্রাম এই লাইনেই থাকে।
- **`conn.close()`:** window বন্ধ হলে ডাটাবেসের সংযোগ বন্ধ করে। এটি ভালো অভ্যাস, এতে ফাইল লক হয়ে থাকে না।

---

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** **database.py** শুধু ডাটাবেসের কাজ করে (কোনো window নেই), **gui.py** শুধু ফর্ম দেখায় এবং database এর function ডাকে। একই database.py Colab এর মেনু সংস্করণেও ব্যবহার করা যায়। এটাই module এর আসল সুবিধা।

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

### `student_db/__init__.py` — package এর দরজা

```python
"""student_db package: SQLite database functions and a tkinter form that uses them."""

from .database import create_table, save_student, find_student, all_students

__all__ = ["create_table", "save_student", "find_student", "all_students"]
```

- ডাটাবেসের চারটি function export করে। gui কে আলাদা রাখা হয়েছে, কারণ GUI ছাড়াও (যেমন Colab এ) ডাটাবেস ব্যবহার করা যায়।

### `student_db/database.py` — ডাটাবেসের কাজ

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

### `student_db/gui.py` — ফর্ম (GUI)

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

### `main.py` — প্রোগ্রাম শুরু

```python
from student_db.gui import run_app

if __name__ == "__main__":
    run_app()
```

- `from student_db.gui import run_app`: package এর ভিতরের নির্দিষ্ট module (gui) থেকে সরাসরি import।
- main.py মাত্র কয়েক লাইন। পুরো প্রোগ্রাম package এর ভিতরে, main শুধু শুরু করে।

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job6_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: module import ও ডাটাবেস টেবিল | student.db ও students টেবিল তৈরি হবে। |
| Cell 2: function ১: save_data() তৈরি | নতুন ছাত্র সংরক্ষণের function। শুধু তৈরি হবে। |
| Cell 3: function ২: search_data() তৈরি | roll দিয়ে খোঁজার function। |
| Cell 4: function ৩: show_all() তৈরি | সব রেকর্ড দেখানোর function। |
| Cell 5: মেনু চালানো | 1 Save, 2 Search, 3 Show all, 4 Exit। শেষে 4 দিন। |
| Cell 6: ডাটাবেসে কী আছে দেখা |  |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## `p6_console_colab.py` (Colab সংস্করণ) এর পার্থক্য

ডাটাবেস অংশ (লাইন ১–১১) হুবহু একই। পার্থক্য শুধু ইনপুট-আউটপুটে:

| GUI সংস্করণ | Console সংস্করণ |
|---|---|
| `e_roll.get()` দিয়ে Entry বক্স থেকে | `input("Roll: ")` দিয়ে কীবোর্ড থেকে |
| `messagebox.showinfo(...)` পপআপ | `print(...)` লেখা |
| Search এ ফর্ম ভরে যায় | Search এ `Found: ...` ছাপে |
| বোতাম চেপে কাজ বাছাই | `while True` মেনু: 1 Save, 2 Search, 3 Show all, 4 Exit |
| `mainloop()` | `while True` লুপ, `4` দিলে `break` |

মেনুর লুপে `if / elif / else` দিয়ে বাছাই করা হয়। ভুল নম্বর দিলে `Invalid choice!` দেখায়।

---

## নমুনা ইনপুট ও আউটপুট (পরীক্ষিত)

| পরীক্ষার ইনপুট / কাজ | ফলাফল |
|---|---|
| 701234, Rahim Uddin, CST, 01712345678 → **Save** | পপআপ "Student saved successfully"। ফর্ম খালি হয়, তালিকায় রেকর্ড আসে। |
| 701235, Sumaiya Akter, CST, 01812345678 → **Save** | সফল |
| আবার 701234 → **Save** | লাল পপআপ "This roll already exists" |
| Roll ও Name খালি → **Save** | হলুদ পপআপ "Roll and Name are required" |
| Roll বক্সে 701235 → **Search** | ফর্মে ভরে যায়: 701235, Sumaiya Akter, CST, 01812345678 |
| 709999 → **Search** | পপআপ "No student with roll 709999" |

তালিকা বক্সে:
```
701234 | Rahim Uddin | CST | 01712345678
701235 | Sumaiya Akter | CST | 01812345678
```

ডাটা `student.db` ফাইলে স্থায়ীভাবে থাকে। প্রোগ্রাম বন্ধ করে আবার খুললেও রেকর্ড থাকে। টেবিলটি দেখতে চাইলে **DB Browser for SQLite** (sqlitebrowser.org) দিয়ে `student.db` খুলুন।

Colab সংস্করণের নমুনা:
```
1. Save   2. Search   3. Show all   4. Exit
Choose (1-4): 1
Roll: 701234
Name: Rahim Uddin
Department: CST
Phone: 01712345678
Saved: Student saved successfully

1. Save   2. Search   3. Show all   4. Exit
Choose (1-4): 2
Enter roll to search: 701234
Found: 701234 | Rahim Uddin | CST | 01712345678

1. Save   2. Search   3. Show all   4. Exit
Choose (1-4): 4
Bye!
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
| window খোলার আগেই Save চলে যায় | `command=save_data()` লেখা হয়েছে। `()` বাদ দিন। |
| `database is locked` | `student.db` অন্য সফটওয়্যারে (যেমন DB Browser) খোলা আছে। বন্ধ করুন। |
| `ModuleNotFoundError: No module named 'tkinter'` (Linux) | `sudo apt install python3-tk` |
| Colab এ `TclError: no display name` | Colab এ GUI চলে না। `p6_console_colab.py` ব্যবহার করুন। |
| প্রোগ্রাম বন্ধ করলে ডাটা থাকে না | কোনো জায়গায় `conn.commit()` বাদ পড়েছে। |
| শুরু থেকে নতুন করে চাই | `student.db` ফাইলটি মুছে দিন। |

## বাড়তি কাজ (অনুশীলন)

1. **Update** বোতাম যোগ করুন: `UPDATE students SET name = ?, department = ?, phone = ? WHERE roll = ?`
2. **Delete** বোতাম যোগ করুন: `DELETE FROM students WHERE roll = ?`। মোছার আগে `messagebox.askyesno()` দিয়ে নিশ্চিত হয়ে নিন।
3. Listbox এ একটি লাইনে ক্লিক করলে সেই রেকর্ড ফর্মে ভরে যাবে (`listbox.bind("<<ListboxSelect>>", ...)`)।
4. Department এর জন্য Entry এর বদলে `ttk.Combobox` (CST, Civil, Electrical...) ব্যবহার করুন।

## ভাইভা প্রশ্ন ও উত্তর

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
