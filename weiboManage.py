#coding=utf-8
import logging
import datetime
from google.appengine.ext import db
from models.model import UserAccessToken, PutWeibMark, Joke

from t4py.tblog.tblog import TBlog
from tools.page import Page
import webSetting
from weibopy.api import API
from t4py.http.oauth import OAuthToken
from t4py.example import json
import json as sysjson

from google.appengine.ext import webapp

__author__ = 'wangjian2254'

#from weibopy import OAuthHandler, oauth, WeibopError
from google.appengine.api import memcache, urlfetch
from qqweibo.auth import  OAuthHandler as qqOAuthHandler
from qqweibo.api import  API as qqAPI
import weibo
import HTMLParser
html_parser = HTMLParser.HTMLParser()

#class MainPage(Page):
#  def get(self):
#      logging.info(self.request.host)
#      setting=Setting().all().fetch(1)
#      if not setting:
#          setting=Setting()
#          setting.dbphotoWebSite="http://localhost:8000"
#          setting.weiboWebSite="http://localhost:8080"
#          setting.put()
#      userwebo=UserAccessToken().all()
#      url = users.create_logout_url(self.request.uri)
#      template_values = {'url':url,'webouser':userwebo}
#      self.render('templates/index.html',template_values)
#
#class WebOAuthHandler(OAuthHandler):
#    user_id=None
#    def get_authorization_url_with_callback(self, callback, signin_with_twitter=False):
#        """Get the authorization URL to redirect the user"""
#        try:
#            # get the request token
#            self.request_token = self._get_request_token()
#
#            # build auth request and return as url
#            if signin_with_twitter:
#                url = self._get_oauth_url('authenticate')
#            else:
#                url = self._get_oauth_url('authorize')
#            request = oauth.OAuthRequest.from_token_and_callback(
#                token=self.request_token, callback=callback, http_url=url
#            )
#            return request.to_url()
#        except Exception, e:
#            raise WeibopError(e)

#class MainPage(PublicPage):
#  def get(self):
##def _get_referer_url(request):
#    referer_url = request.META.get('HTTP_REFERER', '/')
#    host = request.META['HTTP_HOST']
#    if referer_url.startswith('http') and host not in referer_url:
#        referer_url = '/' # 避免外站直接跳到登录页而发生跳转错误
#    return referer_url
#
#def _oauth():
#    """获取oauth认证类"""
#    return WebOAuthHandler(webSetting.xlconsumer_key, webSetting.xlconsumer_secret)

class PubWeib(Page):
    def get(self):
        textnum=98
        addsubject=u'#趣图##搞笑##笑话#'
        jmark=PutWeibMark.get_by_key_name('mark')
        jlist=Joke.all()
        if jmark:
            joke=Joke.get_by_key_name(jmark.jokename)
        else:
            joke=None
            jmark=PutWeibMark(key_name='mark')
        if joke:
            jlist.filter('updateTime >',joke.updateTime)
        jlist.filter('type =',2).order('updateTime').fetch(1)
        jlist.order('updateTime').fetch(1)
        try:
            j=jlist[0]
            jmark.jokename=j.key().name()
            jmark.put()
            j.joke=html_parser.unescape(j.joke.replace(u'绿',u'转'))
            j.put()
            j.joke=j.joke.replace('<br/>','')
            total=len(j.joke)/textnum
            if len(j.joke)%textnum>0: 
                total=int(total)+1
            m=1
            mark=''
            if j.img:
                image = urlfetch.fetch(
                    url =j.img,
                    payload = {},
                    method = urlfetch.GET,
                    headers = {'Content-Type':'application/x-www-form-urlencoded',
                               'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'},
                    follow_redirects = True,deadline=10)
                if image.status_code==200:
                    bf=db.Blob(image.content)
                    if total>=m and total>1:
                        mark='(%s/%s)'%(m,total)
                        m+=1
                    sendWeibo(self,addsubject+j.joke[:textnum]+mark+'http://joke.123fangsong.com/%s.html'%jmark.jokename,bf)
                    j.joke=j.joke[textnum:]
            while j.joke:
                if total>=m and total>1:
                    mark='(%s/%s)'%(m,total)
                    m+=1
                sendWeibo(self,'http://joke.123fangsong.com/%s.html'%jmark.jokename+' '+j.joke[:textnum]+mark+addsubject)
                j.joke=j.joke[textnum:]
        except Exception,e:
            logging.info('empty'+str(e))






class Login(Page):
  def get(self):
    # 保存最初的登录url，以便认证成功后跳转回来
#    back_to_url = _get_referer_url(request)
#    request.session['login_back_to_url'] = back_to_url
    website=self.request.get('website')
