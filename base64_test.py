#!/usr/bin/env python

import paho.mqtt.client as mqtt
import os
import sys
import base64
import json
import time
import threading

pls = "IzsjGWtBAQAjJSI9sEMBACM7IiP0SwEAIzsiIm5WAQAiOyMa2mABACI7Ih1WawEAIjsiPjt6AQAkLysjdYQBACs7Ih2YhAEAIjsiHyiIAQAiOyIfMY4BACI7Ih26mAEAIjsiHRSjAQAiKiYfAKoBACYqJk8pqgEAJiYmDYKqAQAmKiVZj6oBACUqJkLoqgEAJSomQZurAQAmKiJJ5qsBAA=="
arr = base64.b64decode(pls).hex()
print(arr)
print('\n')

print(bytearray.fromhex(arr))
print('\n')

y = [ord(c) for c in base64.b64decode(pls).hex()]

print(y)
print('\n')

host = "192.168.0.228"
port = 1883
client_id = "123456789"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/#")         # 订阅消息

raw_buffer  = {}
def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode()))
    revmsg = json.loads(msg.payload.decode())
    print(revmsg)
    print("\n")
    # pls = revmsg["1"]
    for v in revmsg:
        print(v)
    print(revmsg['token'])
    for p in revmsg['stu']:
        print(p)
    print("\n")
    print(revmsg['stu'][0]['pls'])
    print(revmsg['stu'][1]['pls'])
    print(revmsg['stu'][2]['pls'])

    print('callback')
    for i in range(0,3):
        print(str(i))
        if len(revmsg['stu'][i]['pls']) != 0:
            print(i, 'is not Null')

def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

client = mqtt.Client(client_id)
client.username_pw_set("xxxxxx", "xxxxxx")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(host, port, 60)
client.loop_forever()