import requests
import json
from pprint import pprint
from tinydb import TinyDB,Query

db=TinyDB('user.json')
user=Query()

result=db.search(user.dob.age>65)
for i in result:
    print(i["gender"],i["name"]["first"])

# print(result[0])
