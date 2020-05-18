from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd

url = "https://carmelclaylibrary.org"

activities = []
time = []
description = []
links = []

page = requests.get(url)
soup = BeautifulSoup('page.content', 'html.parser')

for data in soup:
    event_title = soup.find_all('div', class_='amev-event-title')
    event_time = soup.find_all('div', class_='amev-event-time headingtext')
    event_desc = soup.find_all('div', class_='amev-event-description-full')
    event_register = soup.find_all('button', class_='button eventRegButton')

    activities.append(event_title)
    time.append(event_time)
    description.append(event_desc)
    links.append(event_register)

eventData = pd.DataFrame(
    {'Event Name': activities,
     'Time': time,
     'Description': description,
     'Register': links
        }
    )
eventData.to_csv('CCPL_Events_Info.csv')
