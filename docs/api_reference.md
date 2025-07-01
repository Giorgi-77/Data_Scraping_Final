# Scraper API Reference

> Detailed descriptions of all scraper modules, utilities, and their public interfaces.

---

## Table of Contents

1. [Utilities](#utilities)
   1.1 [Config Loader](#config-loader)
   1.2 [Logger](#logger)
   1.3 [Helpers](#helpers)
   1.4 [Ethical Checks](#ethical-checks)
2. [Core Scraper Interfaces](#core-scraper-interfaces)
   2.1 [BaseScraper](#basescraper)
   2.2 [StaticScraper](#staticscraper)
   2.3 [SeleniumScraper](#seleniumscraper)
   2.4 [AmazonScraper](#amazonscraper)
3. [Scrapy Runner & Crawler](#scrapy-runner--crawler)
   3.1 [Scrapy Runner](#scrapy-runner)
   3.2 [Spiders](#spiders)
   3.3 [Pipelines](#pipelines)

---

## Utilities

### Config Loader

```python
# src/utils/config.py

def load_settings(path: str) -> dict:
    """
    Load YAML settings from the given file path.

    Parameters:
      path (str): Path to a .yaml file.

    Returns:
      dict: Parsed settings.
    """
```

### Logger

```python
# src/utils/logger.py

def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters:
      name (str): Logger name (e.g., module name).

    Returns:
      logging.Logger: Configured logger instance.
    """
```

### Helpers

```python
# src/utils/helpers.py

def rotate_user_agent() -> str:
    """
    Pick a random User-Agent string for requests.

    Returns:
      str: A User-Agent header value.
    """
```

### Ethical Checks

```python
# src/utils/ethical.py

def is_allowed_domain(url: str, allowed_domains: list[str]) -> bool:
    """
    Check if the URL’s domain is in the allowed list.

    Parameters:
      url (str): The URL to check.
      allowed_domains (list[str]): Domains you permit scraping.

    Returns:
      bool: True if allowed, False otherwise.
    """
```

---

## Core Scraper Interfaces

### BaseScraper

```python
# src/scrapers/base_scraper.py

class BaseScraper:
    """
    Abstract base class defining the scraping interface.
    """

    def fetch(self, url: str) -> requests.Response:
        """
        Perform an HTTP GET on the URL.

        Parameters:
          url (str): Target URL.

        Returns:
          requests.Response: The HTTP response.
        """
```

### StaticScraper

```python
# src/scrapers/static_scraper.py

class StaticScraper(BaseScraper):
    """
    Scraper for static HTML sites using BeautifulSoup.
    """

    def parse(self, html: str) -> list[dict]:
        """
        Extract structured data from raw HTML.

        Parameters:
          html (str): Page HTML content.

        Returns:
          list[dict]: List of item dicts.
        """
```

### SeleniumScraper

```python
# src/scrapers/selenium_scraper.py

class SeleniumScraper(BaseScraper):
    """
    Scraper for dynamic pages driven by JavaScript.
    """

    def fetch(self, url: str) -> str:
        """
        Load the page in a headless browser and return rendered HTML.

        Parameters:
          url (str): Target URL.

        Returns:
          str: Rendered HTML content.
        """
```

### AmazonScraper

```python
# src/scrapers/amazon_scraper.py

class AmazonScraper(StaticScraper):
    """
    StaticScraper subclass with Amazon-specific parsing.
    """

    def parse(self, html: str) -> list[dict]:
        """
        Parse Amazon product listings and return details.

        Returns:
          list[dict]: Each dict contains title, price, rating, url.
        """
```

---

## Scrapy Runner & Crawler

### Scrapy Runner

```python
# src/scrapers/scrapy_runner.py

def run_crawler(spider_name: str, settings: dict) -> None:
    """
    Invoke Scrapy to run a named spider.

    Parameters:
      spider_name (str): Name of the spider class to run.
      settings (dict): Scrapy settings overrides.
    """
```

### Spiders

```python
# src/scrapers/scrapy_crawler/aliexpress_spider.py

class AliExpressSpider(scrapy.Spider):
    """
    Scrapy spider to crawl AliExpress listings.
    """
    name = "aliexpress"
    start_urls = []  # define starting URLs

    def parse(self, response):
        """
        Parse listing page and yield items.

        Parameters:
          response (scrapy.http.Response): The page response.
        """
```

*(Repeat similarly for `NeweggSpider`, `QuotesSpider`, and `GenericSpider`.)*

### Pipelines

```python
# src/scrapers/scrapy_crawler/pipelines.py

class PricePipeline:
    """
    Scrapy pipeline for cleaning and saving scraped items.
    """

    def process_item(self, item: dict, spider):
        """
        Clean item fields and store to DB or CSV.

        Parameters:
          item (dict): Raw item from spider.
          spider (scrapy.Spider): Spider instance.

        Returns:
          dict: Cleaned item.
        """
```
