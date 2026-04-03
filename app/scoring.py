STRONG_SOURCES = [
    "B-Stock",
    "Liquidation.com",
    "Direct Liquidation"
]

STRONG_BRANDS = [
    "graco",
    "fisher-price",
    "baby jogger",
    "uppababy",
    "evenflo",
    "maxi-cosi",
    "britax",
    "munchkin",
    "regalo",
    "ingenuity"
]

RELEVANT_KEYWORDS = [
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

BAD_KEYWORDS = [
    "office",
    "furniture",
    "electronics",
    "laptop",
    "monitor"
]

RISK_KEYWORDS = [
    "mixed",
    "salvage",
    "damaged"
]

NEARBY_LOCATIONS = [
    "NJ",
    "PA",
    "CT",
    "NY",
    "New Jersey",
    "Pennsylvania",
    "Connecticut",
    "New York"
]


def score_deal(deal):
    score = 0
    reasons = []
    title_lower = deal["title"].lower()

    if any(keyword in title_lower for keyword in RELEVANT_KEYWORDS):
        score += 25
        reasons.append("Relevant baby/kids category")

    matched_brand = next((brand for brand in STRONG_BRANDS if brand in title_lower), None)
    if matched_brand:
        score += 20
        reasons.append(f"Strong brand match: {matched_brand}")

    if any(bad_word in title_lower for bad_word in BAD_KEYWORDS):
        score -= 25
        reasons.append("Contains less relevant category terms")

    if any(risk_word in title_lower for risk_word in RISK_KEYWORDS):
        score -= 15
        reasons.append("Contains risk-related terms")

    condition = deal["condition"].lower()

    if condition == "overstock":
        score += 20
        reasons.append("Overstock condition")
    elif condition == "returns":
        score += 10
        reasons.append("Returns condition")

    if deal["price"] > 0 and deal["price"] <= 1000:
        score += 10
        reasons.append("Attractive price point")
    elif deal["price"] == 0:
        score -= 10
        reasons.append("Missing or zero price")

    if deal["source"] in STRONG_SOURCES:
        score += 10
        reasons.append("Trusted source")

    if deal["location"] in NEARBY_LOCATIONS:
        score += 5
        reasons.append("Nearby location")

    return score, reasons


def add_scores_to_deals(deals):
    scored_deals = []

    for deal in deals:
        deal_copy = deal.copy()
        score, reasons = score_deal(deal_copy)
        deal_copy["score"] = score
        deal_copy["reasons"] = reasons
        scored_deals.append(deal_copy)

    return scored_deals