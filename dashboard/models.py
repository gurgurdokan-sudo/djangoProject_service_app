from django.db import models
from datetime import datetime, date

LEVEL_CHOICES = [('要支護1', '要支護1'),('要支護2', '要支護2'),('要介護1', '要介護1'),('要介護2', '要介護2'),('要介護3', '要介護3'),('要介護4', '要介護4'),('要介護5', '要介護5'),]

class User(models.Model):
    name = models.CharField(max_length=100,verbose_name='被保険者氏名')
    name_kana = models.CharField(max_length=100,verbose_name='フリガナ')
    care_level = models.CharField(max_length=10,choices=LEVEL_CHOICES,verbose_name='要介護状態区分')  # 要介護1など
    insured_number = models.CharField(max_length=10, blank=True, default="",verbose_name='被保険者番号')
    date_of_birth = models.DateField(blank=True, null=True,verbose_name='生年月日')
    GENDER_CHOICES = [('male', '男性'),('female', '女性'),]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, default="female",verbose_name='性別')
    notes = models.TextField(blank=True,default="",verbose_name='メモ')
    def __str__(self):
        return self.name
    @property
    def max_separate_payment(self):
        match self.care_level:
            case '要支援1':
                return 5003
            case '要支援2':
                return 10473
            case '要介護1':
                return 16692
            case '要介護2':
                return 19705
            case '要介護3':
                return 27048
            case '要介護4':
                return 30938
            case '要介護5':
                return 36217
            case _:
                return -1

class ServiceMaster(models.Model):
    care_level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    STAY_TIME_CHOICES = [('<3','<3'),('3-4','3-4'),('4-5','4-5'),('5-6','5-6'),('6-7','6-7'),('7-8','7-8'),('8-9','8-9')]
    stay_time_category = models.CharField(max_length=20, choices=STAY_TIME_CHOICES)
    service_code = models.CharField(max_length=20)
    service_name = models.CharField(max_length=20)
    unit = models.IntegerField()  # 409 など
    description = models.CharField(max_length=100,default="2024-01-01")
    def __str__(self):
        return str(self.service_name)
    @classmethod
    def get_query_plan(cls,level,timezone):
        print(level)
        plan = cls.objects.filter(care_level = level,stay_time_category = '3-4')
        return plan.service_name if plan else -1

# class ServicePlan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.ForeignKey(ServiceMaster, on_delete=models.CASCADE)
#     year = models.IntegerField()
#     month = models.IntegerField()
#     mon = models.BooleanField(default=False)
#     tue = models.BooleanField(default=False)
#     wed = models.BooleanField(default=False)
#     thu = models.BooleanField(default=False)
#     fri = models.BooleanField(default=False)
#     sat = models.BooleanField(default=False)
#     sun = models.BooleanField(default=False)
#     time_from = models.TimeField(null=True)
#     time_to = models.TimeField(null=True)
#     notes = models.TextField(blank=True)
#     def __str__(self):
#         return str(self.year)+'年'+str(self.month)+'月'

class ServiceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceMaster, on_delete=models.CASCADE)
    date = models.DateField()
    unit = models.FloatField()
    notes = models.TextField(blank=True)
    def __str__(self):
        return str(self.user)
class ServicePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default="2024-01-01")
    start_time = models.TimeField(default="09:00")
    end_time = models.TimeField(default="15:01")

    @property
    def stay_time_category(self):
        # 時間差からカテゴリを判定
        delta = datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time)
        hours = delta.total_seconds() / 3600
        if hours <= 3:
            return '<3'
        elif 3 < hours <= 4:
            return '3-4'
        elif 4 < hours <= 5:
            return '4-5'
        elif 5 < hours <= 6:
            return '5-6'
        elif 6 < hours <= 7:
            return '6-7'
        elif 7 < hours <= 8:
            return '7-8'
        elif 8 < hours <= 9:
            return '8-9'
        else:
            return '-1'
    def __str__(self):
        return str(self.user)

