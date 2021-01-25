from django.shortcuts import render
# djangoが提供しているUserModelを使用
from django.contrib.auth.models import User

def signupfunc(request):
    # Userモデルのオブジェクト全てをobject_listに格納
    object_list = User.objects.all()
    print(object_list)
    # Userモデルのデータの一部を取り出すことも可能。.getに引数を渡し、該当のデータをインスタンス化
    object = User.objects.get(username='nsktky')
    # object.要素でモデルに定義されたデータを扱える
    print(object.email)
    
    if request.method == 'POST':
        print('This is post method')
    else:
        print('This is not post method')
    # renderメソッドはhttpレスポンスを作成する
    return render(request, 'signup.html', {'some': 100})