from rest_framework import serializers
from django import forms
from .models import *



class LockedTokensForm(forms.ModelForm):
    class Meta:
        model = LockedTokenModel
        fields = ['token_address', 'amount', 'target_address']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = managerModel
        fields = "__all__"










