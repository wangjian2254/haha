#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from datetime import datetime
import logging
import webSetting
#from weibopy.api import API
#from weibopy.auth import OAuthHandler
import  weibo
__author__ = u'王健'

def getApi(username,secret,t):
    auth = weibo.APIClient(webSetting.xlconsumer_key, webSetting.xlconsumer_secret,webSetting.WEIBOURL+'/login_check?username='+username+'&data='+str(datetime.now())+'&website=sina')
    auth.set_access_token( secret,int(t))
    return auth

def getFriends(token,secret):
    l=[]
    try:
        api=getApi(token,secret)
        result=api.friends(cursor=-1,count=200)
        l=result['users']
        while result['next_cursor']!=0:
            result=api.friends(cursor=result['next_cursor'],count=200)
            l+=result['users']
    except Exception,e:
        logging.info('sina'+str(e))

    return l

def getTimeline(token,secret,last=None):
    m={}
    try:
        api=getApi(token,secret)
        if last:
            result=api.friends_timeline(since_id=last,count=30)#如果获取过则获取最新的
        else:
            result=api.friends_timeline(count=30)

        if result:
           m['lastid']=result[0]['id']
           m['weibo']=result
    except Exception,e:
        logging.info('sina'+str(e))

    return m

def getUserByWeibo(token,secret,userid=None,last=None):
    result=[]
    try:
        api=getApi(token,secret)
        if userid and last:
            result=api.user_timeline(user_id=userid,since_id=last)
        elif not userid and last:
            result=api.user_timeline(since_id=last)
        elif not userid and not last:
            result=api.user_timeline()
            
    except Exception,e:
        logging.info('sina'+str(e))
    return result

def sendWeibosina(username,secret,t,text):
    try:
        api=getApi(username,secret,t)
        result=api.statuses.update.post(status=text[:139].encode('utf-8'))
        return True
    except  Exception,e:
        logging.info('sina send fail')
        logging.error(str(e))
    return

def delWeibosina(token,secret,ids):
    try:

        if ids[0]=='1':
            api=getApi(token,secret)
            result=api.destroy_status(id=int(ids[1:]))
    except Exception,e:
        logging.info('sina delete fail')
        logging.error(str(e))
    return
def commitWeibosina(token,secret,ids,text):
    try:

        if ids[0]=='1':
            api=getApi(token,secret)
            result=api.comment(id=int(ids[1:]),comment=text[:139])
    except Exception,e:
        logging.info('sina commit fail')
        logging.error(str(e))
    return

def replyWeibosina(token,secret,ids,text,content):
    try:

        if ids[0]=='1':
            api=getApi(token,secret)
            result=api.repost(id=int(ids[1:]),status=text[:139].encode('utf-8'))
        else:
            sendWeibosina(token,secret,text+content)
    except Exception,e:
        logging.info('sina reply fail')
        logging.error(str(e))
    return




