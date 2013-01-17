#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
import time
import logging
import json
import re
import urllib
import urllib2
import datetime
from google.appengine.api import urlfetch
from models.model import Joke,User
import setting
import sinaWeibo
import tengWeibo
from tools.page import Page
from google.appengine.api import memcache
from xml.dom.minidom import Document
import HTMLParser
from webSetting import  sinawebtext, wywebtext, tengwebtext
import wyWeibo

html_parser = HTMLParser.HTMLParser()


__author__ = u'王健'
headmap={'Referer':'http://www.haha.mx/good/day/1','Cookie':'MAXAUTH=NO','Host':'www.haha.mx',"User-Agent": "	Mozilla/5.0 (Windows NT 5.1; rv:9.0.1) Gecko/20100101 Firefox/9.0.1"}
class getHaHa(Page):
    def get(self):
        uri='http://www.haha.mx/good/day/'
#        uri='http://sso.maxthon.cn/get.php?host=www.haha.mx%2FCommon%2Fsso%2Fmaxthon_passport_sso.php&url=%2Fgood%2Fday%2F'
        self.jokeset=set()
#        self.jokelist=[]
#        p=urllib2.urlopen(uri)
#        print p
        start=self.request.get('start')
        if start:
            uri='http://www.haha.mx/good/year/'
            self.searchRSS(uri,int(start))
        else:
            self.searchRSS(uri)
        
    def searchRSS(self,url,start=0):
        self.rpcs=[]
        for i in range(1+start,11+start):
            rpc=urlfetch.create_rpc(deadline=60)
            rpc.callback=self.rpc_callback(rpc,url+str(i)) 
            urlfetch.make_fetch_call(rpc, url+str(i),method='GET',  headers=headmap,follow_redirects=True)
            self.rpcs.append(rpc)
        for rpc in self.rpcs:
            rpc.wait()

#        Search.saveBook(self.bookMaps)
    def rpc_callback(self,rpc,url):
        return lambda:self.handle_result(rpc,url)
    def handle_result(self,rpc,url):
        try:
            result=rpc.get_result()
#            print result.status_code
            if result.status_code ==200:
                html=result.content.decode('utf-8').replace('\r','').replace('\n','')
#                html=result.content.decode('utf-8')
                skin(self,html)
#            else:
#                rpc=urlfetch.create_rpc(deadline=60)
#                rpc.callback=self.rpc_callback(rpc,result['data']['location'])
#                urlfetch.make_fetch_call(rpc, url,method='GET',  headers=headmap,follow_redirects=False)
#                self.rpcs.append(rpc)
#                pass
#                self.render('templates/result.html',{'hahalist':l,'hahamap':m})
                
        except Exception,e:
            logging.error('0000'+str(e)+url)

def skin(self,html):
#    haha=[]
    '''
    <div class='list-text' id='listText-242377'>

    <a href='###' class='list-pic' mark='242377' id='list-pic-242377' path='2012/01/18/' pic_name='242377_cc5fb6ff525c05fb833d0d973f344da5_1326872875.jpg'>
            <img src='http://image.haha.mx/2012/01/18/small/242377_cc5fb6ff525c05fb833d0d973f344da5_1326872875.jpg' onerror='this.onerror=null;this.src="http://static.haha.mx/images/img-error.jpg"'/>
        </a>
    '''
    haha=re.findall('(?i)<div class=\'list-text\' id=\'listText-(\d+)\'[^>]*>(.*?)</div>',html)
    hahaimg=re.findall('(?i)<a [^>]*mark=\'(\d+)\'[^>]*>[^<]*?<img src=\'(.*?)\'[^>]*>[^<]*</a>',html)
    imgmap={}
    num=0
    for i,src in hahaimg:
        imgmap[i]=src.replace('/small/','/big/')
    for idn,txt in haha:
        if idn not in self.jokeset:
            self.jokeset.add(idn)
            joke= Joke.get_by_key_name('j'+idn)
            if not joke:
                joke=Joke(key_name='j'+idn)
                num+1
            joke.joke= re.sub('(?i)<a [^>]*>[^<]*</a>','',re.sub('(?i)<[/]{0,1}[\w]{1,5} [^>]*>','',html_parser.unescape(txt)))
            if imgmap.has_key(idn):
                joke.img=imgmap[idn]
                joke.type=2
            else:
                joke.type=3
            joke.put()

    logging.info(str(i))
#                self.jokelist.append({'id':idn,'txt':txt,'img':imgmap[idn]})
#            else:
#                self.jokelist.append({'id':idn,'txt':txt})
    return haha,imgmap
