#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from models.model import Joke, JokeCheck
from tools.page import Page
from google.appengine.ext import db

__author__ = u'王健'

class checkHaHa(Page):
    def get(self):
        checkJoke=JokeCheck.get_by_key_name('check')
        checkJoke=Joke.get_by_key_name(checkJoke.lastCheckJoke)
        if checkJoke:
            hahalist=Joke.all().filter('updateTime >',checkJoke.updateTime).order('updateTime').fetch(40)
        else:
            hahalist=Joke.all().order('updateTime').fetch(40)
        self.render('templates/check.html',{'hahalist':hahalist})
    def post(self):
        jokeids=self.request.get('jokeids')
        checkJoke=JokeCheck.get_by_key_name('check')
        if not checkJoke:
            checkJoke=JokeCheck(key_name='check')
        checkJoke.lastCheckJoke=jokeids
        checkJoke.put()
        delids=self.request.get_all('delid')
#        for name,id in self.request.POST.multi:
#            if name=='jokeids':
#                jokeids.append(id)
#            if name=='delid':
#                delids.append(id)
#        jokeids=self.request.get('jokeids').split(',')
#
#        delids=self.request.get('delid').split(',')

#        ids=[]
#        for id in  jokeids:
#            if id not in delids:
#                ids.append(id)
#        js=[]
#        for j in Joke.get_by_key_name(ids):
#            #j=Joke.get_by_key_name(id)
#            j.isCheck=True
#            js.append(j)
#        db.put(js)

        deljoke=Joke.get_by_key_name(delids)
        if deljoke:
            db.delete(deljoke)
        self.redirect('/check')

