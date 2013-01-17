#coding=utf-8
#author:u'王健'
#Date: 11-12-25
#Time: 下午5:31
import logging

from t4py.http.oauth import OAuthToken
from t4py.tblog.tblog import TBlog
import webSetting
from t4py.example import json

__author__ = u'王健'


def getApi(token,secret):
    t = TBlog(webSetting.wyconsumer_key,  webSetting.wyconsumer_secret)
    t._request_handler.access_token = OAuthToken(token,secret)
    return t

def getFriendswy(wyToken,wySecret):
    l=[]
    try:
        t=getApi(wyToken,wySecret)

        cursor=0
        while True:
            try:
                friends = t.statuses_friends({'cursor':cursor})
                result = json.read(friends)
                if result.has_key('error_code'):
                    raise


            except Exception,e:
                logging.info(str(e))
                logging.info(useracc.username+':'+str(cursor))
                if '401' in result['error_code']:
                    raise
               #get friends
            else:
                l+=result['users']
                if len(result['users'])==30:
                    cursor+=30
                else:
                    break
    except Exception,e:
        logging.info('wy'+str(result))
    return l


def getTimelinewy(token,secret,last=None):
    result=[]
    try:
        t=getApi(token,secret)
        if last:
            result=json.read(t.statuses_home_timeline({'max_id':last,'count':30}))#如果获取过则获取最新的
            result=result[:-1]
        else:
            result=json.read(t.statuses_home_timeline({'count':30}))#如果没获取过则获取最近的
#        if last and 199==len(result):
#            pass
#        else:
#            usernameSet=getWYWeibo()
#            usernameSet.remove(useracc.username)
#            memcache.Client().set("wyWeibo",usernameSet,360000)
        if result:
            m={}
            if result:
               m['lastid']=result[0]['cursor_id']
               m['weibo']=result
            return m

    except Exception,e:
        logging.info('wy'+str(result))
#        logging.exception()
#    m={}
#    if result:
#       m['lastid']=result[0].id
#       m['weibo']=result
#    return m

def getUserByWeibowy(token,secret,userid,last=None):
    result=[]
    try:
        t=getApi(token,secret)
        if userid and last:
            result=json.read(t.statuses_user_timeline({'user_id':userid,'max_id':last}))
        elif not userid and last:
            result=json.read(t.statuses_user_timeline({'max_id':last}))
        elif not userid and not last:
            result=json.read(t.statuses_user_timeline({}))
        if type(result)==list:
            result=result[0:-1]
        else:
            result=[]

    except Exception,e:
        logging.info('wy'+str(result))
    return result


def sendWeibowy(token,secret,text):
    try:
        t=getApi(token,secret)
        result=json.read(t.statuses_update({'status':text[:139].encode('utf-8')}))
        return True
    except  Exception,e:
        logging.info('wy send fail')
        logging.error(str(e))
    return


def commitWeibowy(token,secret,ids,text):
    try:

        if ids[0]=='3':
            t=getApi(token,secret)
            result=json.read(t.statuses_reply({'id':int(ids[1:]),'status':text[:139].encode('utf-8')}))
    except Exception,e:
        logging.info('wy commit fail')
        logging.error(str(e))
    return

def delWeibowy(token,secret,ids):
    try:

        if ids[0]=='3':
            t=getApi(token,secret)
            result=json.read(t.statuses_destroy({'id':ids[1:]}))
    except Exception,e:
        logging.info('wy delete fail')
        logging.error(str(e))
    return

def replyWeibowy(token,secret,ids,text,content):
    try:

        if ids[0]=='3':
            t=getApi(token,secret)
            result=t.statuses_retweet({'id':int(ids[1:]),'status':text[:139].encode('utf-8')})
        else:
            sendWeibowy(token,secret,text+content)
    except Exception,e:
        logging.info('wy reply fail')
        logging.error(str(e))
    return




  