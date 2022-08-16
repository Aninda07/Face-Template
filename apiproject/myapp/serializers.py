from rest_framework import serializers
from .models import Contact
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.db import transaction

class ContactSerializer(serializers.ModelSerializer):
    Description = serializers.CharField(default='Null')
    Picture = serializers.ImageField()

    class Meta:
        model = Contact
        fields = ('Description', 'Picture')

    def to_representation(self, instance):
        response = {
            "set_attributes" : super().to_representation(instance),
        }
        return response




















