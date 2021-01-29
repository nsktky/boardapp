from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    # settings.pyに記載した場所に画像を保存する場合は、upload_toは空
    snsimage = models.ImageField(upload_to='')
    # いいねの数ををカウントするためのフィールド
    # nullはデータベースに値が空で入ってよいか定義できる。blankはformで入力がなくてもよいかを定義できる。
    good = models.IntegerField(null=True, blank=True, default=1)
    # 既読状態を確認するためのフィールド
    read = models.IntegerField(null=True, blank=True, default=1)
    # 既読をした人の名前を記録するフィールド。同じ人が既読するのを防ぐために使用
    readtext = models.TextField(null=True, blank=True, default='a')