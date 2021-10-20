import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/cc4e93311b537126218a1d9a0dc33295fd3f3d0c8fe0965a4b8eab0fb00e7d39"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open("C:/Users/MANASVI/Desktop/weather.png")
img = img.resize((150,150))
img = ImageTk  .PhotoImage(img)

import geocoder
g = geocoder.ip('me')
print(g.latlng)



def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--kyTeL").text
    temprature = soup.find('span', class_="CurrentConditions--tempValue--3a50n").text
    weatherPrediction = soup.find('div' , class_ = "CurrentConditions--phraseValue--2Z18W").text
    weatherPredictionDetails = soup.find('div',class_ ="CurrentConditions--precipValue--3nxCj").text
    templocationLabel.after(60000,getWeather)
    master.update()


    locationLabel.config(text=location)
    templocationLabel.config(text=temprature)
    weatherPredictionLabel.config(text=weatherPrediction)


locationLabel = Label(master,font=("Calibri bold",20),bg = "white")
locationLabel.grid(row=0,sticky="N",padx = 100)
templocationLabel = Label(master,font=("Calibri bold",70),bg = "white")
templocationLabel.grid(row=1,sticky="N",padx = 40)
Label(master , image =img,bg="white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(master,font=("Calibri bold",15) , bg="white")
weatherPredictionLabel.grid(row=2 , sticky="W",padx=40)


getWeather()
master.mainloop()
