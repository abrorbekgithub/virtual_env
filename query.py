import requests
import json
from tinydb import TinyDB,Query

db=TinyDB('user.json')
user=Query()
a=db.search(user.dob.age>40)
for i in a:
    print(i["name"]["first"])

# db=TinyDB('user.json')
# print(db)

# qidir=Query()
# result=db.search(qidir.age>30)

# print(result)