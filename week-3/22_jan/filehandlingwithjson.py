

import json

#converting dictionary into json object
a = {"Name":"meshw","age":21}
b = json.dumps(a)
print(b)

#writing into json file

with open("week-3/22_jan/tempjson.json",'w') as j:
    json.dump(b, j)


#deserializing data
with open("week-3/22_jan/tempjson.json",'r') as j:
    c = json.load(j)
    print(c)


