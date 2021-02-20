import requests
import json
from tinydb import TinyDB,Query

db=TinyDB('db.json')
qidir=Query()
a=db.search(qidir.young>10)
for i in a:
    print(i["name"])

