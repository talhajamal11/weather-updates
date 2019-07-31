#!/usr/bin/python3

import requests
import sys
import slack
import os
import json

web_hook_url = (
    "https://hooks.slack.com/services/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"
)

# SLACK_API_TOKEN = 'xoxb-7871756934-707612720407-NP0mKmHAPuUV7KVL4XAx8AZP'

# client = slack.WebClient(token=os.environ['xoxb-7871756934-707612720407-NP0mKmHAPuUV7KVL4XAx8AZP'])

# response = client.chat_postMessage(
#       channel='#bykea-internship',
#      text="Hello world!")
# assert response["ok"]
# assert response["message"]["text"] == "Hello world!"

# slack = Slacker('xoxb-7871756934-707612720407-jejuMOFJbqlSpwyMYvmIl5aJ')


# city = input("Enter your city: ")
city = "Islamabad"
url = "http://api.openweathermap.org/data/2.5/weather?q={},pk&APPID=d58366f88671fbbb22b4cc69734c45ba".format(
    city
)

res = requests.get(url)

data = res.json()
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]


# message = "'Temperature: ', temp \n"


# print(res)

# print('Temperature: ', temp)
# print('Wind Speed: {}'.format(wind_speed))
# print('Humidity: {}'.format(humidity))
# print('Description: {}'.format(description))

slack_city = {"text": city}
slack_temp = {"text": "Temperature : {}".format(temp)}
slack_windspeed = {"text": "Wind Speed: {}".format(wind_speed)}
slack_humidity = {"text": "Humidity : {}".format(humidity)}
slack_description = {"text": "Description : {}".format(description)}


requests.post(web_hook_url, data=json.dumps(slack_city))
requests.post(web_hook_url, data=json.dumps(slack_temp))
requests.post(web_hook_url, data=json.dumps(slack_windspeed))
requests.post(web_hook_url, data=json.dumps(slack_humidity))
requests.post(web_hook_url, data=json.dumps(slack_description))

