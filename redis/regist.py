#!/usr/bin/python3

import os
import sys
import time
import json
import redis
import urllib.request

DOCKER_HOST = os.getenv('DOCKER_HOST')


def redisDump():
  list=[]
  conn = redis.Redis(host='127.0.0.1', port=6379)
  for key in conn.keys():
    list.append( conn.get(key) )
  return list

def addData(datas):
  conn = redis.Redis(host='127.0.0.1', port=6379)
  for key in set(list(datas.keys()) + list(conn.keys())):
    if isinstance(key, bytes):
      key = key.decode('utf-8')
    if key in datas:
      conn.set(key, datas[key])
    else:
      conn.delete(key)


def getContainers():
  response = urllib.request.urlopen('http://' + DOCKER_HOST + '/containers/json?all=1')
  jsonData = json.loads(response.read().decode("UTF-8"))
  
  datas = {}
  for con in jsonData:
    #print(con)
    
    name = con['Names'][-1][1:]
    for port in con['Ports']:
      key = name + '_' + str(port['PrivatePort'])
      value=DOCKER_HOST.split(':')[0] + ':' + str(port['PublicPort'])
      datas[key] = value
    
  return datas
  

while True:
  addData(getContainers())
  print( redisDump() )
  sys.stdout.flush()
  time.sleep(3)

