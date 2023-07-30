from django import forms

class RequestForm(forms.Form):
    amount_input = forms.IntegerField()
    amount_output = forms.IntegerField()
    telegram_login = forms.CharField(label='Логин телеграм', widget=forms.TextInput())
    fio = forms.CharField(label='Ф.И.О', widget=forms.TextInput())
    description = forms.CharField(label='Примечание', widget=forms.TextInput())
