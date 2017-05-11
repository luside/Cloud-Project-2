#Author:Side Lu<sidel@student.unimelb.edu.au>
#Date: 10/5/2017
#Project:COMP90024 Cluster and Cloud Computing Assignment2import json
from dateutil import parser
import json

count={'morning':0,'afternoon':0,'night':0,
       'morning-pos':0,'afternoon-pos':0,'night-pos':0,
	   'morning-neu':0,'afternoon-neu':0,'night-neu':0,
	   'morning-neg':0,'afternoon-neg':0,'night-neg':0}


	
    #twitter data uses american time
	#we must take time difference into consideration   
def collect(data):
    date=parser.parse(data["key"]['time'])
    if date.hour>=12 and date.hour<20:
        count['morning']+=1
        if data["key"]["score"]>0:
            count['morning-pos']+=1
        if data["key"]["score"]==0:
            count['morning-neu']+=1
        if data["key"]["score"]<0:
            count['morning-neg']+=1
    if date.hour>=20 or date.hour<4:
        count['afternoon']+=1
        if data["key"]["score"]>0:
            count['afternoon-pos']+=1
        if data["key"]["score"]==0:
            count['afternoon-neu']+=1
        if data["key"]["score"]<0:
            count['afternoon-neg']+=1
    if date.hour>=4 and date.hour<12:
        count['night']+=1
        if data["key"]["score"]>0:
            count['night-pos']+=1
        if data["key"]["score"]==0:
            count['night-neu']+=1
        if data["key"]["score"]<0:
            count['night-neg']+=1

#allfile.json is all documents in couchDB after removing duplicates
with open("allfile.json",encoding='utf-8') as json_data:
    iter=0
    for line in json_data:
        iter+=1
        if iter>2:
            try:
                line = line[:-2]
                data = json.loads(line)
                collect(data)
            except:
                continue
    print(count)
