#!/usr/bin/python3
import ctypes
import urllib3
import simplejson as json
import requests
from datetime import datetime
from datetime import time
import time as systime

## Get transpotation information from VBB's API
# def getStationInfo(name):
#     rest_url = getStationInfoURL(name)
#     res_json = httpGet(rest_url)
#     print(res_json)
#     if res_json is not None:
#         return res_json
#     return "No data return"
#
# def getStationInfoURL(name):
#     vbb_url = 'https://vbb.transport.rest/stations'
#     query = {'query': name}
#     rest_url = getRestURL(vbb_url, query)
#     return rest_url
#
# def getDataFromVBB(rest_url):
#     http = urllib3.PoolManager()
#     rest_url = getCurrntStationURL()
#     res_json = httpGet(rest_url)
#     if res_json is not None:
#         nameList = []
#         for place in res_json:
#             nameList.append(place['name'])
#         return nameList
#     return "No data return"
#
# def getRestURL(vbb_url, coordinate):
#     count = 0
#     for key, value in coordinate.items():
#         if count is 0:
#             rest_url = vbb_url + "?" + key + "=" + str(value)
#         else:
#             rest_url += "&" + key + "=" + str(value)
#         count += 1
#     return rest_url
#
# def getStationNearbyURL():
#     coordinate = getCoordinate()
#     if coordinate is not None:
#         vbb_url = 'https://vbb.transport.rest/stations/nearby'
#         rest_url = getRestURL(vbb_url, coordinate)
#         return rest_url
#     return None
#
# def getCoordinate():
#     send_url = 'http://freegeoip.net/json'
#     j = httpGet(send_url)
#     try:
#         coordinate = {'latitude': j['latitude'], 'longitude': j['longitude']}
#         return coordinate
#     except ValueError:
#       return None
#
# def httpGet(send_url):
#     res = requests.get(send_url)
#     if res.status_code is 200:
#         return httpResponse(res.text)
#     return None
#
# def httpResponse(resText):
#     if resText is None:
#         zeroResponse = { 'latitude' : 0, 'longitude' : 0 }
#         return zeroResponse
#     else:
#         res_json = json.loads(resText)
#         return res_json

def MsgBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def countdown(seconds):
    systime.sleep(seconds)
    
def diffTime(start, stop):
    seconds = timeinseconds(stop) - timeinseconds(start)
    if seconds <= 0:
        seconds = 1
    return seconds

def timeinseconds(t):
    h,m,s = t.split(':')
    seconds = int(h)*60*60 + int(m)*60 + int(s)
    return seconds

def validTime(h,m,s):
    if int(h) > 23 or int(m) > 59 or int(s) > 59:
        return False
    return True

def checkFaile(t):
    try:
        h, m, s = t.split(':')
        if validTime(h,m,s):
            return False
        else:
            return True
    except ValueError:
        return True

def main():
    leave = input("When do you plan to leave? (hh:mm:ss) >>> ")
    while checkFaile(leave):
        leave = input("Please follow the formate and retype again.  Ex: 23:59:59 >>> ")
    now = datetime.now().strftime("%H:%M:%S")
    sec = diffTime(now, leave)
    countdown(sec)
    MsgBox("Schdule Alert", "Time to go!", 1)

if __name__ == '__main__':
    main()