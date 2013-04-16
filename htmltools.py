#coding=utf-8
#author:u'王健'
#Date: 13-4-16
#Time: 下午8:28
from google.appengine.api import memcache
from models.model import HtmlPage


__author__ = u'王健'



def get(keyName):
    html=memcache.get(keyName)
    if not html:
        h=HtmlPage.get_by_key_name(keyName)
        if h:
            memcache.set(keyName,h.html,3600*24)
        else:
            return None
    else:
        return html



def set(keyName,html,timeNum):
    h=HtmlPage.get_by_key_name(keyName)
    if h:
        h.html=html
        h.put()
    else:
        h=HtmlPage(key_name=keyName)
        h.html=html
        h.put()
    memcache.set(keyName,h.html,timeNum)


def delete(keyName):
    h=HtmlPage.get_by_key_name(keyName)
    if h:
        h.delete()



  