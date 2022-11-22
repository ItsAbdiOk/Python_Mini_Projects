from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")

#declare a list to store the score


articles = soup.find_all(class_="title", name = "h3")

print(articles)
