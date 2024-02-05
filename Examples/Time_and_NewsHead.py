import serial
import time
import requests as r
from datetime import datetime

API_KEY = "1c074bd08729417e8a860b56970af6ae"

conn = serial.Serial("COM3", 9600)

delay = 0.7

def displaySetup():
    conn.write("<ID**><MC>\r\n".encode("ascii")) # Setting color mode on both displays
    time.sleep(delay)
    conn.write("<ID01><HR><FU>\r\n".encode("ascii")) # Setting the color "High Red" and setting it to display time on display ID 1
    time.sleep(delay)
    conn.write("<ID02><HG><FU>\r\n".encode("ascii")) # Setting the color "High Green" and setting it to display time on display ID 2
    time.sleep(delay)
    conn.write("<ID01><M2>\r\n".encode("ascii")) # Setting display ID 1 to 24hr time format
    time.sleep(delay)
    conn.write("<ID02><M1>\r\n".encode("ascii")) # Setting display ID 1 to 12hr time format
    time.sleep(delay)


def getNews():
    response = r.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=" + API_KEY)
    return response.json()

def getTime():
    try:
        response = r.get("http://worldtimeapi.org/api/ip")
        TResponse = response.json()
        return datetime.utcfromtimestamp(TResponse['unixtime']).strftime('%H%M%S')
    except:
        current_time = datetime.now().strftime("%H%M%S")
        return current_time

Headlines = []
NResponse = getNews()
for i in NResponse['articles']:
    Headlines.append(i['title'])


print(Headlines)
print(getTime())