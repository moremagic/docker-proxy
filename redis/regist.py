#!/usr/bin/python3

import os
import sys
import time
import json
import redis
import urllib.request

DOCKER_HOST = os.getenv('DOCKER_HOST')


def redisDump():
  conn = redis.Redis(host='127.0.0.1', port=6379)
  return conn.keys()

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

    con_ip = getContainerIp(con['Id'])
    name = con['Names'][-1][1:]
    for port in con['Ports']:
      key = name + '_' + str(port['PrivatePort'])
      value=con_ip + ':' + str(port['PublicPort'])
      datas[key] = value
      print(key + "  " + value)

  return datas

def getContainerIp(con_id):
  response = urllib.request.urlopen('http://' + DOCKER_HOST + '/containers/' + con_id + '/json')
  jsonData = json.loads(response.read().decode("UTF-8"))
  return jsonData['NetworkSettings']['IPAddress']

while True:
  addData(getContainers())
  print( redisDump() )
  sys.stdout.flush()
  time.sleep(3)

