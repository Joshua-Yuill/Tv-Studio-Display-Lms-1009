import serial
import time
import requests as r
from datetime import datetime

API_KEY = "1c074bd08729417e8a860b56970af6ae"

API_KEY_WEATHER = "9c54407c094061e37db595e0d4c728be"

NightMode = False

try:
    conn = serial.Serial("COM3", 9600)
except:
    conn = ""

delay = 0.7

def displaySetup():
    conn.write("<ID**><MC>\r\n".encode("ascii")) # Setting color mode on both displays
    time.sleep(delay)
    conn.write("<ID02><HG><FU>\r\n".encode("ascii")) # Setting the color "High Green" and setting it to display time on display ID 2
    time.sleep(delay)
    conn.write("<ID02><HG><M2>\r\n".encode("ascii")) # Setting the color "High Green" and setting it to display time on display ID 2
    time.sleep(delay)
    conn.write("<ID01><HG>\r\n".encode("ascii")) # Setting display ID 1 to 12hr time format
    time.sleep(delay)

def nightMode(timeN):
    if NightMode == False:
        conn.write("<ID01><LG>\r\n".encode("ascii"))
        time.sleep(delay)
        conn.write("<ID02><LY>\r\n".encode("ascii")) 
        time.sleep(delay)
        conn.write("<T{}>\r\n".format(timeN).encode("ascii"))
    else:
        conn.write("<T{}>\r\n".format(timeN).encode("ascii"))

def getNews():
    errored = False
    Headlines = []
    try:
        response = r.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=" + API_KEY)
        if errored == True:
            conn.write("<ID01><HG>\r\n".encode("ascii"))
            errored = False
        NResponse = response.json()
        for i in NResponse['articles']:
            Headlines.append(i['title'])
    except:
        Headlines = []
        Headlines.append("Offline")
        conn.write("<ID01><HR>Offline\r\n".encode("ascii"))
        print('\a')
    return Headlines

def getTime():
    try:
        response = r.get("http://worldtimeapi.org/api/ip")
        TResponse = response.json()
        return datetime.utcfromtimestamp(TResponse['unixtime']).strftime('%H%M%S')
    except:
        current_time = datetime.now().strftime("%H%M%S")
        return current_time
    
def getWeather():
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
	        "latitude": 51.4416,
	        "longitude": 0.1487,
	        "hourly": "temperature_2m",
	        "timezone": "Europe/London",
	        "forecast_days": 1
        }
        responses = openmeteo.weather_api(url, params=params)
        return responses
    except:
        return "Offline"

    
def displayTime(timeN):
    conn.write("<ID02><M2>\r\n".encode("ascii")) # Setting display ID 1 to 24hr time format
    time.sleep(delay)
    conn.write("<T{}>\r\n".format(timeN).encode("ascii"))

def displayNews(headlines):
    for i in headlines:
        conn.write("<ID01><HY>\r\n".encode("ascii"))
        time.sleep(0.5)
        conn.write("<ID01><HY>{}\r\n".format(i).replace(u"\u2018", "'").replace(u"\u2019", "'").encode("ascii", "ignore"))
        time.sleep(8)

def main():
    displaySetup()
    while True:
        if datetime.now().hour >= 22 or datetime.now().hour <= 8:
            nightMode(getTime())
            NightMode = True
            time.sleep(480)
        else:
            NightMode = False
            displayTime(getTime())
            displayNews(getNews())

main()