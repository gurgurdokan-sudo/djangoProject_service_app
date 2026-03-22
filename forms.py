from django import forms
from .models import User, ServicePlan

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'name': '氏名',
            'name_kana': 'フリガナ',
            'care_level': '要介護状態区分',
            'insured_number': '被保険者番号',
            'date_of_birth': '生年月日',
            'gender': '性別',
            'notes' : 'メモ',
        }
        widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
class PlanForm(forms.ModelForm):
    def __init__(self, *args, user_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user_id:
            self.user_id = user_id
    class Meta:
        model = ServicePlan
        fields = ['date','start_time','end_time']
        labels = {
            'date': 'サービス提供開始日',
            'start_time': '開始時間',
            'end_time': '終了時間',
        }
        widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'start_time': forms.TimeInput(attrs={'type': 'time'}),
        'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }