# E-Commerce Price Monitoring System

[View the GitHub repository »](https://github.com/Giorgi-77/Data_Scraping_Final)

Based on the final project guidelines and our team of three members — **Lizi**, **Giorgi**, and **Lasha** — here’s a clear and fair task breakdown for **Option A** that matches the required project structure and grading criteria.

---

### 👩‍💻 Lizi – **Frontend, Reporting, and CLI**

Focus on user interface, visualizations, and report generation.

#### Responsibilities

- `src/cli/interface.py`, `src/cli/commands.py`: Interactive CLI with filters and options  
- `src/analysis/reports.py`: Generate HTML and CSV/JSON reports  
- `src/analysis/statistics.py`, `src/analysis/trends.py`: Data analysis and trend graphs using `pandas`, `matplotlib`  
- `data_output/reports/`: Create and manage output reports  
- `docs/user_guide.md`: Write clear user instructions with examples and screenshots  
- Testing/reporting CLI components  
- Documentation formatting and polish  

#### Tech

- `argparse`, `pandas`, `matplotlib`, `seaborn`, `csv`, `json`

---

### 👨‍💻 Giorgi – **Scraping System Developer**

Handle all website scraping, scraping logic, and dynamic content extraction.

#### Responsibilities

- `src/scrapers/static_scraper.py`: BeautifulSoup scrapers for static pages  
- `src/scrapers/selenium_scraper.py`: Selenium automation for JavaScript-driven pages  
- `src/scrapers/scrapy_crawler/`: Scrapy-based crawler implementation (spiders, pipelines)  
- Anti-bot: session handling, user-agent rotation, error/retry logic  
- `src/utils/helpers.py`, `src/utils/config.py`, `src/utils/logger.py`: Logging, config loading, UA rotation, ethical checks  
- `docs/api_reference.md`: Describe scraper modules, usage, and public interfaces  

#### Tech

- `requests`, `BeautifulSoup4`, `Selenium`, `Scrapy`, `fake_useragent`, `time`, `random`

---

### 👨‍💻 Lasha – **Architecture, Data Management, and Concurrency**

Focus on backend logic, database, and performance.

#### Responsibilities

- `src/data/models.py`, `src/data/database.py`: Define data models and database schema (SQLite or PostgreSQL)  
- `src/data/processors.py`: Validate, clean, and transform scraped data  
- `main.py`: Entry point orchestration of the full pipeline  
- Concurrency: implement threading / multiprocessing for parallel scrapes  
- `config/scrapers.yaml`, `config/settings.yaml`: Manage configuration files  
- `tests/`: Unit and integration tests for data/storage modules  
- `docs/architecture.md`: Document pipeline design, ER diagrams, and flow  

#### Tech

- `SQLite` / `PostgreSQL`, `SQLAlchemy`, `pandas`, `multiprocessing`, `threading`

---

### 📦 Shared Tasks

| Task                                 | Responsible              |
| ------------------------------------ | ------------------------ |
| GitHub Repo Setup & Branching       | All (rotate ownership)   |
| `README.md` & `CONTRIBUTIONS.md`    | All                      |
| Code Reviews & Merge Requests       | All                      |
| Final Testing & Bug Fixing          | All                      |
| Final Video Demonstration (8–12 min) | All (shared script roles)|

---

### ✅ Final Notes

- **Workflow**: Each feature on its own branch (`lizi-cli`, `giorgi-scrapers`, `lasha-backend`), PR to `main`  
- **Communication**: Use GitHub Issues and Slack/Teams for real-time sync  
- **Milestones**:  
  1. **Week 1**: Scaffold + static scrapers + DB models  
  2. **Week 2**: Dynamic scraping + concurrency + initial tests  
  3. **Week 3**: CLI, reports, docs, full testing + polish  

---

_For full details and the latest updates, see our repository on GitHub:_  
**https://github.com/Giorgi-77/Data_Scraping_Final**  
