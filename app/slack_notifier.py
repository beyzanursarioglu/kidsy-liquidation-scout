import requests


def build_slack_message(deals):
    lines = []
    lines.append("*Kidsy Liquidation Scout Report*")
    lines.append("")

    for i, deal in enumerate(deals, start=1):
        lines.append(f"*{i}. {deal['title']}*")
        lines.append(f"Price: ${deal['price']}")
        lines.append(f"Source: {deal['source']}")
        lines.append(f"Condition: {deal['condition']}")
        lines.append(f"Location: {deal['location']}")
        lines.append(f"Score: {deal['score']}")
        lines.append(f"URL: {deal['url']}")
        lines.append("")

    return "\n".join(lines)


def send_slack_message(webhook_url, message_text):
    payload = {
        "text": message_text
    }

    response = requests.post(webhook_url, json=payload, timeout=20)
    response.raise_for_status()

    return response