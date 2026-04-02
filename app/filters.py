KEYWORDS = [
    "baby",
    "kids",
    "stroller",
    "car seat",
    "bassinet",
    "toy",
    "nursery",
    "bouncer",
    "high chair",
    "playard"
]


def is_relevant_deal(deal):
    title_lower = deal["title"].lower()

    for keyword in KEYWORDS:
        if keyword in title_lower:
            return True

    return False


def filter_relevant_deals(deals):
    relevant_deals = []

    for deal in deals:
        if is_relevant_deal(deal):
            relevant_deals.append(deal)

    return relevant_deals