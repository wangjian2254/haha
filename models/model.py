#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from google.appengine.ext import db
__author__ = u'王健'
class Joke(db.Model):
    updateTime=db.DateTimeProperty(auto_now_add=True)
    joke=db.TextProperty()
    img=db.TextProperty()
    type=db.IntegerProperty()
    isCheck=db.BooleanProperty(default=True)
    date=db.StringProperty()
#    replay=db.StringListProperty(indexed=False)
#    good=db.IntegerProperty(default=0)
#    bad=db.IntegerProperty(default=0)
class UserJoke(db.Model):
    username=db.StringProperty()
    pwd=db.StringProperty(indexed=False)
    nickname=db.StringProperty(indexed=False)

class Replay(db.Model):
    joke=db.StringProperty()
    face=db.IntegerProperty(default=1,indexed=False)
    fatherid_id=db.IntegerProperty()
    user=db.IntegerProperty()
    content=db.TextProperty()
    updateTime=db.DateTimeProperty()

class ReplayGood(db.Model):
    point=db.IntegerProperty()
class ReplayBad(db.Model):
    point=db.IntegerProperty()


class DefaultDate(db.Model):
    date=db.StringProperty()

class JokeCheck(db.Model):
    lastCheckJoke=db.StringProperty()

class UserAccessToken(db.Model):
    sinauserid=db.StringProperty()#新浪用户id
    sinaSecret=db.StringProperty()#新浪微博的用户授权
    sinaToken=db.StringProperty()
    sinaisright=db.BooleanProperty(default=False)
    qqSecret=db.StringProperty()#新浪微博的用户授权
    qqToken=db.StringProperty()
    qqisright=db.BooleanProperty(default=False)
    qqupdate=db.DateTimeProperty(auto_now_add=True)#最后一次更新时间
    shAccessToken=db.StringProperty()#新浪微博的用户授权
    wySecret=db.StringProperty()#新浪微博的用户授权
    wyToken=db.StringProperty()
    wyuserid=db.StringProperty()#新浪用户id
    wyisright=db.BooleanProperty(default=False)
    update=db.DateTimeProperty(auto_now_add=True)#最后一次更新时间
    wyupdate=db.DateTimeProperty(auto_now_add=True)#最后一次更新时间

class PutWeibMark(db.Model):
    jokename=db.StringProperty()


class User(db.Model):
    pwd=db.StringProperty(indexed=False)
    nick=db.StringProperty(indexed=False)
    sinaSecret=db.StringProperty(indexed=False)
    sinaToken=db.StringProperty(indexed=False)
    wySecret=db.StringProperty(indexed=False)
    wyToken=db.StringProperty(indexed=False)
    tengSecret=db.StringProperty(indexed=False)
    tengToken=db.StringProperty(indexed=False)


    
  