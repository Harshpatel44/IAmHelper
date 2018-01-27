import requests
import re
import json


def get_response(word_id):
    # language='en'
    # #word_id='harsh'
    # app_id = '433bec40'
    # app_key = '90d6bd1e273afb373e23e082604d6d8d'
    #
    # url='https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()+'/synonyms'
    # r=requests.get(url,headers={'app_id':app_id,'app_key':app_key})
    # string=r.content
    # result=re.findall("\"synonyms\": .*\W.*\W.*\"id\":\W\"(.*)\"",string)


    print(word_id)
    url="""http://api.wordnik.com/v4/word.json/"""+str(word_id).lower()+"""/definitions?limit=200&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"""
    r=requests.get(url)
    string=r.content
    print(string)
    j=json.loads(string)
    return j[0]["text"]


