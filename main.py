#coding=utf-8
#
from check import checkHaHa
from haha import getHaHa, newHaHa, listHaHa, getJokeByPhone, Reg, SendWeibo, Robots
from haha2 import listHaHa2, listHaHa_redict, lookHaHa2, HaHa2CommentList, replayHaHa2, HaHa2CommentAdd, HaHa2getUser, HaHa2Login, HaHa2Success, HaHa2Reg
from imgcode import ImgCode
import login
from weiboManage import Login, Login_check, PubWeib


__author__ = u'王健'
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2


app = webapp2.WSGIApplication([
    ('/', listHaHa2),
    ('/android', listHaHa),
    ('/(\d+)/(\d+)/(\d+)/(j\d+)[/]{0,1}', listHaHa_redict),
#    ('/(\d+)/(\d+)/(\d+)/(j\d+)[/]{0,1}', listHaHa),
    ('/(\d+)/(\d+)/(\d+)', listHaHa2),
    ('/(j\d+).*', lookHaHa2),
    ('/replay/(j\d+)', replayHaHa2),
    ('/imagecode',ImgCode),
    ('/joke/commentList', HaHa2CommentList),
    ('/joke/commentAdd', HaHa2CommentAdd),
    ('/joke/getUser', HaHa2getUser),
    ('/joke/login', HaHa2Login),
    ('/joke/success', HaHa2Success),
    ('/joke/reg', HaHa2Reg),
    ('/(\d+)/(\d+)[/]{0,1}', newHaHa),
    ('/getHaHa', getHaHa),
    ('/check', checkHaHa),
    ('/InfoUpdate',getJokeByPhone),
    (r'/Admin/login',Login),
    (r'/Admin/login_check',Login_check),
    ('/PubWeibo',PubWeib),
    ('/Reg',Reg),
    ('/login',login.Login),
    ('/login_check',login.Login_check),
    ('/SendWeibo',SendWeibo),
    (r'/robots.txt',Robots),



                              ],
                                         debug=True)
def main():
    pass

#    util.run_wsgi_app(app)


if __name__ == '__main__':
    main()
