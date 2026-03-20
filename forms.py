from django import forms
from .models import User

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
