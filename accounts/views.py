from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth # 이사람이 어떤 권한을 가지고있는지 확인할때 사용하는것!

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']: # 만약 가입할때 비번이랑 비번확인이랑 같으면
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'이미 존재하는 아이디입니다!'})
            except User.DoesNotExist:
                user = User.objects.create_user( # User 클래스를 기반으로 한 쿼리셋에서 유저를 만드는 함수!
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다!'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'아이디, 혹은 비밀번호를 다시 확인해보세요!'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')

# def signup(request):
#     if request.method =='POST':
#         userId = request.POST['userid']
#         pwOrigin = request.POST['userPw']
#         pwConfirm = request.POST['userPw2']
#         if pwOrigin != pwConfirm:
#             return render(request, 'signup.html', {'error':'비밀번호가 맞지 않습니다.'})
#         else:
#             user = User.objects.create_user(userId,password=pwOrigin)
#             auth.login(request, user) # 회원가입 하자마자 바로 로그인해버리는 방법!!
#             return redirect('home')
#     else:
#         return render(render, 'signup.html')