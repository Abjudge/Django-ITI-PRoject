from rest_framework import serializers
from .models import *
from django.db.models import fields

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traineee
        fields = "__all__"
