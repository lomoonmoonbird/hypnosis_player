#! /usr/local/bin/env python3.4

""" businesscard View """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import UserProfileModel
from .serializers import UserProfileSerializer
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bson import json_util, ObjectId
import json
import time
import datetime
from mongoengine import *

class RegisterView(APIView):
    """
    retrieve number of cards
    """



    def post(self, request):
        data = request.data
        # UserProfileModel(data['info'])
        name = data['info']['name']
        gender = data['info']['gender']
        age = data['info']['age']
        location = data['info']['location']
        detail = data['info']['detail']
        print(data['info']['location'])
        if UserProfileModel(
                    name=str(name),
                    gender=str(gender),
                    age=str(age),
                    location=str(location),
                    detail = str(detail),

                ).save():
            return Response({"code":'000001'}, status=status.HTTP_200_OK)
        return Response({"code":'000000'}, status=status.HTTP_200_OK)





__author__ = "moonmoonbird"
__copyright__ = "Copyright 2015 , The TeenkerOperations Project"
__version__ = "1.0.1"
__maintainer__ = "moonmoonbird"
__email__ = "lomoonmoonbird@gmail.com"
__status__ = "Development"
