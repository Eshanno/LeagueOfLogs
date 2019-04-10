from flask import Flask , request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
import os
##API KEY##
API_KEY='RGAPI-0734cd2f-b903-4fba-98cc-1532a8774c27'
###

##API LOOKUP#
import requests
from helperFuncs import getSummonerByName

###


#Utilities #
from helperFuncs import chooseHomePageBanner , getSrcPlayerIconPngByNum
#######
#FORMS#
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,FileField
from wtforms.validators import DataRequired
####################

#Config#
from config import config
app=Flask(__name__)
app.config.from_object(config)

#####
class searchBarForm(FlaskForm):
    search = StringField("<h1>Search By Summoner Name<h1>", validators=[DataRequired()])
    submit = SubmitField('Submit')






bootstrap=Bootstrap(app)
@app.route('/',methods=['GET','POST'])
def index():
    form = searchBarForm()
    user_agent = request.headers.get('User-Agent')
    if form.validate_on_submit():
        responseCode,summoner=getSummonerByName(form.search.data)

        #Summoner Not Found
        if (responseCode==404):
            pass
        #Summoner Found
        else:
            session['summoner']=summoner
            return redirect('/summoner/{}'.format(form.search.data))
    return render_template('/homepage/home.html',form=form,banner=chooseHomePageBanner())

@app.route('/summoner/<summonerName>')
def summoner(summonerName):
    summoner=session.get('summoner')
    return render_template('/summonerTemplates/baseSummonerTemplate.html',summonerName=summonerName,summoner=summoner,profileImg=getSrcPlayerIconPngByNum(summoner['profileIconId']))
    #return '<h1>Hello, {}!</h1>'.format(summonerName)
