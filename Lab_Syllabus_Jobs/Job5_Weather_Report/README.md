# জব ৫: Weather Report (Open Weather API)

**বিষয়:** 28531 Application Development Using Python (৩য় পর্ব, CST)
**ক্লাস:** ২ | **নম্বর:** ৪

## উদ্দেশ্য

ব্যবহারকারী একটি শহরের নাম দেবে। প্রোগ্রাম OpenWeather API থেকে সেই শহরের বর্তমান আবহাওয়া এনে তাপমাত্রা, আর্দ্রতা, অবস্থা ও বাতাসের গতি দেখাবে।

সিলেবাসের ধাপ: 5.1 Setup → 5.2 Connect with Open Weather API → 5.3 Take location → 5.4 Get weather data → 5.5 Print basic data

## API ও JSON কী

- **API (Application Programming Interface):** এক প্রোগ্রাম অন্য প্রোগ্রাম থেকে ডাটা চাওয়ার নির্দিষ্ট নিয়ম।
  - উপমা: রেস্টুরেন্টের ওয়েটার।
  - আমরা ওয়েটারকে অর্ডার দিই (request), রান্নাঘর (server) খাবার বানায়, ওয়েটার তা এনে দেয় (response)।
  - আমাদের রান্নাঘরে ঢুকতে হয় না।
- **JSON:** API যে আকারে ডাটা পাঠায়। দেখতে Python এর dictionary এর মতো, key-value জোড়ায়।

```
{ "name": "Dhaka",
  "sys":  { "country": "BD" },
  "main": { "temp": 26.99, "feels_like": 28.5, "humidity": 65 },
  "weather": [ { "description": "haze" } ],
  "wind": { "speed": 2.06 } }
```

## তিন ধরনের সমাধান

এই জবটি **তিনভাবে** করা আছে। তিনটিই একই কাজ করে এবং একই আউটপুট দেয়। পার্থক্য শুধু কোড সাজানোর ধরনে।

| সমাধান | ফোল্ডার | কী শিখবেন | কোথায় চালাবেন |
|---|---|---|---|
| **১. Single file** | `1_single_file/` | পুরো প্রোগ্রাম একটি ফাইলে, উপর থেকে নিচে পড়া যায় | লোকাল কম্পিউটার (venv) |
| **২. Module / Package** | `2_modular/` | function আলাদা module এ রাখা, `import` ও package থেকে export (অধ্যায় ৩) | লোকাল কম্পিউটার (venv) |
| **৩. Google Colab** | `3_colab/` | `.ipynb` notebook: কোড আলাদা আলাদা cell এ, প্রতিটি ধাপ চালিয়ে দেখা | ব্রাউজারে (colab.research.google.com) |

### ফোল্ডারের গঠন

```
Job5_Weather_Report/
├── README.md              ← এই ফাইল
├── requirements.txt       ← তিন সমাধানের জন্যই একই package
├── 1_single_file/
│   └── p5_weather.py
├── 2_modular/
│   ├── main.py
│   └── weather/
│       ├── __init__.py
│       ├── api.py
│       ├── config.py
│       └── display.py
└── 3_colab/
    └── Job5_colab.ipynb
```

## ধাপ ০: API Key সংগ্রহ (ক্লাসের আগেই করুন)

1. https://openweathermap.org এ গিয়ে **Sign Up** করে একটি ফ্রি একাউন্ট খুলুন। ই-মেইল যাচাই করুন।
2. প্রোফাইল মেনু থেকে **My API keys** এ যান এবং key টি কপি করুন।
3. নতুন key **সক্রিয় হতে কয়েক মিনিট থেকে ঘণ্টা দুয়েক** লাগতে পারে। তাই ক্লাসের আগেই তৈরি করে রাখুন।
4. `p5_weather.py` এর লাইন ৩ এ `your_api_key_here` এর জায়গায় নিজের key বসান।

