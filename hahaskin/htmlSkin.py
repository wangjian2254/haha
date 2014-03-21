#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
import HTMLParser

__author__ = u'王健'


class JokePage(HTMLParser.HTMLParser):

    def clearHtml(self):
        self.infodict = {'jokecontent': '', 'jid': '', 'img': ''}
        self.info = False
        self.content = False
        self.img = False
        self.l = []
    def newjoke(self):
        self.l.append(self.infodict)
        self.infodict = {'jokecontent': '', 'jid': '', 'img': ''}
        self.info = False
        self.content = False
        self.img = False

    def handle_starttag(self, tag, attrs):
        if not self.info and tag == 'div':
            for att, val in attrs:
                if att == 'class' and val == 'block joke-item':
                    self.info = True

                if att == 'jid':
                    self.infodict['jid'] = val
        if self.info and tag == 'p':
            for att, val in attrs:
                if att == 'class' and val == 'text word-wrap':
                    self.content = True
                    self.infodict['jokecontent'] = ''

        if self.info and tag == 'img':
            for att, val in attrs:
                if att == 'src' and 0 < val.find('image.haha.mx') < 10:
                    self.infodict['img'] = val

    def handle_endtag(self, tag):
        if self.info and self.content and tag == 'div':
            self.newjoke()

    def handle_data(self, data):
        if self.info and self.content:
            if data.find('(展开全部)') < 0:
                self.infodict['jokecontent'] += data


  