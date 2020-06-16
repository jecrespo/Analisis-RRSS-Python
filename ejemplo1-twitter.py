#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:49:04 2019

@author: ecrespo
"""

from twitter_secrets import consumer_key, consumer_secret, access_token_key, access_token_secret
from TwitterAPI import TwitterAPI
import json

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Tweet something
'''
r = api.request('statuses/update', {'status':'This is a tweet from python!'})
print(r.status_code,r.text)
'''

#Get some tweets:
r = api.request('search/tweets', {'q':'#arduino'})
#print(r.text)
for item in r:
    print("---------------->",item)

json_r = json.loads(r.text) #dict con la respuesta de la API en JSON

#Followers
followers = set(id for id in api.request('followers/ids')) #set de seguidores
friends = set(id for id in api.request('friends/ids'))

print("Tengo {} seguidores".format(len(followers)))

#Amistades de otros usuarios
usuarios = api.request('friends/list',{'user_id':'799575607420026882'})
json_usuarios = json.loads(usuarios.text)
#sacar los amigos la lista de mis amigos, ahora solo saco mis seguidores
#ejemplo 799575607420026882 - CanSatSP

print ("amigos del usuario: {}".format('799575607420026882'))
for amigo in json_usuarios['users']:
    print(amigo['id'],amigo['name'])
    
    
usuarios = api.request('friends/list',{'user_id':'1004178510'})
json_usuarios = json.loads(usuarios.text)
#sacar los amigos la lista de mis amigos, ahora solo saco mis seguidores
#ejemplo 1004178510

print ("amigos del usuario: {}".format('1004178510'))
for amigo in json_usuarios['users']:
    print(amigo['id'],amigo['name'])