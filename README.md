Based on the final project guidelines and your team of 3 members — **Lizi**, **Giorgi**, and **Lasha** — here's a clear and fair task breakdown for the **E-Commerce Price Monitoring System (Option A)** that matches the required project structure and grading criteria.

---

### 👩‍💻 Lizi – **Frontend, Reporting, and CLI**

Focus on user interface, visualizations, and report generation.

#### **Responsibilities**

* `cli/interface.py`, `cli/commands.py`: Interactive CLI with filters and options.
* `analysis/reports.py`: Generate HTML and CLI reports.
* `analysis/statistics.py`, `trends.py`: Data analysis and trend graphs using `matplotlib`, `seaborn`.
* `data_output/reports/`: Create and manage output reports.
* `docs/user_guide.md`: Write clear user instructions with screenshots/examples.
* Testing/reporting CLI components.
* Documentation formatting and polish.

#### **Tech**

* `Click`, `argparse`, `matplotlib`, `pandas`, `seaborn`.

---

### 👨‍💻 Giorgi – **Scraping System Developer**

Handle all website scraping, scraping logic, and dynamic content extraction.

#### **Responsibilities**

* `scrapers/static_scraper.py`: BeautifulSoup scrapers for Amazon/eBay.
* `scrapers/selenium_scraper.py`: Selenium automation for dynamic site (3rd platform).
* `scrapers/scrapy_crawler/`: Scrapy-based crawler implementation.
* Anti-bot: session handling, user-agent rotation, error/retry logic.
* `utils/helpers.py`, `utils/config.py`, `utils/logger.py`: Logging, config loading, etc.
* `docs/api_reference.md`: Describe scraper modules, usage.

#### **Tech**

* `requests`, `BeautifulSoup4`, `Selenium`, `Scrapy`, `fake_useragent`, `time`, `random`.

---

### 👨‍💻 Lasha – **Architecture, Data Management, and Concurrency**

Focus on backend logic, database, and performance.

#### **Responsibilities**

* `data/models.py`, `data/database.py`: Define data models and database schema (PostgreSQL or SQLite).
* `data/processors.py`: Validate, clean, transform scraped data.
* `main.py`: Entry point logic, manage the overall pipeline.
* Concurrency: implement threading/multiprocessing for scrapers.
* `config/scrapers.yaml`, `settings.yaml`: Manage config files.
* `tests/`, especially unit tests for data/storage modules.
* `docs/architecture.md`: Document pipeline and backend design.

#### **Tech**

* `SQLite/PostgreSQL`, `pandas`, `multiprocessing`, `SQLAlchemy` or `sqlite3`.

---

### 📦 Shared Tasks

| Task                                 | Responsible                        |
| ------------------------------------ | ---------------------------------- |
| GitHub Repo Setup, Branches          | All (rotating)                     |
| README.md, CONTRIBUTIONS.md          | All                                |
| Code Reviews & Merge Requests        | All                                |
| Final Testing & Bug Fixing           | All                                |
| Final Video Demonstration (8–12 min) | All (shared voice or script parts) |

---

### ✅ Final Notes

* **Workflow**: Follow a Git branching model (e.g., `lizi-cli`, `giorgi-scrapers`, `lasha-backend`), and merge to `main` via PRs.
* **Communication**: Use GitHub issues or a group chat to sync progress.
* **Milestones**:

  * **Week 1**: Everyone sets up their base modules.
  * **Week 2**: Midpoint integration + real data scrape + database.
  * **Week 3**: CLI, Reports, UI polish + testing.

---
Git link "https://github.com/Giorgi-77/Data_Scraping_Final.git"
Let me know if you'd like a GitHub `CONTRIBUTIONS.md` file template based on this division.
