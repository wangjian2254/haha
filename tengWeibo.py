#coding=utf-8
#author:u'王健'
#Date: 11-12-25
#Time: 下午6:39
import logging
from qqweibo import OAuthHandler,API
import webSetting

__author__ = u'王健'


def getApi(token,secret):
    auth = OAuthHandler(webSetting.qqconsumer_key, webSetting.qqconsumer_secret)
    auth.setToken(token, secret)
    api = API(auth)
    return api

def getFriendsteng(wyToken,wySecret):
    l=[]
    try:
        t=getApi(wyToken,wySecret)
        cursor=0
        while True:
            try:
                result=t._friends_idollist(reqnum=30,startindex=cursor)
    #                        result=self.api._statuses_public_timeline()
            except Exception,e:
                logging.info(str(e))
                raise e
            else:
                l+=result
                if len(result)==30:
                    cursor+=30
                else:
                    break
    except Exception,e:
        logging.info('teng'+str(e))
    return l


def getTimelineteng(token,secret,last=None):
    try:
        t=getApi(token,secret)
        if last:
            result=t._statuses_home_timeline(pagetime=int(last.split('*')[0]),lastid=last.split('*')[1],pageflag=2,reqnum=30)#如果获取过则获取最新的
        else:
            result=t._statuses_home_timeline(reqnum=30)#如果没获取过则获取最近的
#        if last and 70==len(result):
#            pass
#        else:
#            usernameSet=getQQWeibo()
#            usernameSet.remove(useracc.username)
            #memcache.Client().set("qqWeibo",usernameSet,360000)
        if result:
            m={}
            if result:
               m['lastid']=str(result[0].timestamp) +'*'+result[0].id
               m['weibo']=result
            return m
#        if result:
#            useracc.qqFriendsLastId=str(result[0].timestamp) +'*'+result[0].id
#            useracc.put()
#            for weibo in result[::-1]:
#                saveFriendsWeibo(weibo.name,weibo,'qq',friendsdic)
#            for k in friendsdic.keys():
#                friendslist.append(friendsdic[k])
#            db.put(friendslist)
    except Exception,e:
        logging.info('teng'+str(e))

#    if result:
#       m['lastid']=result[0].id
#       m['weibo']=result
#    return m

def getUserByWeiboteng(token,secret,userid=None,last=None):
    result=[]
    try:
        t=getApi(token,secret)
        if userid and last:
            result=t._statuses_user_timeline(name=userid,pageflag=2,reqnum=100,pagetime=int(last.split('*')[0]),lastid=last.split('*')[-1])
        elif not userid and last:
            result=t._statuses_broadcast_timeline(pageflag=2,reqnum=100,pagetime=int(last.split('*')[0]),lastid=last.split('*')[-1])
        elif not userid and not last:
            result=t._statuses_broadcast_timeline(pageflag=0,reqnum=10,pagetime=0)
    except Exception,e:
        logging.info('teng'+str(e))
    return result


def sendWeiboteng(token,secret,text):
    try:
        t=getApi(token,secret)
        result=t._t_add(content=text[:139].encode('utf-8'),clientip='64.233.172.33')
        return True
    except  Exception,e:
        logging.info('qq send fail')
        logging.error(str(e))
    return


def delWeiboteng(token,secret,ids):
    try:

        if ids[0]=='4':
            t=getApi(token,secret)
            result=t._t_del(id=ids[1:])
    except Exception,e:
        logging.info('teng delete fail')
        logging.error(str(e))
    return

def commitWeiboteng(token,secret,ids,text):
    try:

        if ids[0]=='4':
            t=getApi(token,secret)
            result=t._t_comment(reid=ids[1:],content=text[:139],clientip='64.233.172.33')
    except Exception,e:
        logging.info('teng commit fail')
        logging.error(str(e))
    return

def replyWeiboteng(token,secret,ids,text,content):
    try:

        if ids[0]=='4':
            t=getApi(token,secret)
            result=t._t_re_add(reid=int(ids[1:]),content=text[:139],clientip='64.233.172.33')
        else:
            sendWeiboteng(token,secret,text+content)
    except Exception,e:
        logging.info('qq reply fail')
        logging.error(str(e))
    return


  