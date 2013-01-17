# -*- coding: utf-8 -*-
'''
Created on Jul 28, 2011

@author: wangyouhua
'''
from t4py.tblog.tblog import TBlog
from t4py.tblog.constants import CONSUMER_KEY
from t4py.tblog.constants import CONSUMER_SECRET
from t4py.utils.token_util import TokenUtil

def get_request_token():
    t = TBlog(CONSUMER_KEY, CONSUMER_SECRET)
    return t.get_request_token()

def get_authorzie_url():
    t = TBlog(CONSUMER_KEY, CONSUMER_SECRET)
    return t.get_auth_url() #copy the url to your browser and get PIN number

def get_access_token():
    t = TBlog(CONSUMER_KEY, CONSUMER_SECRET)
    print t.get_auth_url() #copy the url to your browser and get PIN number
    verifier = raw_input('PIN: ').strip() #input PIN number
    return t.get_access_token(verifier)    
    
def store_token(user_id, token_str):
    string = token_str.replace('oauth_token_secret=', '').replace('oauth_token=', '')
    strs = string.split('&')
    token_util = TokenUtil()
    token_util.add_token(user_id, strs[1], strs[0])

def store_token_str(user_id, token_str):
    token_util = TokenUtil()
    token_util.add_token_str(user_id, token_str)
    
def restore_token_str(user_id):
    token_util = TokenUtil()
    return token_util.get_token_str(user_id)