#    userAccessToken=UserAccessToken()
#    userAccessToken.sinaExpires='1522066881'
#    userAccessToken.sinaSecret='2.00HGNhqCdb1iQBb8eed27af80MRd2r'
#    userAccessToken.put()
#    logging.info(str(UserAccessToken().all().count()))

    # 获取oauth认证url
#    setting=Setting().all().fetch(1)
#    if setting:
#        setting=setting[0]
#    else:
#        return
    if 'sina'==website:
        login_backurl =webSetting.WEIBOURL+'/Admin/login_check?website=sina'
        auth_client = weibo.APIClient(webSetting.xlconsumer_key, webSetting.xlconsumer_secret, login_backurl)

        auth_url = auth_client.get_authorize_url()
        # 保存request_token，用户登录后需要使用它来获取access_token
#        user_request_token=memcache.Client().get(website+"_request_token1")
#        if not user_request_token:
#            user_request_token= auth_client.request_token
#            memcache.Client().set(website+"_request_token1",user_request_token,36000)
        # 跳转到登录页面
        return self.redirect(auth_url)
    elif 'wy'==website:
        login_backurl =self.request.host_url+'/Admin/login_check?website=wy'
        t = TBlog(webSetting.wyconsumer_key, webSetting.wyconsumer_secret)
        t.get_request_token()
        url=t.get_auth_url(login_backurl)
        # 保存request_token，用户登录后需要使用它来获取access_token
        user_request_token=memcache.Client().get(website+"_request_token3")
        if not user_request_token:
            user_request_token= t
            memcache.Client().set(website+"_request_token3",user_request_token,36000)
        return self.redirect(url)
    elif 'teng'==website:
        login_backurl=self.request.host_url+'/Admin/login_check?website=teng'
        auth=qqOAuthHandler(webSetting.qqconsumer_key,webSetting.qqconsumer_secret,callback=login_backurl)
        url=auth.get_authorization_url()
        # 保存request_token，用户登录后需要使用它来获取access_token
        memcache.Client().set(website+"_request_token4",auth,36000)
        return self.redirect(url)

class Login_check(Page):
  def get(self):
    website=self.request.get('website')
    userAccessToken=UserAccessToken().all().fetch(1)
    if userAccessToken:
        userAccessToken=userAccessToken[0]
    else:
        userAccessToken=UserAccessToken()
    if 'sina'==website:
        """用户成功登录授权后，会回调此方法，获取access_token，完成授权"""
        # http://mk2.com/?oauth_token=c30fa6d693ae9c23dd0982dae6a1c5f9&oauth_verifier=603896
#        verifier = self.request.get('oauth_verifier', None)
#        auth_client = _oauth()
#        # 设置之前保存在session的request_token
#    #    request_token = request.session['oauth_request_token']
#        request_token=memcache.Client().get(website+"_request_token1")
#        if not request_token:
#            return
#        memcache.Client().delete(website+"_request_token1")
#    #    del request.session['oauth_request_token']
#
#        auth_client.set_request_token(request_token.key, request_token.secret)
#        access_token = auth_client.get_access_token(verifier)
        code=self.request.get('code')
        logging.info('code:'+code)
        client = weibo.APIClient(webSetting.xlconsumer_key, webSetting.xlconsumer_secret,webSetting.WEIBOURL+'/Admin/login_check?website=sina')
        r = client.request_access_token(code)

        access_token, expires_in, uid = r.access_token, r.expires_in, r.uid
        client.set_access_token(access_token, expires_in)
        logging.info('access token: %s' % sysjson.dumps(access_token))
        u = client.users.show.get(uid=uid)
        # 保存access_token，以后访问只需使用access_token即可
        userAccessToken.sinaSecret=access_token
#        userAccessToken.sinaToken=access_token.key
        userAccessToken.sinaExpires=str(expires_in)
        userAccessToken.sinauserid=uid
        userAccessToken.sinaisright=True
        userAccessToken.put()
    elif 'wy'==website:
#        t = TBlog(weboSetting.wyconsumer_key, weboSetting.wyconsumer_secret)
        request_token=memcache.Client().get(website+"_request_token3")
        if not request_token:
            return
        memcache.Client().delete(website+"_request_token3")
#        t._request_handler.request_token=request_token
#        request_token.get_auth_url()
#        pin=self.request.get('pin', None)
        pin=self.request.get('oauth_token', None)
        s=request_token.get_access_token(pin)
        userAccessToken.wySecret=s.secret
        userAccessToken.wyToken=s.key
        userAccessToken.wyisright=True
        userAccessToken.put()
    elif 'teng'==website:
        request_token=memcache.Client().get(website+"_request_token4")
        if not request_token:
            return
        memcache.Client().delete(website+"_request_token4")
        verifier = self.request.get('oauth_verifier', None)
        access_token = request_token.get_access_token(verifier)
        userAccessToken.qqSecret=access_token.secret
        userAccessToken.qqToken=access_token.key
        #userAccessToken.qquserid=auth_client.user_id
        userAccessToken.qqisright=True
        userAccessToken.put()

    return self.redirect('/Admin')

