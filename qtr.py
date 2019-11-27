import time
import re
import slack
import datetime
import json

message = ""
settings = ""
with open('settings.json') as json_file:
    settings = json.load(json_file)

web_client = slack.WebClient(settings['token'])

today = datetime.date.today()
print("Today's date:", today)
format_str = '%d-%m-%Y'

with open('codes.json') as json_file:
    data = json.load(json_file)
    for entry in data['quest']:
        dateStart  = datetime.datetime.strptime(entry['start'], format_str).date()
        dateEnd  = datetime.datetime.strptime(entry['end'], format_str).date()
        if ((today >= dateStart) and (today <= dateEnd)):
            message = "Le code quest d'aujoud'hui : " + entry['code'] + "\r\n pour le module : " + entry['module'] + "\r\n" + settings['urlQuest']
            response = web_client.chat_postMessage(channel=settings['channel'], text=message)
            if (response['ok'] == True):
                print("ok")
            else:
                print("prblm avec l'envoi")
            print(message)

