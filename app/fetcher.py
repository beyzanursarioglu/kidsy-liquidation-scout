import requests


def fetch_html(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def save_html_to_file(html_content, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)