import datetime as dt
from django.db import models


class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=256, unique=True, verbose_name='Имя пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name

    @property
    def get_total_time(self):
        user_days = self.day_set.all()
        total_time = dt.timedelta(hours=0, days=0)
        for day in user_days:
            if day.start and day.end:
                total_time += day.get_time
        return total_time


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата')
    start = models.TimeField(verbose_name='Время начала', null=True)
    end = models.TimeField(verbose_name='Время окончания', null=True)

    def __str__(self):
        return f'{self.user.name}: {self.date}'

    @property
    def get_time(self):
        if self.start and self.end:
            result = dt.timedelta(hours=self.end.hour, minutes=self.end.minute) - \
                     dt.timedelta(hours=self.start.hour, minutes=self.start.minute)
        else:
            result = 0
        return result

