from django.shortcuts import render, redirect, get_object_or_404
# djangoが提供しているUserModelを使用
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required

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
            # ログイン成功したらlistページへリダイレクト
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})


# ログインしてなければLOGIN_URLにリダイレクトするようデコレーターをつける
@login_required
def listfunc(request):
    # BoardModelのデータを全てとってきてobject_listに入れる
    object_list = BoardModel.objects.all()
    # renderで渡すデータを辞書型で記載。キーとバリューは基本同じ名前にする。html上でキーを記載するとバリューを呼び出せる
    return render(request, 'list.html', {'object_list': object_list})

# ログアウト機能。ログアウト後はloginページへ遷移
def logoutfunc(request):
    logout(request)
    return redirect('login')

# 投稿の詳細表示。urlに入っているpkを引数に渡す
def detailfunc(request, pk):
    # BoardModelにデータがあればオブジェクトに入れる。なければエラーを返す。持ってくるデータはpkで判断
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})