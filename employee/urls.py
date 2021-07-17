from django.urls import path
from .import views       # ピリオドインポートは相対という意味、views.pyを読み込む

app_name = 'employee'   # アプリケーション名を「employee」に指定

urlpatterns = [
    path('',views.IndexView.as_view(),name='index')     # から文字列にすることで、「127.0.0.1:8000」と打つと、indexビューが呼ばれる
]



# 動画８５の5分53秒　employeeフォルダ内に、このurls.pyファイルを作成