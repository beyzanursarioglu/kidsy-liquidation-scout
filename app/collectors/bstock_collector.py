from bs4 import BeautifulSoup
from collectors.base_collector import BaseCollector


class BStockCollector(BaseCollector):
    def __init__(self, file_path):
        self.file_path = file_path

    def _get_text_or_default(self, parent, tag_name, class_name, default_value=""):
        element = parent.find(tag_name, class_=class_name)
        if element:
            return element.text.strip()
        return default_value

    def _get_link_or_default(self, parent, class_name, default_value=""):
        element = parent.find("a", class_=class_name)
        if element and element.has_attr("href"):
            return element["href"]
        return default_value

    def _parse_price(self, price_text):
        try:
            return int(price_text)
        except ValueError:
            return 0

    def collect(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        deal_elements = soup.find_all("div", class_="deal")

        deals = []

        for deal_element in deal_elements:
            try:
                title = self._get_text_or_default(deal_element, "h2", "title", "Untitled Deal")
                price_text = self._get_text_or_default(deal_element, "p", "price", "0")
                source = self._get_text_or_default(deal_element, "p", "source", "Unknown Source")
                condition = self._get_text_or_default(deal_element, "p", "condition", "Unknown")
                location = self._get_text_or_default(deal_element, "p", "location", "Unknown")
                url = self._get_link_or_default(deal_element, "url", "")

                price = self._parse_price(price_text)

                deal = {
                    "title": title,
                    "price": price,
                    "source": source,
                    "condition": condition,
                    "location": location,
                    "url": url
                }

                deals.append(deal)

            except Exception as error:
                print("Skipping one deal due to parse error:", error)

        return deals