# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = '19d9e0033aed4c9f8081236f856590f8'

host = 'api.cognitive.microsoft.com'
path = '/bing/v7.0/Suggestions'

mkt = 'zh-CN'
#query_str = '梦创信息(大连)'
query_str = '最近'
query = urllib.parse.quote_plus(query_str,encoding='utf-8')

params = '?mkt=' + mkt + '&q=' + query

def get_suggestions():
  "Gets Autosuggest results for a query and returns the information."

  headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
  conn = http.client.HTTPSConnection(host)
  conn.request ("GET", path + params, None, headers)
  response = conn.getresponse ()
  return response.read ().decode("utf8")

result = get_suggestions()
print (json.dumps(json.loads(result), indent=4, ensure_ascii=False))