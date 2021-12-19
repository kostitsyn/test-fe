import requests
import datetime as dt
from django.views.generic import ListView
from django.http import JsonResponse
from .models import User, Day


class TableView(ListView):
    template_name = 'mainapp/index.html'
    queryset = User.objects.prefetch_related('day_set').all()
    paginate_by = 10


class TableFilterView(ListView):
    template_name = 'mainapp/index.html'
    paginate_by = 10

    def get_queryset(self):
        search_name = self.request.GET.get('searchname')
        found_users = User.objects.prefetch_related('day_set').filter(name__icontains=search_name)
        return found_users


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
        return JsonResponse({'result': f'Погода в Екатеринбурге на {day} число {temperature} градусов'})


class SortedListView(ListView):
    template_name = 'mainapp/index.html'
    paginate_by = 10

    def get_queryset(self):
        direct = self.kwargs.get('direct')
        num_col = int(self.kwargs.get('num_col'))
        if direct == 'up':
            sorted_days = sorted(Day.objects.select_related('user').filter(date__day=num_col),
                                 key=lambda x: x.get_time if x.start else dt.timedelta(hours=0, minutes=0))
        else:
            sorted_days = sorted(Day.objects.select_related('user').filter(date__day=num_col),
                                 key=lambda x: x.get_time if x.start else dt.timedelta(hours=0, minutes=0), reverse=True)
        res = [day.user for day in sorted_days]
        return res