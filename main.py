def is_relevant_deal(deal):
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
            return True

    return False


def filter_relevant_deals(deals):
    relevant_deals = []

    for deal in deals:
        if is_relevant_deal(deal):
            relevant_deals.append(deal)

    return relevant_deals


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

    strong_sources = [
        "B-Stock",
        "Liquidation.com",
        "Direct Liquidation"
    ]

    for keyword in keywords:
        if keyword in title_lower:
            score += 30
            break

    if deal["condition"].lower() == "overstock":
        score += 20
    elif deal["condition"].lower() == "returns":
        score += 10

    if deal["price"] <= 1000:
        score += 10

    if deal["source"] in strong_sources:
        score += 10

    return score


deals = [
    {
        "title": "Graco Baby Stroller Lot",
        "price": 1200,
        "source": "B-Stock",
        "condition": "Returns"
    },
    {
        "title": "Fisher-Price Toy Bundle",
        "price": 800,
        "source": "Liquidation.com",
        "condition": "Overstock"
    },
    {
        "title": "Office Chairs Bulk Sale",
        "price": 500,
        "source": "Wholesale Hub",
        "condition": "Used"
    },
    {
        "title": "Baby Bassinet Returns Pallet",
        "price": 950,
        "source": "Direct Liquidation",
        "condition": "Returns"
    },
    {
        "title": "Electronics Clearance Lot",
        "price": 1500,
        "source": "B-Stock",
        "condition": "Mixed"
    }
]

relevant_deals = filter_relevant_deals(deals)

for deal in relevant_deals:
    deal["score"] = score_deal(deal)

sorted_deals = sorted(relevant_deals, key=lambda deal: deal["score"], reverse=True)

print("Top relevant deals:\n")

for deal in sorted_deals:
    print("Title:", deal["title"])
    print("Price:", deal["price"])
    print("Source:", deal["source"])
    print("Condition:", deal["condition"])
    print("Score:", deal["score"])
    print("-" * 30)