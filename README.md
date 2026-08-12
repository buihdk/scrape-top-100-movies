## Netflix's best movies

Scraping the [Rotten Tomatoes](https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/) 🍅 website using *BeautifulSoup* to obtain a list of the best Netflix movies to watch right now.

Scraped data is then written into `movies.txt` file in the format `idx) title (score)`.

With this curated list at your fingertips, you'll never again find yourself endlessly scrolling in search of the perfect movie to watch.

## Usage

Install the dependencies.

```
pip install -r requirements.txt
```

Run the scraper.

```
python main.py
```

The list is written to `movies.txt`. The page holds about 80 movies today.
