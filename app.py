import json

from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests
from urllib.request import urlretrieve, urlopen
from pprint import PrettyPrinter
import xml.etree.ElementTree as ET
app = Flask(__name__)
pp = PrettyPrinter()


apiKey = "WYnpJOANhxzSik0UJ7Ewac5MOqssVJH0l10JfVAI"

@app.route('/apod')
def apod():
    url_apod = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':apiKey
    }

    response = requests.get(url_apod, params=params).json()
    json_obj = json.dumps(response)
    dict = json.loads(json_obj)
    apod = {
        "date": dict['date'],
         "explanation": dict['explanation'],
        "url": dict['url'],
        "title": dict['title']

    }
    return render_template('apod.html', apod=apod)
@app.route('/epic')
def epic():
    url_epic = "https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY"
    params = {
        'api_key': apiKey
    }
    response = requests.get(url_epic, params=params).json()
    json_obj = json.dumps(response)
    dict = json.loads(json_obj)

    YEAR = '2023'
    MONTH = '05'
    DAY = '21'
    IMAGE_ID = 'epic_1b_20230521010436'
    url_img = "https://epic.gsfc.nasa.gov/archive/natural/"
    url_img = url_img + YEAR + '/' + MONTH + '/' + DAY
    url_img = url_img + '/png'
    url_img = url_img + '/' + IMAGE_ID + '.png'
    for d in dict:
        epic = {
            "date":d.get('date'),
            "coordinates":d.get('centroid_coordinates'),
            "url":url_img
        }
    return render_template('epic.html',epic=epic)


@app.route('/')
def index():
    URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'api_key': apiKey,
        'start_date': '2020-01-22',
        'end_date': '2020-01-23'
    }

    response = requests.get(URL_NeoFeed, params=params).json()
    json_obj = json.dumps(response)
    dict = json.loads(json_obj)
    print(dict['links']['self'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