> **key গোপন রাখুন।** GitHub বা অনলাইনে key সহ কোড আপলোড করবেন না। key টি আপনার একাউন্টের পাসওয়ার্ডের মতো।

## চালানোর নিয়ম

### ধাপ ক: virtual environment (জবের ফোল্ডারে, একবারই)

VS Code এ **File → Open Folder** দিয়ে `Job5_Weather_Report` ফোল্ডার খুলুন, তারপর **Terminal → New Terminal**:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/Mac এ activate: `source venv/bin/activate`)। লাইনের শুরুতে `(venv)` দেখা গেলে ঠিক আছে। এই একটি environment দিয়েই সমাধান ১ ও ২ দুটোই চলবে।

### ধাপ খ: সমাধান ১ (single file) চালানো

```bash
cd 1_single_file
python p5_weather.py
```

### ধাপ গ: সমাধান ২ (module/package) চালানো

```bash
cd ../2_modular
python main.py
```

`main.py` অবশ্যই `2_modular` ফোল্ডার থেকে চালাবেন, যাতে Python `weather` package খুঁজে পায়। তৈরি হওয়া ফাইলগুলো যে ফোল্ডার থেকে চালাচ্ছেন সেখানেই হবে।

### ধাপ ঘ: সমাধান ৩ (Google Colab) চালানো

colab.research.google.com → **File → Upload notebook** → `3_colab/Job5_colab.ipynb` আপলোড করুন → উপর থেকে প্রতিটি cell এ **Shift + Enter** (অথবা **Runtime → Run all**)।

> **API key কোথায় বসাবেন:** সমাধান ১ এ `p5_weather.py` এর লাইন ৩ এ, সমাধান ২ এ `weather/config.py` তে, সমাধান ৩ এ notebook এর import cell এ।

### এই জবের বিশেষ নোট

> **ইন্টারনেট সংযোগ ও সক্রিয় API key লাগবে** (তিন সমাধানেই)।

কাজ শেষে Terminal এ `deactivate`।

## সমাধান ১: Single file — কোডের ব্যাখ্যা (লাইন/ব্লক ধরে)

### লাইন ১: module আনা

```python
import requests
```

- **কেন `requests`:** API ও ইন্টারনেটে HTTP request পাঠানোর জন্য। এটি JSON উত্তরকে সরাসরি dictionary তে রূপান্তর করার সুবিধাও দেয় (`.json()`)।

### লাইন ৩–৪: API key ও ঠিকানা

```python
API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"
```

- **`API_KEY`:** OpenWeather আমাদের চেনে এই key দিয়ে। key ছাড়া বা ভুল key দিলে সার্ভার ডাটা দেয় না (401 error)।
- **`URL`:** API এর **endpoint**, অর্থাৎ যে নির্দিষ্ট ঠিকানায় "বর্তমান আবহাওয়া" চাওয়া হয়। `2.5` API এর version।
- **কেন বড় হাতের নাম:** এগুলো ধ্রুবক (constant), প্রোগ্রাম চলার সময় বদলায় না।

### লাইন ৭: শহরের নাম ইনপুট

```python
city = input("Enter city name: ")
```

- **কী হচ্ছে:** ব্যবহারকারী শহরের নাম ইংরেজিতে দেবে, যেমন `Dhaka`, `Pabna`, `London`।

### লাইন ১০: request এর parameter

```python
params = {"q": city, "appid": API_KEY, "units": "metric"}
```

- **কী হচ্ছে:** API কে যা জানাতে হবে তা একটি dictionary তে রাখা হলো।
  - `q` (query) = শহরের নাম।
  - `appid` = API key।
  - `units` = এককের ধরন।
- **কেন `"units": "metric"`:** না দিলে তাপমাত্রা **Kelvin** এ আসে (যেমন 300.14)। `metric` দিলে **সেলসিয়াস** (°C) ও বাতাসের গতি m/s এ আসে।
- **কেন dictionary (URL হাতে লিখে নয়):** `requests` নিজেই এগুলো দিয়ে সঠিক URL বানায়: `...weather?q=Dhaka&appid=KEY&units=metric`। শহরের নামে স্পেস থাকলে (যেমন `New York`) সেটিও ঠিকভাবে encode করে (`New%20York`)। হাতে লিখলে এসব ভুলের সম্ভাবনা থাকে।

