from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd
from flask import Flask, render_template

url = "https://carmelclaylibrary.org"

activities = []
time = []
description = []
links = []

try:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    events = soup.find_all('div', class_='amev-event')

    for event in events:
        event_title = event.find('div', class_="amev-event-title")
        activities.append(event_title.text)

        event_time = event.find('div', class_="amev-event-time headingtext")
        time.append(event_time.text)

        event_desc = event.find('div', class_="amev-event-description-full")
        description.append(event_desc.text)

        event_register = event.find('button', class_="button eventRegButton registerForEvent")
        links.append(event_register)

    eventData = pd.DataFrame(
        {'Event Name': activities,
         'Time': time,
         'Description': description,
         'Register': links
            }
        )
    print(eventData)
    eventData.to_csv('CCPL_Events_Info.csv')
except:
    print("The program was unable to parse the data.")



app = Flask(__name__)
@app.route('/')
def CCPL_Events(): # don't forget to redefine every new return command!
    items = pandas.read_csv('/Users/shuningliu/Documents/GitHub/Python-Web-Crawler-Class-Course-Project/CCPL_Events_Info.csv') #Click on the file path and tap on 'copy filename as pathname'.
    return CCPL_Events_Info.to_html()

if __name__ == '__main__':
    app.run()
if __name__ == '__main__':
    app.run(debug = True)
