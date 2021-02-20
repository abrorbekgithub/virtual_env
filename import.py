import requests
import json
from tinydb import TinyDB

data=TinyDB('db.json')

user={
    "name":"abror",
    "young":25,
    "phone":123
}

user1={
    "name":"asror",
    "young":22,
    "phone":13
}

data.insert(user)
data.insert(user1)
# data.truncate()