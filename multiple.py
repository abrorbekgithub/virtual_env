import requests
import json
from tinydb import TinyDB

data=TinyDB('db.json')
# data.truncate()

user={
    "name":"abror",
    "young":25,
    "phone":123
}
user1={
    "name":"asror",
    "young":22,
    "phone":125163
}
user2={
    "name":"adror",
    "young":225,
    "phone":12555163
}
user3={
    "name":"adcsror",
    "young":2251,
    "phone":12515163
}

data.truncate()
data.insert_multiple([user,user1,user2,user3])

