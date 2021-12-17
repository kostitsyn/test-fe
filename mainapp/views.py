import json
import collections
import requests
import datetime as dt
from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.http import JsonResponse


class TableView(ListView):
    template_name = 'mainapp/index.html'
    paginate_by = 10

    def get_queryset(self):

        with open('data.json') as f:
            data = json.load(f)
            res_list = list()  # результирующий список с отформатированными данными
            for user in data:
                user_dict = dict()  # словарь с данными конкретного пользователя
                user_dict['fullname'] = user.get('Fullname')

                days_list = user['Days']

                format_day_data = dict()  # словарь содержащий информацию о том
                # сколько часов работал пользователь каждый день
                total_time = None
                for day_data in days_list:
                    day_num = datetime.strptime(day_data.get('Date'), '%Y-%m-%d').date().day

                    start_time_obj = datetime.strptime(day_data.get('Start'), '%H-%M')
                    end_time_obj = datetime.strptime(day_data.get('End'), '%H-%M')

                    res_time = (end_time_obj - dt.timedelta(hours=start_time_obj.hour,
                                                                minutes=start_time_obj.minute)).time()
                    if total_time == None:
                        total_time = dt.timedelta(hours=res_time.hour, minutes=res_time.minute)
                    else:
                        total_time += dt.timedelta(hours=res_time.hour, minutes=res_time.minute)

                    format_day_data[day_num] = str(res_time)
                user_dict['total_time'] = str(total_time)

                for i in range(1, 32):
                    if i not in format_day_data.keys():
                        format_day_data[i] = 0
                format_day_data = collections.OrderedDict(sorted(format_day_data.items()))

                user_dict['days'] = format_day_data
                res_list.append(user_dict)
                if self.kwargs.get('name'):

            return res_list



def get_temperature(request, day=None):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        params = {'q': 'Yekaterinburg',
                  'appid': '72ea70a4fae1d141ca0d517871f7caba',
                  'units': 'metric',
                  'cnt': '31'
                  }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'}

        response = requests.get(url, params=params, headers=headers)

        j_data = response.json()

        temperature = j_data['list'][int(day)-1]['main']['temp']
        return JsonResponse({'result': f'Погода на {day} число {temperature} градусов'})


# def search_by_name(request, name=None):
#     is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
#     if is_ajax:

