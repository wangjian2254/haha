#coding=utf-8
#author:u'王健'
#Date: 13-3-5
#Time: 下午9:27
from google.appengine.api import memcache
from safecode import ImageCode
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
        self.response.out.write("95083c7309aa026bb71de129552f83c9")


  