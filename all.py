import requests
import json
from tinydb import TinyDB

db=TinyDB('db.json')
data=db.all()

for i in data:
    print(i["name"],i["young"],end='   ')