from bs4 import BeautifulSoup
from collectors.base_collector import BaseCollector


class MarketplaceCollector(BaseCollector):
    def __init__(self, file_path):
        self.file_path = file_path

    def _get_text(self, parent, tag_name, class_name, default_value=""):
        element = parent.find(tag_name, class_=class_name)
        if element:
            return element.text.strip()
        return default_value

    def _get_href(self, parent, class_name, default_value=""):
        element = parent.find("a", class_=class_name)
        if element and element.has_attr("href"):
            return element["href"]
        return default_value

    def _parse_price(self, price_text):
        cleaned = price_text.replace("$", "").replace(",", "").strip()
        try:
            return int(float(cleaned))
        except ValueError:
            return 0

    def collect(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        listing_cards = soup.find_all("div", class_="listing-card")

        deals = []

        for card in listing_cards:
            title = self._get_text(card, "h3", "listing-title", "Untitled Deal")
            price_text = self._get_text(card, "span", "listing-price", "$0")
            condition = self._get_text(card, "span", "listing-condition", "Unknown")
            location = self._get_text(card, "span", "listing-location", "Unknown")
            source = self._get_text(card, "span", "listing-source", "Unknown Source")
            url = self._get_href(card, "listing-link", "")

            deal = {
                "title": title,
                "price": self._parse_price(price_text),
                "source": source,
                "condition": condition,
                "location": location,
                "url": url,
            }

            deals.append(deal)

        return deals