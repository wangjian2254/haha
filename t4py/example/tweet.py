# -*- coding: utf-8 -*-
'''
Created on Jul 29, 2011

@author: wangyouhua
'''
from t4py.tblog.tblog import TBlog
from t4py.tblog.constants import CONSUMER_KEY
from t4py.tblog.constants import CONSUMER_SECRET
from t4py.http.oauth import OAuthToken
from t4py.utils.token_util import TokenUtil
import json

content = "Hello From Python SDK"    
token_util = TokenUtil()
token_str = token_util.get_token_str('user_test')
t = TBlog(CONSUMER_KEY, CONSUMER_SECRET)
t._request_handler.access_token = OAuthToken.from_string(token_str)

pic_url = json.read(t.statuses_upload("pic.jpg"))    #upload picture
content +=pic_url["upload_image_url"]
print t.statuses_update({"status":content})    #tweet
