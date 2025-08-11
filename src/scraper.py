import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://news.ycombinator.com/news"

def scrape_page(url):
    """Scrape a single page of Hacker News and return a list of dictionaries."""
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    stories = soup.find_all("tr", class_="athing")
    data = []

    for story in stories:
        title_tag = story.find("span", class_="titleline").a
        title = title_tag.get_text(strip=True)
        link = title_tag["href"]

        subtext = story.find_next_sibling("tr").find("td", class_="subtext")

        score_tag = subtext.find("span", class_="score")
        score = score_tag.get_text(strip=True) if score_tag else "0 points"

        author_tag = subtext.find("a", class_="hnuser")
        author = author_tag.get_text(strip=True) if author_tag else "N/A"

        age_tag = subtext.find("span", class_="age")
        age = age_tag.get_text(strip=True) if age_tag else "N/A"

        comment_tag = subtext.find_all("a")[-1]
        comments = comment_tag.get_text(strip=True)
        if "comment" not in comments:
            comments = "0 comments"

        data.append({
            "Title": title,
            "Link": link,
            "Score": score,
            "Author": author,
            "Age": age,
            "Comments": comments
        })

    return data

def scrape_multiple_pages(pages=2):
    """Scrape multiple pages of Hacker News."""
    all_data = []
    url = BASE_URL

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        page_data = scrape_page(url)
        all_data.extend(page_data)

        # Find the link to the next page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        more_link = soup.find("a", string="More")
        if more_link:
            url = "https://news.ycombinator.com/" + more_link["href"]
        else:
            break

        time.sleep(1)  # polite delay

    return all_data

if __name__ == "__main__":
    # Change pages=3 if you want more pages
    results = scrape_multiple_pages(pages=3)

    # Print results
    for item in results:
        print(f"Title: {item['Title']}")
        print(f"Link: {item['Link']}")
        print(f"Score: {item['Score']}")
        print(f"Author: {item['Author']}")
        print(f"Age: {item['Age']}")
        print(f"Comments: {item['Comments']}")
        print("-" * 80)

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv("data/output.csv", index=False)

    # Save to JSON
    df.to_json("data/output.json", orient="records", indent=4)

    print("\n✅ Data saved to data/output.csv and data/output.json")
