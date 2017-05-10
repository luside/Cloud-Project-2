#Author:Side Lu<sidel@student.unimelb.edu.au>
#Date: 10/5/2017
#Project:COMP90024 Cluster and Cloud Computing Assignment2

import json
from dateutil import parser
#the bounding box of cities
Melbourne=[144.5532,-38.2250,145.5498, -37.5401]
Sydney=[150.6396, -34.1399, 151.3439, -33.5780]
Hobart=[147.1762, -42.9619, 147.4628, -42.6999]
Brisbane=[152.6859, -27.6633, 153.4685, -27.0220]
Canberra=[148.9960, -35.4799, 149.3993, -35.1244]
Perth=[115.5607, -32.4824, 116.4151, -31.4552]
Adelaide=[138.4421, -35.3490, 138.7832, -34.6481]
Darwin=[130.8151, -12.4882, 130.9691, -12.3293]
citybyweekday={'Mel':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'Syd':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'Bri':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'Per':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'Hob':[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]],
'Can':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'Dar':[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]],
'Ade':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
'none':[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]}

#input:coordinates of a point
#return: the name of the city which the point belongs to
def whichcity(x,y):
    if x>0 and y<0:
        latitude=y
        longitude=x
    if x< 0 and y>0:
        latitude=x
        longitude=y
    else:
	    return 'none'
    if longitude>=Melbourne[0] and longitude<=Melbourne[2] and latitude>=Melbourne[1] and latitude<=Melbourne[3]:
        return 'Mel'
    if longitude>=Sydney[0] and longitude<=Sydney[2] and latitude>=Sydney[1] and latitude<=Sydney[3]:
        return 'Syd'
    if longitude>=Hobart[0] and longitude<=Hobart[2] and latitude>=Hobart[1] and latitude<=Hobart[3]:
        return 'Hob'
    if longitude>=Brisbane[0] and longitude<=Brisbane[2] and latitude>=Brisbane[1] and latitude<=Brisbane[3]:
        return 'Bri'
    if longitude>=Canberra[0] and longitude<=Canberra[2] and latitude>=Canberra[1] and latitude<=Canberra[3]:
        return 'Can'
    if longitude>=Perth[0] and longitude<=Perth[2] and latitude>=Perth[1] and latitude<=Perth[3]:
        return 'Per'
    if longitude>=Adelaide[0] and longitude<=Adelaide[2] and latitude>=Adelaide[1] and latitude<=Adelaide[3]:
        return 'Ade'
    if longitude>=Darwin[0] and longitude<=Darwin[2] and latitude>=Darwin[1] and latitude<=Darwin[3]:
        return 'Dar'
    else:
        return 'none'
		

		
def countbycityandweekday(data):
    date=parser.parse(data["key"]['time'])
    key=whichcity(data["key"]["coordinate"][0],data["key"]["coordinate"][1])
    if data["key"]["score"]!=0:
        if date.weekday()==0:
            citybyweekday[key][0][0]+=data["key"]["score"]
            citybyweekday[key][0][1]+=1
        if date.weekday()==1:
            citybyweekday[key][1][0]+=data["key"]["score"]
            citybyweekday[key][1][1]+=1
        if date.weekday()==2:
            citybyweekday[key][2][0]+=data["key"]["score"]
            citybyweekday[key][2][1]+=1
        if date.weekday()==3:
            citybyweekday[key][3][0]+=data["key"]["score"]
            citybyweekday[key][3][1]+=1
        if date.weekday()==4:
            citybyweekday[key][4][0]+=data["key"]["score"]
            citybyweekday[key][4][1]+=1
        if date.weekday()==5:
            citybyweekday[key][5][0]+=data["key"]["score"]
            citybyweekday[key][5][1]+=1
        if date.weekday()==6:
            citybyweekday[key][6][0]+=data["key"]["score"]
            citybyweekday[key][6][1]+=1
        


with open("allfile.json",encoding='utf-8') as json_data:
    iter=0
    for line in json_data:
        iter+=1
        if iter>2:
            try:
                line = line[:-2]
                data = json.loads(line)
                countbycityandweekday(data)
            except:
                continue
    print(citybyweekday)
    result={'Mel':[0,0,0,0,0,0,0],
'Syd':[0,0,0,0,0,0,0],
'Bri':[0,0,0,0,0,0,0],
'Per':[0,0,0,0,0,0,0],
'Hob':[0,0,0,0,0,0,0],
'Can':[0,0,0,0,0,0,0],
'Dar':[0,0,0,0,0,0,0],
'Ade':[0,0,0,0,0,0,0],
'none':[0,0,0,0,0,0,0]}
    for key in citybyweekday:
        for i in range(len(result[key])):
            result[key][i]=citybyweekday[key][i][0]/citybyweekday[key][i][1]
    print(result)