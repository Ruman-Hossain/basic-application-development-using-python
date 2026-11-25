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
