import requests
from IPython.display import HTML

import json

subscription_key = "19d9e0033aed4c9f8081236f856590f8"
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

search_term = 'DreamArts'

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params = {"q": search_term,"textDecorations": True, "textFormat": "HTML"}

response = requests.get(search_url,headers=headers,params=params)

response.raise_for_status()

search_results = response.json()

print(json.dumps(search_results,indent=4, ensure_ascii=False))

rows = "\n".join(["""<tr>
                       <td><a href=\"{0}\">{1}</a></td>
                       <td>{2}</td>
                     </tr>""".format(v["url"],v["name"],v["snippet"]) \
                  for v in search_results["webPages"]["value"]])
HTML("<table>{0}</table>".format(rows))