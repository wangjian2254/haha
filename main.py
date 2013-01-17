#coding=utf-8
#
from check import checkHaHa
from haha import getHaHa, newHaHa, listHaHa, getJokeByPhone, Reg, SendWeibo, Robots
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
    ('/', listHaHa),
    ('/android', listHaHa),
    ('/(\d+)/(\d+)/(\d+)/(j\d+)[/]{0,1}', listHaHa),
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
