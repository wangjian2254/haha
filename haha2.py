#coding=utf-8
import json
import uuid
from google.appengine.api import memcache
from loginmanage import get_current_user, getUser, setLogin
from models.model import DefaultDate, Joke, Replay, UserJoke
from tools.page import Page
import datetime
timezone=datetime.timedelta(hours =8)

__author__ = '王健'

class listHaHa_redict(Page):
    def get(self,limit=20,pagenum=1,nowpage=1,jokeid='j'):
        self.redirect('/')
class listHaHa2(Page):
    def get(self,date=None,page=1,limit=20):
        perdate=''
        afterdate=''
        if None==date:
            defaultdate=DefaultDate.get_by_key_name('date')
            date=defaultdate.date
            afterdate='flage'

        html=memcache.get('date'+date+'page'+str(page)+'limit'+str(limit))
        if html:
            return self.flashhtml(html)
        perdate=(datetime.datetime.strptime(date,'%Y%m%d')-datetime.timedelta(hours =24)).strftime('%Y%m%d')
        if not afterdate:
            afterdate=(datetime.datetime.strptime(date,'%Y%m%d')+datetime.timedelta(hours =24)).strftime('%Y%m%d')
        else:
            afterdate=''
        if page:
            page=int(page)
        if limit:
            limit=int(limit)
        hahamap=memcache.get('query:date'+date+'page'+str(page)+'limit'+str(limit))
        if not hahamap:
            hahalist=[]
            for joke in Joke.all().filter('date =',date).order('-updateTime'):
                hahalist.append(joke)
            total=int(len(hahalist)/limit)
            for i in range(total):
                if i==(total-1):
                    memcache.set('query:date'+date+'page'+str(i+1)+'limit'+str(limit),{'hahalist':hahalist[i*limit:],'total':len(hahalist)},3600*72)
                else:
                    memcache.set('query:date'+date+'page'+str(i+1)+'limit'+str(limit),{'hahalist':hahalist[i*limit:(i+1)*limit],'total':len(hahalist)},3600*72)
        hahamap=memcache.get('query:date'+date+'page'+str(page)+'limit'+str(limit))
        if not hahamap:
            self.redirect('/%s/1/%s'%(perdate,limit))
            return
        totalpage=hahamap.get('total',0)
        nowpage=None
        pagelist=[]
        for p in range(int(totalpage/limit)):
            if (page-1)==p:
                nowpage='/%s/%s/%s'%(date,(p+1),limit)
            pagelist.append({'page':'/%s/%s/%s'%(date,(p+1),limit),'pagenum':p+1})
        if perdate==date:
            perdate=''
        html=self.obj2str('templates/jokeindex.html',{'hahalist':hahamap.get('hahalist',[]),'pagelist':pagelist,'nowpage':nowpage,'pagenum':page,'limit':limit,'nowdate':date,'perdate':perdate,'afterdate':afterdate})
        memcache.set('date'+date+'page'+str(page)+'limit'+str(limit),html,3600*5*page)
        self.flashhtml(html)
        return

class lookHaHa2(Page):
    def get(self,jokeid=None):
        html=memcache.get('joke'+jokeid)
        if not html :
            ha=Joke.get_by_key_name(jokeid)
            html=self.obj2str('templates/jokedetail.html',{'ha':ha,'uuid':str(uuid.uuid4()),'guest':{}})
            memcache.set('joke'+jokeid,html,720000)
        self.flashhtml(html)
class replayHaHa2(Page):
    def post(self,jokeid=None):
        num=memcache.get('replayjokenum'+jokeid)
        if num==None:
            num=Replay.all().filter('joke =',jokeid).count()
            memcache.set('replayjokenum'+jokeid,num,720000)
        self.flashhtml('{"success":true,"replaynum":%s}'%num)
class HaHa2CommentList(Page):
    def get(self):
        jokeid=self.request.get('jokeid')
        html=memcache.get('replayjoke'+jokeid)
        if not html:
            replaylist=[]
            for replay in Replay.all().filter('joke =',jokeid).order('-updateTime'):
                rmap={}
                rmap['id']=replay.key().id()
                rmap['jokeid']=replay.joke
                rmap['face']=replay.face
                rmap['content']=replay.content
                rmap['createDate']=replay.updateTime.strftime('%Y年%m月%d日 %H:%M:%S')
                rmap['fatherid']=replay.fatherid_id
                rmap['userid']=replay.user
                rmap['username']=getUserName(replay.user)
                replaylist.append(rmap)
            html=json.dumps(replaylist)
            memcache.set('replayjoke'+jokeid,html,7200)
        self.flashhtml(html)
