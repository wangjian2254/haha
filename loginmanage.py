#coding=utf-8
#author:u'王健'
#Date: 13-3-5
#Time: 下午10:15
import uuid
from google.appengine.api import memcache
from models.model import User, UserJoke

__author__ = u'王健'





def setLogin(web,username):
    uid=str(uuid.uuid4())
    memcache.set('webusername'+uid,username,36000)
    setCookie='webusername='+uid+';'
    web.response.headers.add_header('Set-Cookie', setCookie+'Max-Age = 3600000;path=/;')

def setLogout(web):
    setCookie='webusername=;'
    web.response.headers.add_header('Set-Cookie', setCookie+'Max-Age = 3600000;path=/;')

def getUser(user):
    user_joke=memcache.get('userbyid'+str(user))
    if not user_joke:
        user_joke=UserJoke.get_by_id(int(user))
        memcache.set('userbyid'+str(user),user_joke,720000)
    return user_joke

def get_current_user(web):
    guist={}
    Cookies = {}  # tempBook Cookies
    Cookies['request_cookie_list'] = [{'key': cookie_key, 'value': cookie_value} for cookie_key, cookie_value in web.request.cookies.iteritems()]
    for c in Cookies['request_cookie_list']:
        if c['key']=='webusername':
            guist["userid"]=memcache.get('webusername'+c['value'])
    if guist and guist.has_key('userid') and guist['userid']:
        user=memcache.get('userlogin'+str(guist['userid']))
        if not user:
            user=getUser(guist['userid'])
            memcache.set('userlogin'+str(guist['userid']),user,36000)
        if user:
            return user
    return False


  