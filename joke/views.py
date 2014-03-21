#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from models.model import Joke, HtmlPage
from tools.page import Page

__author__ = u'王健'


class delJoke(Page):
    def get(self):
        for j in HtmlPage.all().fetch():
            j.delete()
        for j in Joke.all().fetch(200):
            j.delete()