class listHaHa(Page):
    def get(self,limit=20,pagenum=1,nowpage=1,jokeid='j'):
        if int(limit)!=20:
            return
        html=memcache.Client().get(str(limit)+'page'+str(pagenum))
        if html:
            return self.flashhtml(html)
        limit=int(limit)
        pagenum=int(pagenum)
        nowpage=int(nowpage)
        nowjoke=Joke.get_by_key_name(jokeid)
        if not nowjoke:
            pagenum=1
            nowpage=1
        if pagenum==1 and( not self.request.referer or self.request.referer[0:len(self.request.host_url)]!=self.request.host_url):
            refer=True
        else:
            refer=False
        tmppagenum=0
        if pagenum==1:
            Cookies = {}  # tempBook Cookies
            Cookies['request_cookie_list'] = [{'key': cookie_key, 'value': cookie_value} for cookie_key, cookie_value in self.request.cookies.iteritems()]
            for c in Cookies['request_cookie_list']:
                if c['key']=='pagenum':
                    if c.has_key('value') and c['value']:
                        tmppagenum=int(c['value'])
            if not tmppagenum :
                refer=False
        tmp=self.request.get('tmp')
        if tmp and tmppagenum>0:
            pagenum=tmppagenum
        hahalist=memcache.Client().get(str(limit)+'p'+str(pagenum))
        if not hahalist:
            hahalist=Joke.all()
            if pagenum>=nowpage:
                if nowjoke:
                    hahalist=hahalist.filter('updateTime <',nowjoke.updateTime)
                hahalist=hahalist.order('-updateTime').fetch(limit,limit*(pagenum-nowpage))
            else:
                if nowjoke:
                    hahalist=hahalist.filter('updateTime >',nowjoke.updateTime)
                hahalist=hahalist.order('updateTime').fetch(limit,limit*(nowpage-pagenum))
                hahalist.reverse()
            memcache.Client().set(str(limit)+'p'+str(pagenum),hahalist,7200)

        if hahalist:
            nowpagestr=hahalist[-1].key().name()
            nowpagestrp=hahalist[0].key().name()
        else:
            nowpagestr='j'
            nowpagestrp='j'
        nowpage='/%s/%s/%s/%s'%(limit,pagenum,pagenum,nowpagestr)
        pagelist=memcache.Client().get(nowpage)
        if not pagelist:
            pagelist=[]
            for i in range(max(1,pagenum-2),max(1,pagenum-2)+7):
                if pagenum>=i:
                    pagelist.append(('/%s/%s/%s/%s'%(limit,i,pagenum,nowpagestr),i))
                else:
                    pagelist.append(('/%s/%s/%s/%s'%(limit,i,pagenum,nowpagestrp),i))
            memcache.Client().set(nowpage,pagelist,72000)
        if pagenum>1:
            setCookie='pagenum=%s;'%(pagenum,)
            self.response.headers.add_header('Set-Cookie', str(setCookie)+'Max-Age = 36000;path=/;')
        html=self.obj2str('templates/result.html',{'refer':refer,'hahalist':hahalist,'per':'/%s/%s/%s/%s'%(limit,max(1,pagenum-1),pagenum,nowpagestr),'next':'/%s/%s/%s/%s'%(limit,max(1,pagenum+1),pagenum,nowpagestrp),'pagelist':pagelist,'nowpage':nowpage,'pagenum':pagenum})
        memcache.Client().set(str(limit)+'page'+str(pagenum),html,7200)
        self.flashhtml(html)

class newHaHa(Page):
    def get(self,limit=10,pagenum=1):
        limit=int(limit)
        pagenum=int(pagenum)
        if pagenum==1 and( not self.request.referer or self.request.referer[0:len(self.request.host_url)]!=self.request.host_url):
            refer=True
        else:
            refer=False
#            logging.info(str(self.request.referer))
        tmppagenum=0
        if pagenum==1:
            Cookies = {}  # tempBook Cookies
            Cookies['request_cookie_list'] = [{'key': cookie_key, 'value': cookie_value} for cookie_key, cookie_value in self.request.cookies.iteritems()]
            for c in Cookies['request_cookie_list']:
                if c['key']=='pagenum':
                    if c.has_key('value') and c['value']:
                        tmppagenum=int(c['value'])
            if not tmppagenum :
                refer=False
        tmp=self.request.get('tmp')
        if tmp and tmppagenum>0:
            pagenum=tmppagenum
        hahalist=memcache.Client().get(str(limit)+'p'+str(pagenum))
        if not hahalist:
            hahalist=Joke.all().order('-updateTime').fetch(limit,limit*(pagenum-1))
            memcache.Client().set(str(limit)+'p'+str(pagenum),hahalist,7200)
        if hahalist:
            nowpagestr=hahalist[-1].key().name()
            nowpagestrp=hahalist[0].key().name()
        else:
            nowpagestr='j'
            nowpagestrp='j'
        nowpage='/%s/%s/%s/%s'%(limit,pagenum,pagenum,nowpagestr)
        pagelist=memcache.Client().get(nowpage)
        if not pagelist:
            pagelist=[]
            for i in range(max(1,pagenum-2),max(1,pagenum-2)+7):
                if pagenum>=i:
                    pagelist.append(('/%s/%s/%s/%s'%(limit,i,pagenum,nowpagestr),i))
                else:
                    pagelist.append(('/%s/%s/%s/%s'%(limit,i,pagenum,nowpagestrp),i))
            memcache.Client().set(nowpage,pagelist,72000)
        if pagenum>1:
            setCookie='pagenum=%s;'%(pagenum,)
            self.response.headers.add_header('Set-Cookie', str(setCookie)+'Max-Age = 36000;path=/;')
        self.render('templates/result.html',{'refer':refer,'hahalist':hahalist,'per':'/%s/%s/%s/%s'%(limit,max(1,pagenum-1),pagenum,nowpagestr),'next':'/%s/%s/%s/%s'%(limit,max(1,pagenum+1),pagenum,nowpagestrp),'pagelist':pagelist,'nowpage':nowpage,'pagenum':pagenum})


