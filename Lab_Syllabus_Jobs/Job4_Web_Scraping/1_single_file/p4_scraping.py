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
