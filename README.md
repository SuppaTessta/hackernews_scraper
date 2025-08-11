# 📡 Hacker News Web Scraper

A Python-based web scraper that extracts the latest news posts from [Hacker News](https://news.ycombinator.com/), including:
- Title
- Link
- Score (points)
- Author
- Age (posted time)
- Number of comments

The scraper supports multi-page scraping, saves results to **CSV** and **JSON**, and prints them in the terminal.

---

## 📌 Features
- Scrapes **real-time data** from Hacker News.
- Extracts title, link, score, author, age, and comments.
- Handles **multiple pages** automatically.
- Saves results to:
  - `data/output.csv`
  - `data/output.json`
- Prints results in a clean, readable format.
- Error handling for missing data fields.
- Polite scraping delay to avoid overloading the site.

---

## 🛠 Tech Stack
- **Python 3.10+**
- [requests](https://pypi.org/project/requests/) – HTTP requests
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – HTML parsing
- [pandas](https://pandas.pydata.org/) – CSV/JSON export
- [lxml](https://pypi.org/project/lxml/) – Fast HTML parser backend

---

## 🚀 Installation & Usage

### 1. Clone this repository
```bash
git clone https://github.com/SuppaTessta/hackernews_scraper.git
cd hackernews_scraper
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the scraper
```bash
python src/scraper.py
```

---

## 📂 Output Files
After running the scraper, results are saved to:
- `data/output.csv`
- `data/output.json`

Example CSV output:
```csv
Title,Link,Score,Author,Age,Comments
Wikimedia Foundation Challenges UK Online Safety Act Regulations,https://wikimediafoundation.org/news/2025/08/11/wikimedia-foundation-challenges-uk-online-safety-act-regulations/,140 points,danso,1 hour ago,47 comments
OpenSSH Post-Quantum Cryptography,https://www.openssh.com/pq.html,144 points,throw0101d,2 hours ago,39 comments
I tried every todo app and ended up with a .txt file,https://www.al3rez.com/todo-txt-journey,17 points,al3rez,23 minutes ago,4 comments
```

Example JSON output:
```json
[
    {
        "Title": "Wikimedia Foundation Challenges UK Online Safety Act Regulations",
        "Link": "https://wikimediafoundation.org/news/2025/08/11/wikimedia-foundation-challenges-uk-online-safety-act-regulations/",
        "Score": "140 points",
        "Author": "danso",
        "Age": "1 hour ago",
        "Comments": "47 comments"
    },
    {
        "Title": "OpenSSH Post-Quantum Cryptography",
        "Link": "https://www.openssh.com/pq.html",
        "Score": "144 points",
        "Author": "throw0101d",
        "Age": "2 hours ago",
        "Comments": "39 comments"
    },
    {
        "Title": "I tried every todo app and ended up with a .txt file",
        "Link": "https://www.al3rez.com/todo-txt-journey",
        "Score": "17 points",
        "Author": "al3rez",
        "Age": "23 minutes ago",
        "Comments": "4 comments"
    }
]
```

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements
- Data provided by [Hacker News](https://news.ycombinator.com/).
- Built for educational and portfolio purposes.
