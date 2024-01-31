import requests
from datetime import timedelta


standings_url = "https://www.basketball-reference.com/leagues/NBA_2024_standings.html"
data = requests.get(standings_url)

# See how much time I have left to make another request
if data.status_code == 429:
    print("Too many requests, try again after", str(timedelta(seconds = int(data.headers["Retry-After"]))), "hours")

else:
    print("You're good")