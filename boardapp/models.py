from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    # settings.pyに記載した場所に画像を保存する場合は、upload_toは空
    snsimage = models.ImageField(upload_to='')
    # いいねの数ををカウントするためのフィールド
    good = models.IntegerField()
    # 既読状態を確認するためのフィールド
    read = models.IntegerField()
    # 既読をした人の名前を記録するフィールド。同じ人が既読するのを防ぐために使用
    readtext = models.TextField()