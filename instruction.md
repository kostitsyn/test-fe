# Инструкция

1. Создаём виртуальное окружение:

```virtualenv env```

2. Активируем виртуальное окружение и устанавилваем зависимости:

```source env/bin/activate```

```pip install -r requirements.txt```

3. Создаём и выполняем миграции:

```python manage.py makemigrations mainapp```

```python manage.py migrate```

4. Запускаем скрипт по заполнению БД данными из файла *data.json*:

```python manage.py fill_db```

5. Запускаем проект:

```python manage.py runserver```