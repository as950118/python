#myapp/forms.py
from django import forms
#from django.contirb.auth.models import 
class signup_form(forms.Form):
    elems = ['ID', 'PWD', 'EMAIL', 'SEX', 'TEL']
    sex_choices = (('M', 'm'), ("F",'f')) #성별에 관해
    id = forms.CharField(label=elems[0], max_length=128)
    pwd = forms.CharField(label=elems[1], max_length=128)
    email = forms.EmailField(label=elems[2], max_length=254)
    sex = forms.ChoiceField(label=elems[3], choices=sex_choices)
    tel = forms.CharField(label=elems[4], max_length=128)

class login_form(forms.Form):
    elems = ['ID', 'PWD']
    id = forms.CharField(label=elems[0], max_length=128)
    pwd = forms.CharField(label=elems[1], max_length=128, widget=forms.PasswordInput)
