from django.shortcuts import render, redirect
# djangoが提供しているUserModelを使用
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import BoardModel

# サインイン関数。新規ユーザーの作成と重複登録を防ぐ処理をする
def signupfunc(request):
    # レスポンスがpostだった場合（signup.htmlのform入力があった場合）の動作
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ユーザー作成時、重複していたらexcept
        try:
            # create_userでユーザーを作成。引数にユーザー名、メールアドレス、パスワードを渡す
            user = User.objects.create_user(username, '', password)
            # renderメソッドはhttpレスポンスを作成する
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています。'})

    return render(request, 'signup.html')


# ログイン関数。登録されたユーザーを認証する。
def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context':'logged in'})            
        else:
            return render(request, 'login.html', {'context':'not logged in'})
    return render(request, 'login.html', {'context':'get method'})            


def listfunc(request):
    # BoardModelのデータを全てとってきてobject_listに入れる
    object_list = BoardModel.objects.all()
    # renderで渡すデータを辞書型で記載。キーとバリューは基本同じ名前にする。html上でキーを記載するとバリューを呼び出せる
    return render(request, 'list.html', {'object_list': object_list})