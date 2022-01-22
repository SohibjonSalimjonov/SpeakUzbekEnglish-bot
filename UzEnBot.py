import requests
# import json
from pprint import pprint as print


def UzEn(word):
    app_id = '4fb22252'
    app_key = '786b9f73ef528902ce5870a6a1cbbabc'
    language = 'en-gb'

    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    res=r.json()
    if 'error' in res.keys():
        return False

    audio=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    output={}
    definitions=[]

    senses=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']

    for sense in senses:
        definitions.append(f"✅ {sense['definitions'][0]}")
    output['definitions']='\n'.join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=audio

    return output



if __name__=='__main__':
    print(UzEn('python'))
