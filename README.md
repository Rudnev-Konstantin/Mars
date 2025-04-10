# Учебное веб-приложение

Учебный проект, демонстрирующий работу с основными веб-технологиями.
Разработано на Python и его библиотеках. 

## 🛠 Технологии

- **Backend**: Flask
- **Frontend**: HTML, CSS, Jinja2
- **База данных**: SQLite + SQLAlchemy ORM
- **Миграции**: Alembic
- **API**: RESTful
- **Тестирование**: pytest

## 🚀 Запуск проекта

### Установка зависимостей:

```bash
pip install -r requirements.txt
```

### Настройка окружения:

#### Инициализация БД:

```bash
alembic upgrade head
```
#### Запуск приложения:

##### Windows:
```bash
python app.py
```
##### Unix:
```bash
python3 app.py
```

#### Запуск тестов:
```bash
pytest tests/
```

## 🌐 API Endpoints

#### Пользователи:

- GET /api/users - Список пользователей
- POST /api/users - Создать пользователя
- GET /api/users/<"id"> - Получить пользователя
- PUT /api/users/<"id"> - Обновить пользователя
- DELETE /api/users/<"id"> - Удалить пользователя

#### Работы:

- GET /api/jobs - Список работ
- POST /api/jobs - Создать работу
- GET /api/jobs/<"id"> - Получить работу
- PUT /api/jobs/<"id"> - Обновить работу
- DELETE /api/jobs/<"id"> - Удалить работу

## 🧩 Основные компоненты

#### Модели данных

- Пользователи (User)
- Вакансии (Job)

#### Формы

- Регистрация
- Авторизация
- Добавление работы

#### Шаблоны

- Базовый шаблон (base.html)
- Главная страница
- Формы