class getJokeByPhone(Page):
    def get(self):
        joke=self.request.get('joke')
        limit=self.request.get('limit')
        if not limit:
            limit=20
        else:
            limit=int(limit)
        type=self.request.get('type')
        if not type:
            type=3
        else:
            type=int(type)
        memkey='d'+str(limit)+joke+str(type)
        jlist=memcache.Client().get(memkey)
        if not jlist:
            jlist=Joke.all()
            if joke:
                joke=Joke.get_by_key_name(joke)
            if joke:
                jlist=jlist.filter('updateTime >',joke.updateTime)
            if type:
                jlist=jlist.filter('type =',type)
            jlist=jlist.order('updateTime').fetch(limit)
            memcache.Client().set(memkey,jlist,7200)
        xml,datas=list2xml(jlist)
        datas.setAttribute('aPhoneVerson',str(setting.aPhoneVerson))
        datas.setAttribute('aPhoneURI',setting.aPhoneURI)
        datas.setAttribute('ADTime',str(setting.ADTime))
        self.response.out.write(xml.toxml('utf-8'))


def list2xml(contents):
    xml=Document()
    datas=xml.createElement('datas')
    xml.appendChild(datas)
    for c in contents:
        data=xml.createElement('data')
        data.setAttribute('jid',c.key().name())
        data.setAttribute('type',str(c.type))
        data.appendChild(xml.createTextNode(html_parser.unescape(c.joke).replace('<br/>','\n')))
        data.setAttribute('updateTime',str(c.updateTime))
        data.setAttribute('image',c.img or '')
        datas.appendChild(data)
    return (xml,datas)


class SendWeibo(Page):
    def get(self):
        username=self.request.get('username')
        userpwd=self.request.get('userpwd')
        jokeid=self.request.get('jokeid')
        website=self.request.get('website')
        joke=Joke.get_by_key_name(jokeid)
        msg=''
        if not joke:
            self.response.out.write(u'该条笑话在服务器上已经删除。')
            return
        user=User.get_by_key_name('u'+username)
        if not user:
            self.response.out.write(u'用户不存在。')
            return
        elif user.pwd!=userpwd:
            self.response.out.write(u'用户密码错误。')
            return
        else:
            joke.joke=html_parser.unescape(joke.joke).replace('<br/>','\n')
            if 'sina' in website:
                text=joke.joke
                isSuccess=False
                while text:
                    if sinaWeibo.sendWeibosina(user.sinaToken,user.sinaSecret,text[:90]+sinawebtext):
                        isSuccess=True
                    text=text[90:]
                if isSuccess:
                    msg+=u'新浪微博发送成功。'
                else:
                    msg+=u'新浪微博发送失败。'
            if 'wy' in website:
                text=joke.joke
                isSuccess=False
                while text:
                    if wyWeibo.sendWeibowy(user.wyToken,user.wySecret,text[:90]+wywebtext):
                        isSuccess=True
                    text=text[90:]
                if isSuccess:
                    msg+=u'网易微博发送成功。'
                else:
                    msg+=u'网易微博发送失败。'
            if 'teng' in website:
                text=joke.joke
                isSuccess=False
                while text:
                    if tengWeibo.sendWeiboteng(user.tengToken,user.tengSecret,text[:90]+tengwebtext):
                        isSuccess=True
                    text=text[90:]
                if isSuccess:
                    msg+=u'腾讯微博发送成功。'
                else:
                    msg+=u'腾讯微博发送失败。'
            if msg:
                self.response.out.write(msg)
            else:
                self.response.out.write(u'未发送微博。')


class Reg(Page):
    def get(self):
        username=self.request.get('username')
        userpwd=self.request.get('userpwd')
#        usernick=self.request.get('usernick')
        text=''
        for s in self.request.query_string.split('&'):
            if 'usernick'==s[0:8] and len(s)>8:
                unquotedPath= urllib.unquote(s[9:])
                try:
                    text = unicode(unquotedPath, 'utf8')
                except:
                    try:
                      text = unicode(unquotedPath, 'gbk')
                    except:
                        text=''
        user=User.get_by_key_name('u'+username)
        if user:
            self.response.out.write(u'用户名已经存在')
            return
        user=User(key_name='u'+username)
        user.pwd=userpwd
        user.nick=text
        user.put()
        self.response.out.write('1')


class Robots(Page):
    def get(self):
        html='''User-agent: *
Disallow: /20/
Allow: /'''
        self.response.out.write(html)



