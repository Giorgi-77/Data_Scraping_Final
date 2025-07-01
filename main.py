# -------------------- main.py (FINAL VERSION) --------------------
import os
import argparse
import pandas as pd
from src.scrapers.static_scraper import StaticScraper
from src.scrapers.selenium_scraper import SeleniumScraper
from src.scrapers.amazon_scraper import AmazonScraper
from src.scrapers.scrapy_crawler.newegg_spider import NeweggSeleniumScraper
from src.scrapers.scrapy_runner import run_scrapy_spider
from src.data.models import create_tables
from src.utils.logger import logger
from src.data.database import count_items, get_all_items
import matplotlib.pyplot as plt


def run_all_scrapers():
    logger.info("Creating database tables...")
    create_tables()

    logger.info("Running Amazon scraper...")
    amazon_scraper = AmazonScraper()
    amazon_scraper.run()

    logger.info("Running eBay scraper...")
    ebay_scraper = SeleniumScraper()
    ebay_scraper.run()

    logger.info("Running Newegg scraper...")
    newegg_scraper = NeweggSeleniumScraper()
    newegg_scraper.run()

    logger.info("Running Scrapy spider (QuotesToScrape)...")
    run_scrapy_spider()


def generate_report():
    logger.info("Generating final report...")
    items = get_all_items()
    df = pd.DataFrame(items, columns=["id", "title", "price"])
    df.drop_duplicates(subset="title", inplace=True)
    df = df[df["title"].str.strip().astype(bool)]

    os.makedirs("data_output/reports", exist_ok=True)
    df.to_csv("data_output/reports/item_summary.csv", index=False)

    # Plot price distribution (basic bar chart for top 10 prices)
    clean_prices = df[df['price'] != "N/A"].copy()
    clean_prices['price_val'] = clean_prices['price'].str.replace("$", "").str.replace(",", "").astype(float, errors='ignore')
    top_prices = clean_prices.nlargest(10, 'price_val')

    plt.figure(figsize=(10, 6))
    plt.barh(top_prices['title'], top_prices['price_val'])
    plt.xlabel("Price ($)")
    plt.title("Top 10 Most Expensive Items")
    plt.tight_layout()
    plt.savefig("data_output/reports/top_10_prices.png")

    print(f"\n✅ Final Report")
    print(f"Cleaned, unique items: {len(df)}")
    print("Saved: data_output/reports/item_summary.csv")
    logger.info(f"Final cleaned item count: {len(df)}")


def main():
    parser = argparse.ArgumentParser(description="Data Scraping Final Project")
    parser.add_argument("--scrape", action="store_true", help="Run all scrapers")
    parser.add_argument("--report", action="store_true", help="Generate report")
    args = parser.parse_args()

    if args.scrape:
        run_all_scrapers()
    if args.report:
        generate_report()
    if not args.scrape and not args.report:
        parser.print_help()


if __name__ == "__main__":
    main()
