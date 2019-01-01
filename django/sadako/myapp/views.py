from django.shortcuts import render

# Create your views here.
def main(req):
    return render(req, 'myapp/main.html',{})
def signup(req):
    return render(req, 'myapp/signup.html',{})
def login(req):
    return render(req, 'myapp/login.html',{})
def mypage(req):
    return render(req, 'myapp/mypage.html',{})
def bbs(req):
    return render(req, 'myapp/bbs.html',{})
def gallery(req):
    return render(req, 'myapp/gallery.html',{})

def signup_post(req):
    id = req.POST['id']
    print(id)
    return render(req, 'myapp/main.html',{})