### লাইন ১১–১৫: API তে request পাঠানো ও ইন্টারনেট সমস্যা সামলানো

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

### লাইন ১৭: JSON কে dictionary তে রূপান্তর

```python
data = response.json()
```

- **কী হচ্ছে:** সার্ভারের পাঠানো JSON লেখাকে Python **dictionary** তে রূপান্তর করে।
- **কেন:** dictionary হলে `data["main"]["temp"]` এভাবে সহজে মান নেওয়া যায়। (`response.text` দিলে শুধু একটি লম্বা string পাওয়া যেত।)
- error হলেও (ভুল শহর, ভুল key) সার্ভার JSON পাঠায়, যার ভিতরে `message` থাকে। তাই এখানে এটি নিরাপদ।

### লাইন ২০: সফল কিনা যাচাই

```python
if response.status_code == 200:
```

- **কী হচ্ছে:** `200` মানে সফলভাবে আবহাওয়ার ডাটা এসেছে।
- **কেন যাচাই:** ভুল শহরে `404`, ভুল key তে `401` আসে, আর তখন JSON এ `main`, `wind` এসব key থাকে না। যাচাই ছাড়া `data["main"]` লিখলে `KeyError` হতো।

### লাইন ২১–২৭: আবহাওয়ার রিপোর্ট ছাপা

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

### লাইন ২৮–২৯: ব্যর্থ হলে সার্ভারের বার্তা

```python
else:
    print("Error:", data.get("message"))
```

- **কী হচ্ছে:** সফল না হলে সার্ভার JSON এ `message` key তে কারণ লিখে পাঠায়। সেটি ছাপা হয়।
- **কেন `.get("message")` (`["message"]` নয়):** `.get()` key না থাকলে error না দিয়ে `None` দেয়। error এর উত্তরে `message` না থাকলেও প্রোগ্রাম ক্র্যাশ করবে না।

---

## সমাধান ২: Module / Package — ব্যাখ্যা

**মূল ধারণা:** **config.py** এ শুধু API key ও URL (সেটিং), **api.py** সার্ভারের সাথে যোগাযোগ করে, **display.py** রিপোর্ট ছাপে। API key বদলাতে কোড না ঘেঁটে শুধু config.py খুলতে হয়।

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

### `weather/__init__.py` — package এর দরজা

```python
"""weather package: get current weather from the OpenWeather API and show it."""

from .api import get_weather
from .display import print_report

__all__ = ["get_weather", "print_report"]
```

- `get_weather` ও `print_report` export করে। config বাইরে দেওয়া হয়নি, কারণ সেটি package এর ভিতরের ব্যবহারের জন্য।

### `weather/config.py` — সেটিং (API key)

```python
API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"
```

- **এখানে `your_api_key_here` এর জায়গায় নিজের key বসান।** শুধু ভেরিয়েবল আছে, কোনো function নেই।

### `weather/api.py` — API তে request

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

### `weather/display.py` — রিপোর্ট ছাপা

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

### `main.py` — ইনপুট, error সামলানো ও চালানো

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

### single file ও module সংস্করণের তুলনা

| বিষয় | Single file | Module / Package |
|---|---|---|
| কোড কোথায় | একটি ফাইলে সব | কাজ অনুযায়ী আলাদা ফাইলে |
| পড়া | ছোট প্রোগ্রামে সহজ | বড় প্রোগ্রামে সহজ, প্রতিটি ফাইল ছোট |
| পরিবর্তন | পুরো ফাইল ঘাঁটতে হয় | শুধু সংশ্লিষ্ট module বদলাতে হয় |
| পুনর্ব্যবহার | কঠিন | অন্য প্রজেক্টে `import` করেই ব্যবহার করা যায় |
| পরীক্ষা (testing) | কঠিন | প্রতিটি function আলাদাভাবে পরীক্ষা করা যায় (অধ্যায় ৯) |

