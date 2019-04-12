from flask import Flask , request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap

##API KEY##
API_KEY='RGAPI-0734cd2f-b903-4fba-98cc-1532a8774c27'
###

##API LOOKUP#
import requests
from helperFuncs import getSummonerByName, getMatchHistory

###


#Utilities #
from helperFuncs import chooseHomePageBanner , getSrcPlayerIconPngByNum ,parseHistoryIntoMatchInfo,getChampionSquareByNumber
import os
#######
#FORMS in forms.py#
from forms import searchBarForm
####################

#Config#
from config import config
app=Flask(__name__)
app.config.from_object(config)

#####







bootstrap=Bootstrap(app)

## Views ###

@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def index():
    form = searchBarForm()
    user_agent = request.headers.get('User-Agent')
    if form.validate_on_submit():
        return redirect('/summoner/{}'.format(form.search.data))
    return render_template('/homepage/home.html',form=form,banner=chooseHomePageBanner())

@app.route('/summoner/<summonerName>')
def summoner(summonerName):
    responseCode,summoner=getSummonerByName(summonerName)

    #Summoner Not Found
    if (responseCode==404):
        return render_template('/404/summonerNotFound.html',banner=chooseHomePageBanner())
    #Summoner Found
    else:

        matches=(getMatchHistory(summoner['accountId']))['matches']

        pictureSquares= [getChampionSquareByNumber(match['champion']) for match in matches]
        pictureSquares=pictureSquares[0:10]


        return render_template('/summonerTemplates/baseSummonerTemplate.html',summonerName=summonerName,summoner=summoner,profileImg=getSrcPlayerIconPngByNum(summoner['profileIconId']),matches=pictureSquares)
    return '<h1>Hello, {}!</h1>'.format(summonerName)
########
