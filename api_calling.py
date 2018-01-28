import requests
import re
import json


def get_response(word_id):
        try:
        print(word_id)
        url="""http://api.wordnik.com/v4/word.json/"""+str(word_id).lower()+"""/definitions?limit=200&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"""
        r=requests.get(url)
        string=r.content
        j=json.loads(string)    #loading the content in json format
        list=[]
        list.extend([j[0]['text'],j[1]['text'],j[2]['text'],j[3]['text'],j[4]['text']])
        #print(list)
        return list    #returning 5 values in list

    except:
        return ["No Result"]



