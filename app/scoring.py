STRONG_SOURCES = [
    "B-Stock",
    "Liquidation.com",
    "Direct Liquidation"
]


def score_deal(deal):
    score = 0
    title_lower = deal["title"].lower()

    keywords = [
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

    for keyword in keywords:
        if keyword in title_lower:
            score += 30
            break

    condition = deal["condition"].lower()

    if condition == "overstock":
        score += 20
    elif condition == "returns":
        score += 10

    if deal["price"] <= 1000:
        score += 10

    if deal["source"] in STRONG_SOURCES:
        score += 10

    if deal["location"] in ["NJ", "PA", "CT", "NY"]:
        score += 5

    return score


def add_scores_to_deals(deals):
    scored_deals = []

    for deal in deals:
        deal_copy = deal.copy()
        deal_copy["score"] = score_deal(deal_copy)
        scored_deals.append(deal_copy)

    return scored_deals