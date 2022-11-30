from bs4 import BeautifulSoup
import requests
import spotipy
def checkDate(Date):#this Checks to see if the date is valid
    if Date[0:4].isdigit() == False or Date[5:7].isdigit() == False or Date[8:10].isdigit() == False:
        print("Please Use Numbers")
        exit()
    elif int(Date[0:4]) < 1958 or int(Date[0:4]) > 2018:
        print("Please enter a year between 1958 and 2018")
        exit()
    elif Date[4] != "-" or Date[7] != "-":
        print("Please use the format YYYY-MM-DD")
        exit()
    elif int(Date[5:7]) < 1 or int(Date[5:7]) > 12:
        print("Please enter a valid month")
        exit()
    elif int(Date[8:10]) < 1 or int(Date[8:10]) > 31:
        print("Please enter a valid day")
        exit()
  
def scrapeBillboard(Date):#this scrapes the billboard website for the top 10 songs of the year
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{Date}/#")
    BillBoard = response.text
    soup = BeautifulSoup(BillBoard, "html.parser")
    #declare a list to store the score
    SongsList = []
    Songs = soup.find_all("h3", class_="a-no-trucate")
    for song in Songs:
        SongsList.append(song.getText().strip())
    return SongsList

def SearchinSpotify(SongsList):#this searches spotify for the songs
    SpotifyList = []
    for song in SongsList:




UserInput = input("Please enter a date in the format YYYY-MM-DD: ")
checkDate(UserInput)
SongsList = scrapeBillboard(UserInput)

