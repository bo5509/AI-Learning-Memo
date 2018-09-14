# -*- coding: utf-8 -*-

import http.client, urllib.parse, uuid, json

subscriptionKey = 'ebd2b0bebad746449120866dd8d2c4eb'
assert  subscriptionKey
host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

params = "&to=ja&to=en"

text = '你好,我是DreamArts的一名员工。'

print("要翻译："+text)

def translate (content):
    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    conn = http.client.HTTPSConnection(host)
    conn.request("POST", path+params, content, headers)
    response = conn.getresponse()
    return response.read()

requestBody = [
    {
        "Text": text,
    }
]
content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
result = translate(content)
output = json.dumps(json.loads(result), indent=4, ensure_ascii=False)

print(output)
