#coding=utf-8
from datetime import datetime
import urllib
import logging
from t4py.tblog.tblog import TBlog
from tools.page import Page
import webSetting
from models.model import User
__author__ = 'Administrator'

from google.appengine.api import urlfetch
from weibopy import OAuthHandler, oauth, WeibopError
from google.appengine.api import memcache
from google.appengine.api import users
from qqweibo import  OAuthHandler as qqOAuthHandler
from qqweibo import  API,JSONParser


class WebOAuthHandler(OAuthHandler):
    user_id=None
    def get_authorization_url_with_callback(self, callback, signin_with_twitter=False):
        """Get the authorization URL to redirect the user"""
        try:
            # get the request token
            self.request_token = self._get_request_token()

            # build auth request and return as url
            if signin_with_twitter:
                url = self._get_oauth_url('authenticate')
            else:
                url = self._get_oauth_url('authorize')
            request = oauth.OAuthRequest.from_token_and_callback(
                token=self.request_token, callback=callback, http_url=url
            )
            return request.to_url()
        except Exception, e:
            raise WeibopError(e)

#class MainPage(PublicPage):
#  def get(self):
##def _get_referer_url(request):
#    referer_url = request.META.get('HTTP_REFERER', '/')
#    host = request.META['HTTP_HOST']
#    if referer_url.startswith('http') and host not in referer_url:
#        referer_url = '/' # 避免外站直接跳到登录页而发生跳转错误
#    return referer_url

def _oauth():
    """获取oauth认证类"""
    return WebOAuthHandler(webSetting.xlconsumer_key, webSetting.xlconsumer_secret)

class Login(Page):
  def get(self):
    username=self.request.get('username')
    website=self.request.get('website')
    if not username:
        return
    # 获取oauth认证url


    if 'sina'==website:
        login_backurl =webSetting.WEIBOURL+'/login_check?username='+username+'&data='+str(datetime.now())+'&website=sina'
        auth_client = _oauth()
        auth_url = auth_client.get_authorization_url_with_callback(login_backurl)
        # 保存request_token，用户登录后需要使用它来获取access_token
        memcache.Client().set(username+"_request_token1",auth_client.request_token,36000)
        # 跳转到登录页面
        return self.redirect(auth_url)
    elif 'wy'==website:
        login_backurl =webSetting.WEIBOURL+'/login_check?username='+username+'&data='+str(datetime.now())+'&website=wy'
        t = TBlog(webSetting.wyconsumer_key, webSetting.wyconsumer_secret)
        t.get_request_token()
        url=t.get_auth_url(login_backurl)
        # 保存request_token，用户登录后需要使用它来获取access_token

        memcache.Client().set(username+"_request_token3",t,36000)
        return self.redirect(url)
    elif 'teng'==website:
        login_backurl=webSetting.WEIBOURL+'/login_check?username='+username+'&data='+str(datetime.now())+'&website=teng'
        auth=qqOAuthHandler(webSetting.qqconsumer_key,webSetting.qqconsumer_secret,callback=login_backurl)
        url=auth.get_authorization_url()
        # 保存request_token，用户登录后需要使用它来获取access_token
        memcache.Client().set(username+"_request_token4",auth,36000)
        return self.redirect(url)

class Login_check(Page):
  def get(self):
    website=self.request.get('website')
    username=self.request.get('username')
    user=User.get_by_key_name('u'+username)
    msg=u'您开通了'
#    userAccessToken=UserAccessToken().all().filter('username =',username).fetch(1)
#    if userAccessToken:
#        userAccessToken=userAccessToken[0]
#    else:
#        userAccessToken=UserAccessToken()
#        userAccessToken.username=username
    if 'sina'==website:
        """用户成功登录授权后，会回调此方法，获取access_token，完成授权"""
        # http://mk2.com/?oauth_token=c30fa6d693ae9c23dd0982dae6a1c5f9&oauth_verifier=603896
        verifier = self.request.get('oauth_verifier', None)
        if not username:
            return
        auth_client = _oauth()
        # 设置之前保存在session的request_token
    #    request_token = request.session['oauth_request_token']
        request_token=memcache.Client().get(username+"_request_token1")
        if not request_token:
            return
        memcache.Client().delete(username+"_request_token1")
    #    del request.session['oauth_request_token']

        auth_client.set_request_token(request_token.key, request_token.secret)
        access_token = auth_client.get_access_token(verifier)
        # 保存access_token，以后访问只需使用access_token即可
        user.sinaToken=access_token.key
        user.sinaSecret=access_token.secret
        user.put()