class HaHa2CommentAdd(Page):
    def get(self):
        code=self.request.get('code','')
        codename=self.request.get('codename','')
        codestr=memcache.get(codename)
        if codestr==code:
            self.flashhtml('{"success":true}')
        else:
            self.flashhtml('{"success":false,"msg":"%s"}'%(u'验证码错误',))
    def post(self):
        code=self.request.get('imagecode','')
        codename=self.request.get('codename','')
        codestr=memcache.get(codename)
        success=False
        msg=u''
        jokeid=self.request.get('jokeid')
        face=self.request.get('face')
        fatherid_id=self.request.get('fatherid_id')
        content=self.request.get('content','')
        content=content.replace('<','&lt;')
        content=content.replace('>','&gt;')
        if codestr==code:
            user_joke=get_current_user(self)
            replay=Replay()
            replay.joke=jokeid
            if fatherid_id:
                replay.fatherid_id=int(fatherid_id)
            replay.content=content
            replay.face=int(face)
            replay.user=user_joke.key().id()
            replay.updateTime=datetime.datetime.utcnow()+timezone
            replay.put()
            num=memcache.get('replayjokenum'+jokeid)
            if num!=None:
                memcache.set('replayjokenum'+jokeid,num+1,720000)
            memcache.delete('replayjoke'+jokeid)
            self.redirect('/%s.html'%jokeid)
        else:
            self.redirect('/%s.html'%jokeid)


class HaHa2getUser(Page):
    def post(self):
        user=get_current_user(self)
        if not user:
            self.flashhtml('{"success":false}')
        else:
            self.flashhtml('{"success":true,"nickname":"%s","userid":%s}'%(user.nickname,user.key().id()))


class HaHa2Success(Page):
    def get(self):
        if 'login'==self.request.get('do','login'):
            msg=u'登录'
        elif 'reg'==self.request.get('do','login'):
            msg=u'注册'
        html=self.obj2str('templates/success.html',{'msg':msg})
        self.flashhtml(html)
class HaHa2Reg(Page):
    def get(self):
        html=self.obj2str('templates/reg.html',{'uuidstr':str(uuid.uuid4())})
        self.flashhtml(html)
    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        r_password=self.request.get('r_password')
        nickname=self.request.get('nickname')
        code=self.request.get('code','')
        codename=self.request.get('codename','')
        codestr=memcache.get(codename)
        success=False
        msg=u''
        if username and password and r_password and nickname and len(nickname)>2 and len(username)>5 and len(password)>6:
            if password!=r_password:
                msg=u'密码和确认密码不一致'
            else:
                if codestr!=code:
                    msg=u'验证码不正确'
                else:
                    userlist=UserJoke.all().filter('username =',username).fetch(1)
                    if 0==len(userlist):
                        import hashlib
                        userjoke=UserJoke()
                        userjoke.nickname=nickname
                        userjoke.pwd=hashlib.md5(password).hexdigest().upper()
                        userjoke.username=username
                        userjoke.put()
                        setLogin(self,userjoke.key().id())
                        success=True
                    else:
                        msg=u'用户名已经存在'
        else:
            msg=u'用户名、密码、确认密码、昵称不能为空'
        if success:
            self.redirect('/joke/success?do=reg')
        html=self.obj2str('templates/reg.html',{'uuidstr':str(uuid.uuid4()),'msg':msg,'username':username,'password':password,'nickname':nickname,'r_password':r_password})
        self.flashhtml(html)
class HaHa2Login(Page):
    def get(self):
        html=self.obj2str('templates/login.html',{'uuidstr':str(uuid.uuid4())})
        self.flashhtml(html)
    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        code=self.request.get('code','')
        codename=self.request.get('codename','')
        codestr=memcache.get(codename)
        success=False
        msg=u''
        if username and password:
            if codestr!=code:
                msg=u'验证码不正确'
            else:
                userlist=UserJoke.all().filter('username =',username).fetch(1)
                if 1==len(userlist):
                    import hashlib
                    if userlist[0].pwd==hashlib.md5(password).hexdigest().upper():
                        success=True
                        setLogin(self,userlist[0].key().id())
                    else:
                        msg=u'密码错误'
                else:
                    msg=u'用户名不存在'
        else:
            msg=u'用户名、密码不能为空'
        if success:
            self.redirect('/joke/success?do=login')
        html=self.obj2str('templates/login.html',{'uuidstr':str(uuid.uuid4()),'msg':msg,'username':username,'password':password})
        self.flashhtml(html)
def getUserName(user):
    user_joke=getUser(user)
    return user_joke.nickname









  