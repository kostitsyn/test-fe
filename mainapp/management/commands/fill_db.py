import json
import datetime as dt
from datetime import datetime
from django.core.management import BaseCommand, CommandError
from mainapp.models import User, Day


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data.json') as f:
            data = json.load(f)
            for dataset in data:
                user_id = dataset.get('id')
                user_name = dataset.get('Fullname')
                try:
                    user = User.objects.create(id=user_id, name=user_name)
                except Exception as e:
                    raise CommandError(f'Не удалось создать пользователя {user_name}: {e}')
                else:
                    self.stdout.write(self.style.SUCCESS(f'Пользователь {user_name} успешно создан!'))
                num_day = 1

                for day_data in dataset['Days']:
                    date = datetime.strptime(day_data.get('Date'), '%Y-%m-%d').date()
                    while date.day != num_day:
                        self.create_empty_day(user, date, num_day)
                        num_day += 1

                    start_time = datetime.strptime(day_data.get('Start'), '%H-%M').time()
                    end_time = datetime.strptime(day_data.get('End'), '%H-%M').time()
                    try:
                        day = Day.objects.create(user=user, date=date, start=start_time, end=end_time)
                    except Exception as e:
                        raise CommandError(f'Не удалось создать запись за '
                                           f'{str(date)} для пользователя {user_name}: {e}')
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Запись за {str(date)} '
                                                             f'для пользователя {user_name} успешно создана!'))
                    num_day += 1
                if date.day != 31:
                    for i in range(date.day+1, 32):
                        self.create_empty_day(user, date, i)

    def create_empty_day(self, user, date, num_day):
        empty_day = dt.date(date.year, date.month, num_day)
        try:
            day = Day.objects.create(user=user, date=empty_day)
        except Exception as e:
            raise CommandError(f'Не удалось создать запись за '
                               f'{str(empty_day)} для пользователя {user}: {e}')
        else:
            self.stdout.write(self.style.SUCCESS(f'Запись за {str(empty_day)} '
                                                 f'для пользователя {user} успешно создана!'))
