from django.db import models

# Create your models here.

"""
1. wo men de mo xing lei xu yao ji cheng zi models.Model
2. xi tong hui zi dong wei wo men tian jia yi ge zhu jian -- id
3. zi duan

    zi duan ming = model.lei xing( xuan xiang)
    
    zi duan ming qi shi jiu shi shu ju biao de zi duan ming
    zi duan ming bu yao shiyong python , mysql deng guan jian zi
    
    char(M)
    varchar(M)
    M jiu shi xuan xiang
"""


class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)
    # renwu xin fuzhi guo lai , houqi jiang yuanli

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
