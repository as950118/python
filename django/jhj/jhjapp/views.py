#views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# Create your views here.
def main(req):
    return render(req, 'jhjapp/main.html', {})
def signup(req):
    #get방식으로 접속
    if req.method == 'GET':
        return render(req, 'jhjapp/signup.html', {'form':UserCreationForm()})
    #post방식으로 접속
    else: #req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid(): #forn이 유효하면
            form.save() #저장함
            print("Signup Success !")
            return render(req, 'jhjapp/main.html', {}) #메인페이지로 이동
        else: #유효하지않으면
            print("Signup Faield :", e)
            return render(req, 'jhjapp/signup.html', {'form':UserCreationForm()}) #다시 회원가입으로
def login(req):
    if req.method == 'GET':
        return render(req, 'jhjapp/login.html', {})
    else:
        form = authenticate(username = username, password = password)
        if form:
            login(req, form)
            print("Login Success !")
            return render(req, 'jhjapp/mypage.html', {}) #메인페이지로 이동
        else:
            print("Login Faield :", e)
            return render(req, 'jhjapp/login.html', {}) #다시 회원
def mypage(req):
    return render(req, 'jhjapp/mypage.html', {})
def bbs(req):
    return render(req, 'jhjapp/bbs.html', {})
