from config import SOURCE_URL, SNAPSHOT_FILE, SLACK_WEBHOOK_URL
from fetcher import fetch_html, save_html_to_file
from collectors.bstock_collector import BStockCollector
from filters import filter_relevant_deals
from scoring import add_scores_to_deals
from reporting import print_report, save_report_to_file, save_deals_to_csv
from slack_notifier import build_slack_message, send_slack_message


def main():
    print("Downloading source page...")
    html_content = fetch_html(SOURCE_URL)
    save_html_to_file(html_content, SNAPSHOT_FILE)
    print(f"Saved snapshot to: {SNAPSHOT_FILE}")

    collector = BStockCollector("app/sample_page.html")
    deals = collector.collect()
    print(f"Collected deals: {len(deals)}")

    relevant_deals = filter_relevant_deals(deals)
    print(f"Relevant deals: {len(relevant_deals)}")

    scored_deals = add_scores_to_deals(relevant_deals)
    print(f"Scored deals: {len(scored_deals)}")

    sorted_deals = sorted(
        scored_deals,
        key=lambda deal: deal["score"],
        reverse=True
    )

    top_deals = sorted_deals[:3]
    print(f"Top deals selected: {len(top_deals)}")

    print_report(top_deals)
    save_report_to_file(top_deals, "output/daily_report.txt")
    save_deals_to_csv(top_deals, "output/top_deals.csv")

    if SLACK_WEBHOOK_URL:
        slack_message = build_slack_message(top_deals)
        send_slack_message(SLACK_WEBHOOK_URL, slack_message)
        print("Slack message sent successfully.")
    else:
        print("Slack webhook URL not set. Skipping Slack notification.")

    print("\nFiles created:")
    print("- snapshots/source_page.html")
    print("- output/daily_report.txt")
    print("- output/top_deals.csv")


if __name__ == "__main__":
    main()