import requests, time, slack, os
from requests.exceptions import HTTPError

def sendmsg():
    slack_token= os.environ["SLACK_API_TOKEN"]
    client = slack.WebClient(token=slack_token)
    client.chat_postMessage(
        channel='#fb-uptime',
        username='ALERT',
        icon_emoji='alert',
        text= ":alert: " + url.rstrip() + " is down. Error code: " + str(response.status_code) + " :alert:"
        )

with open('/Users/vpham/Documents/scripts/urls.txt', 'r') as file:
        for url in file:
            try:
                response = requests.get(url,verify=False)
                if response.status_code != 200:
                    sendmsg()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                print('Success! '+ str(response.status_code) + " " + url )

exit()