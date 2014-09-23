#!/usr/bin/python
#This script will update google spreadsheet with led value from m/monit server json response
import sys
import json
import urllib2
import os
import requests
from datetime import datetime
from subprocess import Popen
import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheets.data
from KAhostNameDict import kahost_dict
from DLhostNameDict import dlhost_dict
from BRhostNameDict import brhost_dict
#
date = str(datetime.now())
#----read json from url
try:
    #subprocess.Popen(['curl','-c','~/.mmonit/cookie','http://mmonit.vyoma-media.com:10001/index.csp')
    #subprocess.Popen(['curl','-b','~/.mmonit/cookie','-d','z_username=admin','-d','z_password=******',' http://mmonit.vyoma-media.com:10001/z_security_check')
    #data = Popen(['ciurl','~/.mmonit/cookie','http://mmonit.vyoma-media.com:10001/status/hosts/list'])
    #data = urllib2.urlopen(url).read()
    #data = json.loads(data)
    #print data
    #subprocess.Popen(['/usr/bin/bash','/opt/dashboard-app/curltofile.sh'])
    json_file = open('json.txt')
    data = json.load(json_file)
    json_file.close()
    #print data
except:
    #print "server busy or not responding!"
    with open('/opt/dashboard-app/dashboard.log','a') as f:
         f.write(date)
         f.write(' server not responding or host not data avilable!\n')
         f.close()  
    quit()
#
#------ read from local file
#json_file = open('Formatted-mmonit.json')
#data = json.load(json_file)
#json_file.close()
# print data
#
#---dict for store led values(eg:0,1,2,3)
dict_led = {}
dict_status = {}
for record in data['records']:
    store = record['hostname']
    dict_led[store] = record['led']
    dict_status[store] = record['status']
#
#print dict_led
#print dict_status 
#--email and pwd
email = 'xyz@abc.com'
password = 'password***'
spreadsheet_key = '0AqVK32zw_dAldDVicGRsWWxxM1lYT3dQVmxSakduVGc'
worksheet_id = 'od6'
worksheet_id_delhi = 'od4'
worksheet_id_bihar = 'od3'
worksheet_id_status = 'od9'
worksheet_id_delhi_status = 'ocw'
worksheer_id_bihar_status = 'od1'
#
spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Monitoring|Dashboard'
spr_client.ProgrammaticLogin()
#
"""for key, value in dlhost_dict.items():
   # print  key, value
    try:
        led = unicode(dict_led[key])
        status = dict_status[key]
        row = unicode(value["row"])
        col = unicode(value["col"])
        rows = unicode(value["rows"])
        cols = unicode(value["cols"])
        #updating cell value
        spr_client.UpdateCell(row, col, led,spreadsheet_key, worksheet_id_delhi)
        spr_client.UpdateCell(rows, cols, status,spreadsheet_key, worksheet_id_delhi_status)
        #print key, row, col
    except:
        print key," ,host not avilable on server!"
#"""
for key, value in brhost_dict.items():
   #print  key, value
   try:
        led = unicode(dict_led[key])
        status = dict_status[key]
        row = unicode(value["row"])
        col = unicode(value["col"])
        rows = unicode(value["rows"])
        cols = unicode(value["cols"])
        #updating cell value
        spr_client.UpdateCell(row, col, led,spreadsheet_key, worksheet_id_bihar)
        spr_client.UpdateCell(rows, cols, status,spreadsheet_key, worksheer_id_bihar_status)
        #print key, row, col
   except:
        print key," ,host not avilable on server!"
#
#logging,time UTC std.
with open('/opt/dashboard-app/dashboard.log','a') as f:
    f.write(date)
    f.write(' google spreadsheet sucessfully updated!\n')
    f.close()








