#        pam={'key0':'sinaSecret','value0':access_token.secret,'key1':'sinaToken','value1':access_token.key}
#        syncMogu(username,pam)
#        syncWeiboShouQuan(username,'sina')
        msg+=u'新浪'
#        userAccessToken.sinaSecret=access_token.secret
#        userAccessToken.sinaToken=access_token.key
#        userAccessToken.sinauserid=auth_client.user_id
#        userAccessToken.sinaisright=True
#        userAccessToken.put()
#        sinaadd=memcache.Client().get("SinaAdd")
#        if not sinaadd:
#            sinaadd= []
#        sinaadd.append(username)
#        memcache.Client().set("SinaAdd",sinaadd,360000)
    elif 'wy'==website:
#        t = TBlog(weboSetting.wyconsumer_key, weboSetting.wyconsumer_secret)
        request_token=memcache.Client().get(username+"_request_token3")
        if not request_token:
            return
        memcache.Client().delete(username+"_request_token3")
#        t._request_handler.request_token=request_token
#        request_token.get_auth_url()
#        pin=self.request.get('pin', None)
        pin=self.request.get('oauth_token', None)
        s=request_token.get_access_token(pin)
        user.wySecret=s.secret
        user.wyToken=s.key
        user.put()
#        pam={'key0':'wySecret','value0':s.secret,'key1':'wyToken','value1':s.key}
#        syncMogu(username,pam)
#        syncWeiboShouQuan(username,'wy')
        msg+=u'网易'
#        userAccessToken.wySecret=s.secret
#        userAccessToken.wyToken=s.key
#        userAccessToken.wyisright=True
#        userAccessToken.put()
#        wyadd=memcache.Client().get("WyAdd")
#        if not wyadd:
#            wyadd= []
#        wyadd.append(username)
#        memcache.Client().set("WyAdd",wyadd,360000)
    elif 'teng'==website:
        request_token=memcache.Client().get(username+"_request_token4")
        if not request_token:
            return
        memcache.Client().delete(username+"_request_token4")
        verifier = self.request.get('oauth_verifier', None)
        access_token = request_token.get_access_token(verifier)
        user.tengSecret=access_token.secret
        user.tengToken=access_token.key
        user.put()
#        pam={'key0':'qqSecret','value0':access_token.secret,'key1':'qqToken','value1':access_token.key}
#        syncMogu(username,pam)
#        syncWeiboShouQuan(username,'teng')
        msg+=u'腾讯'
#        userAccessToken.qqSecret=access_token.secret
#        userAccessToken.qqToken=access_token.key
#        #userAccessToken.qquserid=auth_client.user_id
#        userAccessToken.qqisright=True
#        userAccessToken.put()
#        qqadd=memcache.Client().get("QQAdd")
#        if not qqadd:
#            qqadd= []
#        qqadd.append(username)
#        memcache.Client().set("QQAdd",qqadd,360000)
    msg+=u'微博。'

    p={'msg':msg.encode('utf-8')}

    return self.redirect(str('joke://jokeweibo/weibo'+'?msg='+urllib.urlencode(p).split('=')[1]+'&website='+website))


#def syncMogu(userName,pam={}):
#    pam['UserName']=userName
#    pam['appid']=weboSetting.WEIBOAPPCODE
#
#    result = urlfetch.fetch(
#        url =weboSetting.DBPHOTOWEBURL+'/changeAppData',
#        payload = urllib.urlencode(pam),
#        method = urlfetch.POST,
#        headers = {'Content-Type':'application/x-www-form-urlencoded',
#                   'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'},
#        follow_redirects = False,deadline=30)
#    if result.status_code==200:
#        return True
#    else:
#        return False
#def syncWeiboShouQuan(userName,web,do=None):
#    login_url =weboSetting.DBPHOTOWEBURL+ '/WeiboCheck'
#    pam={'username':userName,'web':web}
#    if do:
#        pam['do']='del'
#    login_data = urllib.urlencode(pam)
#    result = urlfetch.fetch(
#            url =login_url,
#            payload = urllib.urlencode(pam),
#            method = urlfetch.POST,
#            headers = {'Content-Type':'application/x-www-form-urlencoded',
#                       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'},
#            follow_redirects = False,deadline=20)
#    if result.status_code==200:
#        return True
#    else:
#        return False
