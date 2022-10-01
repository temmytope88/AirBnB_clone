#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    this a class that creates the instance of a user
    the has the public attribute email, password, first_name,
    last_name
    """
    email = ""
    password = ""
    last_name = ""
    first_name = ""
