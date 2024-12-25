#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new user --")

my_user = User()
my_user.first_name = "Emeka"
my_user.last_name = "Egbuniwe"
my_user.email = "egbuniwecemeka@gmail.com"
my_user.password = "welcome1234"
my_user.save()
print(my_user)