def sendWeibo(self,text,imgno=None):
#    logging.info(text)
    if not sendSinaWeibo(self,text,imgno):
        sendSinaWeibo(self,text)
    if not sendWangYiWeibo(self,text,imgno):
        sendWangYiWeibo(self,text)
    if not sendQQWeibo(self,text,imgno):
        sendQQWeibo(self,text)
def sendSinaWeibo(self,text,imgno=None):
    userAccessToken=UserAccessToken.all().fetch(1)
    if userAccessToken and userAccessToken[0].sinaisright:
        useracc=userAccessToken[0]
    else:
        return True
    self.auth=weibo.APIClient(webSetting.xlconsumer_key, webSetting.xlconsumer_secret,webSetting.WEIBOURL+'/Admin/login_check?website=sina')
    self.auth.set_access_token(useracc.sinaSecret, int(useracc.sinaExpires))




    try:
        if imgno:
#                image = urlfetch.fetch(
#                    url =imgno,
#                    payload = {},
#                    method = urlfetch.GET,
#                    headers = {'Content-Type':'application/x-www-form-urlencoded',
#                               'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'},
#                    follow_redirects = True,deadline=10)
#                if image.status_code==200:
#                    bf=db.Blob(image.content)
                    result=self.auth.statuses.upload.post(pic=imgno,status=text.encode('utf-8'))
#                else:
#                    result=self.api.update_status(status=text[:139].encode('utf-8'))
        else:
            result=self.auth.statuses.update.post(status=text.encode('utf-8'))
    except Exception,e:
        logging.info('sina'+str(e))
        return False
#        if str(e).find('40025')==-1:
#            self.error(500)
#            return False
    else:
        return True

def sendWangYiWeibo(self,text,imgno=None):
    userAccessToken=UserAccessToken.all().fetch(1)
    if userAccessToken and userAccessToken[0].wyisright:
        useracc=userAccessToken[0]
    else:
        return True
    t = TBlog(webSetting.wyconsumer_key,  webSetting.wyconsumer_secret)
    t._request_handler.access_token = OAuthToken(useracc.wyToken,useracc.wySecret)
    try:
        imgdata=''
#        if imgno:
#                image = urlfetch.fetch(url=setting[0].dbphotoWebSite+'/s/'+imgno,deadline=10)
#
#                if image.status_code == 200:
#                    logging.info(setting[0].dbphotoWebSite+'/s/'+imgno)
#                    bf=db.Blob(image.content)
        if imgno:
            imgulr=json.read(t.statuses_upload(imgno))
            upload_image_url=imgulr['upload_image_url']
            text=upload_image_url+' '+text

        result=t.statuses_update({'status':text.encode('utf-8')})
    except Exception,e:
        logging.info('wy:'+str(e))
#        logging.info('wy'+str(result))
#        if str(result).find('40025')==-1:
        self.error(500)
        return False
    else:
        return True
def sendQQWeibo(self,text,imgno=None):
    userAccessToken=UserAccessToken().all().fetch(1) 
    if userAccessToken and userAccessToken[0].qqisright:
        useracc=userAccessToken[0]
    else:
        return True
    self.auth = qqOAuthHandler(webSetting.qqconsumer_key, webSetting.qqconsumer_secret)
    self.auth.setToken(useracc.qqToken, useracc.qqSecret)
    self.api = qqAPI(self.auth)



    try:
        if imgno:
#                image = urlfetch.fetch(
#                    url =setting[0].dbphotoWebSite+'/s/'+imgno,
#                    payload = {},
#                    method = urlfetch.GET,
#                    headers = {'Content-Type':'application/x-www-form-urlencoded',
#                               'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'},
#                    follow_redirects = True,deadline=10)
#                if image.status_code==200:
#                    bf=db.Blob(image.content)
            result=self.api._t_add_pic(filename=imgno,content=text.encode('utf-8'),clientip='64.233.172.33')
#                else:
#                    result=self.api.update_status(status=text[:139].encode('utf-8'))
        else:
            result=self.api._t_add(content=text.encode('utf-8'),clientip='64.233.172.33')
    except Exception,e:
        logging.info('qq'+str(e))
        if str(e).find('40025')==-1:
            self.error(500)
            return False
    else:
        return True