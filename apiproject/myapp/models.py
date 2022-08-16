import json

from django.db import models
from django.db import models
import numpy as np
from rest_framework import serializers
from datetime import datetime, date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import pandas as pd
from django.urls import path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from django.conf import settings
import face_recognition
import requests
from django.shortcuts import render

class Contact(models.Model):
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to='covers/')


    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)

        if self.Picture:
            """
            In this part, we handled the input pictures directly. At first we created the post request payload for face detection
            """
            pic = Image.open(self.Picture.path)
            pic.save('media/out.png')
            value = self.Description
            url = 'http://face-detector-app123.herokuapp.com/myapi/'
            payload = {'Description': value}
            # in this part, we did get request payload for face detection
            files = [
                ('Picture', ('out.png', open('media/out.png', 'rb'), 'image/png'))
            ]
            headers = {}
            requests.request("POST", url, headers=headers, data=payload, files=files)
            response = requests.get('http://face-detector-app123.herokuapp.com/myapi')
            res = response.json()
            picture = res[-1]['set_attributes']['Picture']
            # taking image from the url(picture)
            picture_request = requests.get(picture)
            if picture_request.status_code == 200:
                with open("media/out2.png", 'wb') as f:
                    f.write(picture_request.content)

            #In this part, we handled the face detected pictures directly.
            # then we created the post request payload for template

            url = 'http://template-creat.herokuapp.com/myapi/'
            payload = {'Description': value}
            files = [
                ('Picture', ('out2.png', open('media/out2.png', 'rb'), 'image/png'))
            ]
            headers = {}
            requests.request("POST", url, headers=headers, data=payload, files=files)
            # in this part, we did get request payload for template
            response = requests.get('http://template-creat.herokuapp.com/myapi/')
            res = response.json()
            description = res[-1]['set_attributes']['Description']
            picture = res[-1]['set_attributes']['Picture']
            picture_request = requests.get(picture)
            if picture_request.status_code == 200:
                with open("media/out3.png", 'wb') as f:
                    f.write(picture_request.content)
            template = Image.open('media/out3.png')
            template.save(self.Picture.path)


def __str__(self):
    return self.Description

# Create your models here.
