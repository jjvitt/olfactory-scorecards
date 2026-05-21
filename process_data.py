name: Weekly Scorecard Refresh

on:
  schedule:
    # Every Monday at 7:00am ET (12:00 UTC)
    - cron: '0 12 * * 1'
  workflow_dispatch:  # also allows manual trigger from GitHub UI

jobs:
  refresh:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run scorecard refresh
        env:
          SHOPIFY_STORE:            ${{ secrets.SHOPIFY_STORE }}
          SHOPIFY_TOKEN:            ${{ secrets.SHOPIFY_TOKEN }}
          GOOGLE_CREDS_JSON:        ${{ secrets.GOOGLE_CREDS_JSON }}
          RIPPLING_DRIVE_FOLDER_ID: ${{ secrets.RIPPLING_DRIVE_FOLDER_ID }}
          HB_SHEET_ID:              ${{ secrets.HB_SHEET_ID }}
          NETLIFY_TOKEN:            ${{ secrets.NETLIFY_TOKEN }}
          NETLIFY_SITE_ID:          ${{ secrets.NETLIFY_SITE_ID }}
        run: python process_data.py

      - name: Notify on failure
        if: failure()
        run: echo "Scorecard refresh failed — check logs above"
