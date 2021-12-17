import json
import collections
import datetime as dt
from datetime import datetime
import requests
# url = 'https://api.openweathermap.org/data/2.5/forecast/climate'
url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {'q': 'Yekaterinburg',
          'appid': '72ea70a4fae1d141ca0d517871f7caba',
          'units': 'metric',
          'cnt': '31'
          }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

response = requests.get(url, params=params, headers=headers)

j_data = response.json()

# j_data['list'][0]['main']['temp']
print(j_data)

# with open('789.json', 'w') as f:
#     json.dump(j_data, f, indent=4, sort_keys=True)
# print(f'Температура {round(j_data["main"]["temp"], 2)}')

# with open('data.json') as f:
#     data = json.load(f)
#
#
# with open('data1.json', 'w') as f1:
#     json.dump(data, f1, sort_keys=True, indent=4)

# with open('data.json') as f:
#     data = json.load(f)
#     res_list = list()  # результирующий список с отформатированными данными
#     for user in data:
#         user_dict = dict()  # словарь с данными конкретного пользователя
#         user_dict['fullname'] = user.get('Fullname')
#
#         days_list = user['Days']
#
#         format_day_data = dict()  # словарь содержащий информацию о том
#                                   # сколько часов работал пользователь каждый день
#         total_time = None
#         for day_data in days_list:
#
#             day_num = datetime.strptime(day_data.get('Date'), '%Y-%m-%d').date().day
#
#             start_time_obj = datetime.strptime(day_data.get('Start'), '%H-%M')
#             end_time_obj = datetime.strptime(day_data.get('End'), '%H-%M')
#
#             res_time = (end_time_obj - dt.timedelta(hours=start_time_obj.hour,
#                                                         minutes=start_time_obj.minute)).time()
#             if total_time == None:
#                 total_time = dt.timedelta(hours=res_time.hour, minutes=res_time.minute)
#             else:
#                 total_time += dt.timedelta(hours=res_time.hour, minutes=res_time.minute)
#
#             format_day_data[day_num] = str(res_time)
#
#         user_dict['total_time'] = str(total_time)
#         for i in range(1, 32):
#             if i not in format_day_data.keys():
#                 format_day_data[i] = 0
#         format_day_data = collections.OrderedDict(sorted(format_day_data.items()))
#         user_dict['days'] = format_day_data
#         res_list.append(user_dict)
#     print()