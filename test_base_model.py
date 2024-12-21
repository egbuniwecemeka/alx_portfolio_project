#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(f"\n{my_model}")
my_model_json = my_model.to_dict()
print(f"\n{my_model_json}")
