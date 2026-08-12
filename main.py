import requests
from bs4 import BeautifulSoup

URL = (
    "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.select("div.block-countdown")

rows = []
rank = 0
for movie in all_movies:
    title = movie.select_one("a.meta-title")
    score = movie.select_one("span.tMeterScore")
    if title and score:
        rank += 1
        rows.append(f"{rank}) {title.getText().strip()} ({score.getText().strip()})\n")

if not rows:
    raise SystemExit(
        "Parsed 0 movies. The page markup may have changed. "
        "movies.txt was left untouched."
    )

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write("idx) title (score)\n")
    for row in rows:
        file.write(row)

print(f"Wrote {len(rows)} movies to movies.txt")
