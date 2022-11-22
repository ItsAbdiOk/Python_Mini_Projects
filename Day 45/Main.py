from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_wep_page = response.text
soup = BeautifulSoup(yc_wep_page, "html.parser")
#declare a list to store the score
Text = []
Links = []
Points = []
HighestText = ""

articles = soup.find_all(class_="titleline", name = "span")
for article in articles:
    Text = article.getText()
    Links = article.find("a")["href"]

#Getting all the points
Points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#Find the article with the highest points
HighestPoints = max(Points)
HighestIndex = Points.index(HighestPoints)
HighestText = articles[HighestIndex].getText()
HighestLink = articles[HighestIndex].find("a")["href"]
print(HighestText)
print(HighestLink)
print(HighestPoints)


    

