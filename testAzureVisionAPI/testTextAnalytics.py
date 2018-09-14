
import requests
from pprint import pprint
from IPython.display import HTML
import json

subscription_key = 'c401180d0a724be69782174db43aa608'
assert subscription_key

text_analytics_base_url = "https://japaneast.api.cognitive.microsoft.com/text/analytics/v2.0/"

# Detect languages

language_api_url = text_analytics_base_url + "languages"

sentiment_api_url = text_analytics_base_url + "sentiment"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"

entity_linking_api_url = text_analytics_base_url + "entities"

print(language_api_url)
print(sentiment_api_url)
print(key_phrase_api_url)
print(entity_linking_api_url)

documents = {
    'documents': [
        {'id': '1', 'text': 'This is a document written in English.'},
        {'id': '2', 'text': 'Este es un document escrito en Español.'},
        {'id': '3', 'text': '这是一个用中文写的文件'},
        {'id': '4', 'text': 'これは日本語文書です'},
        {'id': '5', 'text': '이것은 일본어 문서입니다'},
        {'id': '6', 'text': 'これはEnglish documents written in English.'}
    ]
}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url,headers=headers,json=documents)

languages = response.json()

pprint(json.dumps(languages, indent=4))

table = []

for document in languages["documents"]:
    text = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
    langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))

#pprint(table)



documents_setiment = {
    'documents' : [
    {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
    {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},
    {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},
    {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'},
    {'id': '5', 'language': 'ja', 'text': 'こんな馬鹿な回答は駄目でしょう。何をしている？お前は'},
    {'id': '6', 'language': 'zh_chs', 'text': '这是一次很好的旅行体验，无论是导游的专业性还是服务上都是上乘！'}
]}

response_setiment = requests.post(sentiment_api_url, headers=headers, json=documents_setiment)
setiments = response_setiment.json()

#The sentiment score for a document is between $0$ and $1$, with a higher score indicating a more positive sentiment.
pprint(json.dumps(setiments, indent=4, ensure_ascii=False))

response_key_phrases = requests.post(key_phrase_api_url,headers=headers,json=documents_setiment)
key_phrases = response_key_phrases.json()
pprint(json.dumps(key_phrases, indent=4, ensure_ascii=False))

documents_entity = {
    'documents' : [
        {'id': '1', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.'},
        {'id': '2', 'text': 'The Seattle Seahawks won the Super Bowl in 2014.'},
        {'id': '3', 'text': 'ドリーム・アーツは「意識共有」の基盤であるINSUITEを本日から大企業お客様向けにご提供いたします'}
]}
response_entity = requests.post(entity_linking_api_url,headers=headers,json=documents_entity)
entities = response_entity.json()
pprint(json.dumps(entities, indent=4, ensure_ascii=False))