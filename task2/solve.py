import json
from dateutil.parser import *
from dateutil import *
import datetime
from datetimerange import DateTimeRange

# taking the logins.json and grepping for successful logon or logged off
json_file='narrowed.json'

# put the data into a list
data = []
with open(json_file) as f:
    for line in f:
        data.append(json.loads(line))

# parsing through the json data for LogonId
logins = {}
for i in range(len(data)):
    # print(data[i]['PayloadData3'])
    login_id = data[i]['PayloadData3'].replace("LogonId: ", "")
    if login_id not in logins:
        logins[login_id] = []
    # if it is a logon, take the time
    if 'logon' in data[i]['MapDescription']:
        logins[login_id] = data[i]['TimeCreated']

    # if it is a log off entry, take the time
    if 'logged off' in data[i]['MapDescription']:
        new_list = [logins[login_id],data[i]['TimeCreated']]
        logins[login_id] = new_list

# for the times found, check if it is in between the time in the proxy.log 
# because it has to within there 
for key in logins:
    start = parse(logins[key][0])
    end = parse(logins[key][1])
    time = parse('2021-03-16 08:34:49')
    if time.timestamp() <=end.timestamp() and time.timestamp() >= start.timestamp():
        print(key)