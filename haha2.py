#coding=utf-8
import datetime
import json
import uuid
from google.appengine.api import memcache
from models.model import DefaultDate, Joke, Replay, UserJoke
from tools.page import Page

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
        if not afterdate:
            perdate=(datetime.datetime.strptime(date,'%Y%m%d')-datetime.timedelta(hours =24)).strftime('%Y%m%d')
        afterdate=(datetime.datetime.strptime(date,'%Y%m%d')+datetime.timedelta(hours =24)).strftime('%Y%m%d')
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
        html=self.obj2str('templates/result2.html',{'hahalist':hahamap.get('hahalist',[]),'pagelist':pagelist,'nowpage':nowpage,'pagenum':page,'limit':limit,'nowdate':date,'perdate':perdate,'afterdate':afterdate})
        memcache.set('date'+date+'page'+str(page)+'limit'+str(limit),html,7200)
        self.flashhtml(html)
        return

class lookHaHa2(Page):
    def get(self,jokeid=None):
        html=memcache.get('joke'+jokeid)
        if not html:
            ha=Joke.get_by_key_name(jokeid)
            html=self.obj2str('templates/joke.html',{'ha':ha,'uuid':str(uuid.uuid4()),'guest':{}})
            memcache.set('joke'+jokeid,html,7200)
        self.flashhtml(html)
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
                rmap['createDate']=replay.createDate.strftime('%Y年%m月%d日 %H:%M:%S')
                rmap['fatherid']=replay.fatherid_id
                rmap['userid']=replay.user
                rmap['username']=getUserName(replay.user)
                replaylist.append(rmap)
            html=json.dumps(replaylist)
            memcache.set('replayjoke'+jokeid,html,7200)
        self.flashhtml(html)

def getUserName(user):
    user_joke=memcache.get('userbyid'+str(user))
    if not user_joke:
        user_joke=UserJoke.get_by_id(user)
        memcache.set('userbyid'+str(user),user_joke,7200)
    return user_joke.nickname









  