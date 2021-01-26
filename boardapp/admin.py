from django.contrib import admin
from .models import BoardModel

# adminでモデルを表示させる
admin.site.register(BoardModel)