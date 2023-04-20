import requests
import json

query = input("What kind of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-03-20&sortBy=publishedAt&apiKey=c6984ca9135243b79b6b6e1d929911ab"

r = requests.get(url)
news = json.loads(r.text)


for article in news["articles"]:
    print(f'Title - {article["title"]}')
    print(f'Description - {article["description"]}\n')
