import requests
import json
from tinydb import TinyDB

data=TinyDB('db.json')

user={
    "name":"abror",
    "young":25,
    "phone":123
}

data.insert(user)

data.truncate()