from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
import json
from .forms import RequestForm
from django.http import HttpResponse
from .models import RequestExchange


# Create your views here.
class MainView(View):
    def get(self, request):
        popup_status = 0
        form = RequestForm()
        return render(request, 'main/index.html', {'form': form, 'popup_status': popup_status})
    def post(self, request):
        popup_status= 1
        amount_input = float(request.POST.get('amount_input'))
        telegram_login = str(request.POST.get('telegram_login'))
        input = str(request.POST.get('change_value_from'))
        output = str(request.POST.get('change_value_to'))
        input_card = str(request.POST.get('input_card'))
        output_card = str(request.POST.get('output_card'))
        fio = str(request.POST.get('fio'))
        description = str(request.POST.get('description'))
        if not telegram_login.startswith('@'):
            telegram_login = '@' + str(telegram_login)
        request_ex = RequestExchange(input=input, output=output, input_card=input_card, output_card=output_card, amount_input=amount_input, telegram_login=telegram_login, fio=fio, description=description)
        request_ex.save()
        url = "https://api.telegram.org/bot"
        channel_id = '#'
        token = '#'
        url += token
        method = url + "/sendMessage"
        import requests as reqs
        s = 'Пришла заявка ' + '\n' + 'Пользователь: ' + telegram_login + '\n' + 'Отдает ' + str(amount_input) + ' ' + str(input) + '\n' 'С ' + str(input_card) + '\n' + 'Получает: ' + str(output) + '\n' + 'На ' + str(output_card) + '\n' + 'Ф.И.О.: ' + str(fio) + '\n' + 'Примечание: ' + str(description)
        r = reqs.post(method, data={
            "chat_id": channel_id,
            "text": s})
        return render(request, 'main/index.html', {'popup_status': popup_status})

def request_send(request):
    popup_status_new = 1
    amount_input = float(request.POST.get('amount_input'))
    telegram_login = str(request.POST.get('telegram_login'))
    input = str(request.POST.get('change_value_from'))
    output = str(request.POST.get('change_value_to'))
    input_card = str(request.POST.get('input_card'))
    output_card = str(request.POST.get('output_card'))
    fio = str(request.POST.get('fio'))
    description = str(request.POST.get('description'))
    if not telegram_login.startswith('@'):
        telegram_login = '@' + str(telegram_login)
    request = RequestExchange(input=input, output=output, input_card=input_card, output_card=output_card, amount_input=amount_input, telegram_login=telegram_login, fio=fio, description=description)
    request.save()
    url = "https://api.telegram.org/bot"
    channel_id = '#'
    token = '#'
    url += token
    method = url + "/sendMessage"
    import requests as reqs
    s = 'Пришла заявка ' + '\n' + 'Пользователь: ' + telegram_login + '\n' + 'Отдает ' + str(amount_input) + ' ' + str(input) + '\n' 'С ' + str(input_card) + '\n' + 'Получает: ' + str(output) + '\n' + 'На ' + str(output_card) + '\n' + 'Ф.И.О.: ' + str(fio) + '\n' + 'Примечание: ' + str(description)
    r = reqs.post(method, data={
        "chat_id": channel_id,
        "text": s})
    return render(request, 'main/request.html', {'popup_status_new': popup_status_new})
