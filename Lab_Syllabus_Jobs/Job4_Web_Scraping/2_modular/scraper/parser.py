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
