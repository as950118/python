#myapp/views.py
from django.shortcuts import render
from .forms import signup_form
from .forms import login_form
from django.contrib.auth import login, authenticate

def main(req):
    return render(req, 'myapp/main.html',{})
def signup(req):
    form = signup_form()
    return render(req, 'myapp/signup.html',{'form':form})
def login(req):
    form = login_form()
    return render(req, 'myapp/login.html',{'form':form})

#Post
from .models import signup_model

def signup_post(req):
    try:
        data = req.POST
        obj = signup_model(id = data['id'], pwd = data['pwd'], email=data['email'], sex=data['sex'], tel=data['tel'])
        obj.save()
        print("Signup Success")
        return render(req, 'myapp/main.html',{})
    except Exception as e:
        print("Signup Failed :", e)
        return render(req, 'myapp/signup.html',{})

def login_post(req):
    try:
        data = req.POST
        auth = authenticate(id = data['id'], pwd = data['pwd'])
        if auth:
            print('Login Success')
            return render(req, 'myapp/main.html',{})
        else:
            print("Login Faield : not auth")
            return render(req, 'myapp/login.html',{})
    except Exception as e:
        print("Login Faield :", e)
        return render(req, 'myapp/login.html',{})
