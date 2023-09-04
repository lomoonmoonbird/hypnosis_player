#! /usr/local/bin/env python3.4

""" businesscard Model """

from mongoengine import *


class UserProfileModel(DynamicDocument):
    """
    sleepcamp register  model
    """
    name = StringField(required=False) # 姓名
    gender = StringField(required=False) # 性别
    age = StringField(required=False) # 年龄
    location = StringField(required=False) # 居住地
    detail = StringField(required=False) # 睡眠问题



    meta = {'collection':'userprofile'}




__author__ = "moonmoonbird"
__copyright__ = "Copyright 2015 , The TeenkerOperations Project"
__version__ = "1.0.1"
__maintainer__ = "moonmoonbird"
__email__ = "lomoonmoonbird@gmail.com"
__status__ = "Development"
