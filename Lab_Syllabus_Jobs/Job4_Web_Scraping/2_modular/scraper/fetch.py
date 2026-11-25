import requests


def get_html(url):
    """Download a web page and return (status_code, html_text)."""
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8"
    return response.status_code, response.text
