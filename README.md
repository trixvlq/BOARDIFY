# Тестовое задание

**Стек:**

![Python](https://img.shields.io/badge/Python-4169E1?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-008000?style=for-the-badge)
![DRF](https://img.shields.io/badge/DRF-800000?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-00BFFF?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-87CEEB?style=for-the-badge)

# Описание проекта

Этот проект представляет собой API запросы по сайту с продажами.

Сайт обладает следующим функционалом:
- API запросы
- Кэширование в аутентефикации
- JWT токены

# Как запустить проект

1. Клонировать репозиторий:



```
https://github.com/trixvlq/BOARDIFY.git```

2. Создать Docker контейнер:

```
docker-compose build
```

3. Создать миграции:

```
docker-compose run --rm backend sh -c "python manage.py makemigrations"
docker-compose run --rm backend sh -c "python manage.py migrate"
```

4. Создать админа:

```
docker-compose run --rm recepies_app sh -c "python manage.py createsuperuser"
```

5. Запустить контейнер:

```
docker-compose up
```

Теперь проект доступен по адресу:

```
http://127.0.0.1/
```
