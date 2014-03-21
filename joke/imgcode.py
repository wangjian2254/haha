#coding=utf-8
#author:u'王健'
#Date: 13-3-5
#Time: 下午9:27
from google.appengine.api import memcache

from joke.safecode import ImageCode
from models.model import UserAccessToken
from tools.page import Page


__author__ = u'王健'

class ImgCode(Page):
   def get(self):
        img=ImageCode()
        img.create()
        imgcode=str(img.text)
        memcache.set(self.request.get('imgcode','111'),imgcode,36000)
        self.response.headers['Content-Type'] = "image/png"
        self.response.out.write(img.img.dump())


class Baidu(Page):
    def get(self):
        self.response.out.write("00242beb80964cb2c1ed6bd3b7593944")
        u=UserAccessToken()
        u.qqSecret = '5846415b2c341c23e9154008025393f7'
        u.qqToken = '151df8254b824f0fb3bc48ed8f7d03c3'
        u.qqisright = True
        u.sinaExpires = '1522066881'
        u.sinaSecret = '2.00HGNhqCdb1iQBb8eed27af80MRd2r'
        u.sinaToken = '7860a0f91f4ddf79f4c0f019c7a5d866'
        u.sinaisright = True
        u.sinauserid = '2610933591'
        u.wyisright = True
        u.wySecret = '2d213529803ab28090f822b896b9b29e'
        u.wyToken = '1c63afb34efb5d7a424c9c9b44b335fe'
        u.put()


  