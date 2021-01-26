from django.shortcuts import render
# djangoが提供しているUserModelを使用
from django.contrib.auth.models import User

def signupfunc(request):
    # レスポンスがpostだった場合（signup.htmlのform入力があった場合）の動作
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # create_userでユーザーを作成。引数にユーザー名、メールアドレス、パスワードを渡す
        user = User.objects.create_user(username, '', password)

    # renderメソッドはhttpレスポンスを作成する
    return render(request, 'signup.html', {'some': 100})