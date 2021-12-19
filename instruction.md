# Инструкция

1. Создаём и выполняем миграции:

```python manage.py makemigrations```

```python manage.py migrate```

2. Запускаем скрипт по заполнению БД данными из файла *data.json*:

```python manage.py fill_db```

3. Запускаем проект:

```python manage.py runserver```