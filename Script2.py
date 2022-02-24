import json

with open("tweets.json") as f:
    data = f.readlines()
tz= {}
for i in data:
    x = json.loads(i)
    tz1 = x['user']['time_zone']
    if( tz1 in tz.keys() ):
        tz[tz1] += 1
    else:
        tz[tz1] = 1

for i,j in tz.items():
    print(str(i) + " - " + str(j))