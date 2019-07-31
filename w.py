#!/usr/bin/python3

import requests
import sys
import slack
import os
import json

web_hook_url = (
    "https://hooks.slack.com/services/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"
)


city = "Islamabad"
url = "http://api.openweathermap.org/data/2.5/weather?q={},pk&units=metric&APPID=d58366f88671fbbb22b4cc69734c45ba".format(
    city
)

res = requests.get(url)

data = res.json()
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]


slack_city = {"text": city.upper()}
slack_temp = {"text": "Temperature : {}deg Celsius".format(temp)}
slack_windspeed = {"text": "Wind Speed: {}m/s".format(wind_speed)}
slack_humidity = {"text": "Humidity : {}%".format(humidity)}
slack_description = {"text": "Description : {}".format(description)}


requests.post(web_hook_url, data=json.dumps(slack_city))
requests.post(web_hook_url, data=json.dumps(slack_temp))
requests.post(web_hook_url, data=json.dumps(slack_windspeed))
requests.post(web_hook_url, data=json.dumps(slack_humidity))
requests.post(web_hook_url, data=json.dumps(slack_description))

