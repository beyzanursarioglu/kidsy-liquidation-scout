# Kidsy Liquidation Scout

Kidsy Liquidation Scout is a Python MVP project that collects liquidation deal data, filters listings relevant to Kidsy, scores the best opportunities, and generates a daily report.

## Current MVP Features

- Downloads a source page and saves a local HTML snapshot
- Parses deal data from an HTML source
- Filters relevant baby/kids deals
- Scores and ranks deals
- Generates a text report
- Exports top deals to CSV

## Project Structure

kidsy-liquidation-scout/
- app/
  - collectors/
    - __init__.py
    - base_collector.py
    - bstock_collector.py
    - html_collector.py
    - sample_collector.py
  - config.py
  - data.py
  - fetcher.py
  - filters.py
  - main.py
  - reporting.py
  - sample_page.html
  - scoring.py
- output/
  - daily_report.txt
  - top_deals.csv
- snapshots/
  - source_page.html
- requirements.txt
- README.md

## How to Run

### 1. Install dependencies

pip3 install -r requirements.txt

### 2. Run the project

python3 app/main.py

## Output Files

After running the project, these files are created:

- snapshots/source_page.html
- output/daily_report.txt
- output/top_deals.csv

## Current Workflow

1. Download source page
2. Save HTML snapshot
3. Collect deals from source
4. Filter relevant deals
5. Score and rank deals
6. Generate report and CSV output

## Next Steps

- Add more source-specific collectors
- Improve scoring logic
- Add Slack or email reporting
- Support real liquidation marketplace HTML structures
- Add logging and error tracking