## সমাধান ৩: Google Colab (`3_colab/Job5_colab.ipynb`)

Colab এ পুরো কোড আলাদা আলাদা cell এ ভাগ করা থাকে: install → import → প্রতিটি function বা ধাপ → চালানো। প্রতিটি cell চালিয়ে সাথে সাথে ফলাফল দেখা যায়। সব cell একই memory শেয়ার করে, তাই উপর থেকে ক্রমানুসারে চালাতে হয়।

| cell | কী হয় |
|---|---|
| Cell 1: package install |  |
| Cell 2: module import ও API key | চালানোর আগে your_api_key_here এর জায়গায় নিজের key বসান। |
| Cell 3: ধাপ ১: শহরের নাম ইনপুট | শহরের নাম ইংরেজিতে দিন, যেমন Dhaka। |
| Cell 4: ধাপ ২: API তে request পাঠানো | সার্ভার থেকে JSON এনে dictionary বানানো। |
| Cell 5: ধাপ ৩: আবহাওয়ার রিপোর্ট দেখানো |  |

- **function তৈরির cell** চালালে কিছু দেখায় না, শুধু function তৈরি হয়। এটাই স্বাভাবিক।
- `!pip install ...` এর শুরুর `!` মানে এটি Python নয়, Terminal এর কমান্ড।
- `NameError: name '...' is not defined` দেখালে আগের কোনো cell চালানো হয়নি। উপর থেকে আবার চালান।
- Colab বন্ধ হলে তৈরি ফাইল মুছে যায়। বাম পাশের 📁 Files থেকে দরকারি ফাইল ডাউনলোড করে রাখুন।

## নমুনা ইনপুট ও আউটপুট

> আবহাওয়া প্রতি মুহূর্তে বদলায়, তাই আপনার সংখ্যাগুলো আলাদা হবে। এখানে আউটপুটের **গঠন** দেখানো হলো।

সঠিক শহর:
```
Enter city name: Dhaka
----- Weather Report -----
City        : Dhaka , BD
Temperature : 26.99 °C
Feels like  : 28.5 °C
Humidity    : 65 %
Condition   : haze
Wind speed  : 2.06 m/s
```

ভুল শহরের নাম:
```
Enter city name: Dhakaa
Error: city not found
```

ভুল বা এখনও সক্রিয় না হওয়া API key:
```
Error: Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.
```

ইন্টারনেট না থাকলে:
```
Enter city name: Dhaka
No internet connection!
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
| `Error: Invalid API key` | key ভুল কপি হয়েছে, অথবা নতুন key এখনও সক্রিয় হয়নি। কিছুক্ষণ পরে আবার চেষ্টা করুন। |
| তাপমাত্রা ২৯৯ এর মতো বড় সংখ্যা | `units=metric` নেই, তাই Kelvin আসছে (°C = K − 273.15)। |
| `Error: city not found` | শহরের বানান ভুল। ইংরেজিতে সঠিক বানান দিন, প্রয়োজনে দেশ সহ: `Pabna,BD`। |
| `No internet connection!` | ইন্টারনেট সংযোগ দেখুন। |

## বাড়তি কাজ (অনুশীলন)

1. একাধিক শহরের নাম একটি list এ রেখে লুপে সবার আবহাওয়া দেখান।
2. প্রতিটি ফলাফল তারিখ-সময় সহ একটি CSV ফাইলে সংরক্ষণ করুন (জব ১ এর মতো)।
3. তাপমাত্রা ৩৫ °C এর বেশি হলে "Heat alert!" সতর্কবার্তা দেখান।
4. API key কোডে না লিখে environment variable থেকে নিন: `import os` তারপর `API_KEY = os.environ.get("OWM_API_KEY")`।

## ভাইভা প্রশ্ন ও উত্তর

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
