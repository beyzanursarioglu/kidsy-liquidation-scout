import csv
from datetime import datetime


def build_report_text(deals):
    lines = []

    lines.append("KIDSY LIQUIDATION SCOUT REPORT")
    lines.append("=" * 40)
    lines.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    for i, deal in enumerate(deals, start=1):
        lines.append(f"{i}. {deal['title']}")
        lines.append(f"   Price: ${deal['price']}")
        lines.append(f"   Source: {deal['source']}")
        lines.append(f"   Condition: {deal['condition']}")
        lines.append(f"   Location: {deal['location']}")
        lines.append(f"   Score: {deal['score']}")
        lines.append(f"   URL: {deal['url']}")

        if deal.get("reasons"):
            lines.append("   Why it matters:")
            for reason in deal["reasons"]:
                lines.append(f"   - {reason}")

        lines.append("")

    return "\n".join(lines)


def print_report(deals):
    report_text = build_report_text(deals)
    print(report_text)


def save_report_to_file(deals, file_path):
    report_text = build_report_text(deals)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report_text)


def save_deals_to_csv(deals, file_path):
    fieldnames = ["title", "price", "source", "condition", "location", "score", "reasons", "url"]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for deal in deals:
            writer.writerow({
                "title": deal["title"],
                "price": deal["price"],
                "source": deal["source"],
                "condition": deal["condition"],
                "location": deal["location"],
                "score": deal["score"],
                "reasons": "; ".join(deal.get("reasons", [])),
                "url": deal["url"]
            })