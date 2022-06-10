# Made by @bentettmar

import json
import requests

BOT_JSON = json.load(open("data/config.json"))["discord"]
API_URL = "https://discordapp.com/api/v9"

def upload_file(file_path):
    url = f"{API_URL}/channels/{BOT_JSON['channelId']}/messages"
    file_name = file_path.split("/")[-1]

    payload={'payload_json': json.dumps({
                "content": "",
                "channel_id": BOT_JSON['channelId'],
                "type": 0,
                "sticker_ids": [],
                "attachments": [
                    {"id": "0", "filename": file_name}
                ]
            })
        }

    files=[('files[0]', (file_name, open(file_path,'rb'),'image/png'))]
    headers = {'Authorization': f'Bot {BOT_JSON["botToken"]}'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_json = response.json()
    attachments = response_json["attachments"]
    
    return attachments[0]["url"]