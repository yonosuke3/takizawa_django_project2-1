from django.db import models
from django.utils import timezone

# 動画８６の1分12秒、部署を表すモデル
class Department(models.Model):
    name = models.CharField('部署名',max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):      # defの後ろに半角スペース忘れてエラーが出た
        return self.name    # 特殊メソッドのストラ


# 動画８７の0分51秒
class Club(models.Model):
    name = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name



# 社員を表すモデル
class Employee(models.Model):
    first_name = models.CharField('名',max_length=20)
    last_name = models.CharField('姓',max_length=20)
    email = models.EmailField('メールアドレス',blank=True)
    department = models.ForeignKey(
        Department,verbose_name='部署',on_delete=models.PROTECT,      # 動画８６の9分,on_deleteのところは、部署に人が1人でもいたら、その部署を削除できない仕様
    )
    club = models.ManyToManyField(
        Club, verbose_name='部活',
    )
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return '{0}{1}{2}'.format(self.last_name,self.first_name,self.department)


# L28 models.ForeignKeyは他のモデルとの紐づけを行う処理、ここではDepartment(部署)モデルと紐づけを行っている