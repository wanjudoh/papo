from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from myprofile.models import Profile
from market.models import Market, Scrap
from myprofile.models import Profile
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now! 즉 [signup!]버튼을 눌렀을 때 일어나는 일
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                   request.POST['username'], 
                   password=request.POST['password1'])
                nickname = request.POST['nickname']
                email = request.POST['email']
                name = request.POST['name']
                profile = Profile(user=user, name=name, nickname=nickname, email=email)
                profile.save()
                auth.login(request, user)
                return redirect('home')
        else:
           return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info --> 유저가 정보를 입력하고 있는 중임.
        return render(request, 'signup.html')


def login(request):
   if request.method == 'POST': #로그인 버튼을 눌렀을 때
       username = request.POST['username']
       password = request.POST['password1']
       user = auth.authenticate(request, username=username, password=password)
       if user is not None: #사용자 정보를 알맞게 입력한 경우
           auth.login(request, user)
           return redirect('home')
       else: #잘못 입력한경우
           return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
   else:
       return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       return redirect('home')
    return render(request, 'signup.html')


def mypage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    scraps = Scrap.objects.filter(user=request.user).order_by('-scrap_date')
    return render(request, 'mypage.html', {'user':user, 'scraps':scraps})


def info(request):
    return render(request, 'info.html')
