#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")

my_user = User()
my_user.first_name = "Emeka"
my_user.last_name = "Egbuniwe"
my_user.email = "egbuniwecemeka@gmail.com"
my_user.password = "welcome1234"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")

my_user = User()
my_user.first_name = "Chidewu"
my_user.last_name = "Blessing"
my_user.email = "blessing1234@gmail.com"
my_user.password = "welcome12345"
my_user.save()
print(my_user)