import requests
import json

def create_Champion_Id_LookUp():
    file=open('champion.json',"r")
    raw=file.read()
    json_data = json.loads(raw)
    #In Raw Payloads
    CHAMPION_ID_LOOKUP=list()
    for x in json_data['data']:
        CHAMPION_ID_LOOKUP.append((int(json_data['data'][x]['key']),json_data['data'][x]['name']))
    CHAMPION_ID_LOOKUP=sorted(CHAMPION_ID_LOOKUP,key=lambda CHAMPION_ID_LOOKUP:CHAMPION_ID_LOOKUP[0])
    return CHAMPION_ID_LOOKUP
