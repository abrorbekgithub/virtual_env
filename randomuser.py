import requests
import json
from pprint import pprint
from tinydb import TinyDB,Query


url='https://randomuser.me/api/?results=5'
res=requests.get(url)
res=res.json()

data=res["results"]
db=TinyDB('user.json')
# db.truncate()
for i in data:
    db.insert(i)

# user=Query()
# result=db.search(user.gender.search('em'))
# for i in result:
#     print(i["name"],i["dob"]["age"],end="  ")
    
    






