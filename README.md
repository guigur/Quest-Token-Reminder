# Quest-Token-Reminder

1. Install the requirements (see REQUIREMENTS.txt)
1. Create a slack app
1. Retrieve your token
1. Copy paste the settings.json.sample and rename it settings.json
1. Fill this file with you slack tocken, the url of the quest tracking tool and the choosen channel
1. Fill the codes.json with entries
1. Create a cron entry to execute this program multiples times a day
ex: 45 12  * * * cd /path/to/Quest-Token-Reminder/ && /usr/local/bin/python3 /path/to/Quest-Token-Reminder/qtr.py &> /path/to/Quest-Token-Reminder/log.txt

Voilà
