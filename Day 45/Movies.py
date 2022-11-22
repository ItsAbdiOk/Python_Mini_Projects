from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")


Movies_list = []
Movies = soup.find_all(class_="title", name = "h3")
for movie in Movies:
    Movies_list.append(movie.getText())

file = open("Movies.txt", "w", encoding="utf-8")
for movie in Movies_list:
    file.write(movie + "\n")
    print (movie)

file.close()

  

