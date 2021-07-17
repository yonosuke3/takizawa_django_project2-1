from django import forms
from .models import Club, Department


class SearchForm(forms.Form):          # form.Formクラスを継承する
    club = forms.ModelChoiceField(                                 # ChoiceFieldは選択する入力欄が作成される
        queryset=Club.objects, label='サークル', required=False)    # 各入力欄を属性として定義する

    department = forms.ModelChoiceField(
        queryset=Department.objects, label='部署', required=False)


# 動画８８の0分15秒で、forms.pyファイルを作成、検索フォームを作るためのファイルか？