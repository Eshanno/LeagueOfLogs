import requests
import json
import math
from random import choice
from flask import url_for
from apiToHumanHelper import CHAMPION_ID_LOOKUP,championIDToName
##API KEY##
API_KEY='RGAPI-5ad26a56-25de-44f0-892d-3c28bd1eb909'
VERSION="9.7.1"
########Consants#########
#BANNERS : Found in chooseHomePageBanner method
#VERSION : Found in getSrcPlayerIconPngByNum method
#########################



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

def getSummonerByName(summonerName):
    querry='https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'.format(summonerName,API_KEY)
    r = requests.get(querry)

    print(querry) #DEBUG
    print(r.json())#DEBUG

    return r.status_code,r.json()
def chooseHomePageBanner():

    BANNERS=['homePageBanners/Pilot-Flag_3.png', 'homePageBanners/Pilot-3.png', 'homePageBanners/Zaun-3.png', 'homePageBanners/Shadow_Isles-2.png', 'homePageBanners/Piltover-3.png', 'homePageBanners/Piltover-2.png', 'homePageBanners/1.png', 'homePageBanners/Pilot-1.png', 'homePageBanners/CoPilot-3.png', 'homePageBanners/3.png', 'homePageBanners/Freljord-1.png', 'homePageBanners/Pilot-2.png', 'homePageBanners/Piltover-1.png', 'homePageBanners/Shadow_Isles-3.png', 'homePageBanners/Pilot-Flag_1.png', 'homePageBanners/Freljord-3.png', 'homePageBanners/CoPilot-2.png', 'homePageBanners/Demacia-3.png', 'homePageBanners/2.png', 'homePageBanners/Zaun-1.png', 'homePageBanners/Pilot-Flag_2.png', 'homePageBanners/Freljord-2.png', 'homePageBanners/Base-1.png', 'homePageBanners/Zaun-2.png', 'homePageBanners/Shadow_Isles-1.png', 'homePageBanners/Demacia-2.png', 'homePageBanners/CoPilot-1.png', 'homePageBanners/Demacia-1.png']
    banner=url_for('static',filename=choice(BANNERS))
    return banner

def getSrcPlayerIconPngByNum(imgNumber):
    querry='http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png'.format(VERSION,imgNumber)
    return querry



def getChampionSquareByNumber(championId):
    sanitizedName=championIDToName(championId).replace(' ','').replace('\'','')

    return 'http://ddragon.leagueoflegends.com/cdn/9.7.1/img/champion/{}.png'.format(sanitizedName)


#Helper Function for making querrys to the riot API it handles the appending of optional params in the form variablename=value& ...#
def attachOptionalParams(paramDict):
    paramString=""
    for counter, key in enumerate(paramDict,1):
        paramString = paramString+"{}={}".format(key,paramDict[key])

        paramString = paramString+"&"

    return paramString


# ParamDict
def getMatchHistory(accountId,champion=None,queue=None,season=None,beginIndex=None,endIndex=None):
    #Turns Params Into a data dictionary for simplicity
    local=locals()
    paramDict={variable:local[variable] for variable in local if variable!='accountId' and local[variable]!=None}
    ###
    if paramDict!=dict():
        r='https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?{}api_key={}'.format(accountId,attachOptionalParams(paramDict),API_KEY)
        matches=requests.get(r).json()
        return matches
    else:
        matches=requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?api_key={}'.format(accountId,API_KEY)).json()
        return matches


def parseHistoryIntoMatchInfo(matchHistory):
    pass
