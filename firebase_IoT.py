import pyrebase
import sensors
import urllib.request
from time import sleep
import _pickle
import os
import requests
import datetime


def post_sensor(datas):
    while len(datas)>0:
        data = datas.pop()
        db.child("Jonathan's Home").child(data.pop('timestamp')).set(data)
    if os.path.exists('backup.pkl'):
        os.remove('backup.pkl')
    if need_update_sea_level_pressure:
        sea_level_pressure = fetch_sea_level_pressure()


def fetch_sea_level_pressure():
    need_update_sea_level_pressure = False
    req = requests.get(url).json()
    return req.get('main').get('pressure')


def check_internet_connection():
    try:
        response = urllib.request.urlopen('http://google.com',timeout=3)
        return True
    except urllib.request.URLError:
        return False


def save_data(obj):
    with open('backup.pkl','wb') as output:
        _pickle.dump(obj,output,-1)


def main():
    last_update = datetime.datetime.now().hour
    while(True):
        now = datetime.datetime.now().hour
        if last_update != now:
            need_update_sea_level_pressure = True
            last_update = now
        data.append(sensors.update_sensors(sea_level_pressure))
        if check_internet_connection():
            post_sensor(data)
        else:
            save_data(data)
        sleep(300)


if __name__ == '__main__':
    config = {
        "apiKey": "AIzaSyAjdp1k-TaUh9DyzxDKoT1PLlaBjiPijGI",
        "authDomain": "maxitondb.firebaseapp.com",
        "databaseURL": "https://maxitondb.firebaseio.com/",
        "storageBucket": "gs://maxitondb.appspot.com"
    }

    url = 'https://api.openweathermap.org/data/2.5/weather?id=1880251&appid=61349b0ffaf068c53c6e5fee3ccae0db'

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    data = []
    need_update_sea_level_pressure = True
    print(f'There are {len(data)} readings not push to internet')
    if check_internet_connection():
        sea_level_pressure = fetch_sea_level_pressure()
    else:
        sea_level_pressure = 1013

    try:
        with open('backup.pkl', 'rb') as input:
            data = _pickle.load(input)
    except:
        pass

    main()