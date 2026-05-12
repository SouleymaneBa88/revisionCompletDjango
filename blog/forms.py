from django import forms 
from .models import Commentaire
from django.contrib.auth.forms import UserCreationForm



class Commentform(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['message'] 

# class InscriptionForm(UserCreationForm):
#     class Meta:
#         model = User