import requests
from bs4 import BeautifulSoup

URL = (
    "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"
)

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup)

all_movies = soup.select("h2")

with open("movies.txt", mode="w") as file:
    file.write("idx) title (score)\n")
    for idx, movie in enumerate(all_movies):
        title = movie.select_one("a")
        score = movie.select_one(".tMeterScore")
        if title and score:
            file.write(f"{idx + 1}) {title.getText()} ({score.getText()})\n")
