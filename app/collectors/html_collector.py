from bs4 import BeautifulSoup


def collect_deals_from_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    deal_elements = soup.find_all("div", class_="deal")

    deals = []

    for deal_element in deal_elements:
        title = deal_element.find("h2", class_="title").text.strip()
        price = int(deal_element.find("p", class_="price").text.strip())
        source = deal_element.find("p", class_="source").text.strip()
        condition = deal_element.find("p", class_="condition").text.strip()
        location = deal_element.find("p", class_="location").text.strip()
        url = deal_element.find("a", class_="url")["href"]

        deal = {
            "title": title,
            "price": price,
            "source": source,
            "condition": condition,
            "location": location,
            "url": url
        }

        deals.append(deal)

    return deals