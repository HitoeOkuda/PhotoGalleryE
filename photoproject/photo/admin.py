from django.contrib import admin
#CustomUserをインポート
# Register your models here.
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカムラを設定するクラス
    
    '''
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカムラにリンクを設定
    list_display_links = ('id','totle')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカムラを設定するクラス

    '''
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカムラにリンクを設定
    list_display_links = ('id','totle')

#Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category,CategoryAdmin)

###