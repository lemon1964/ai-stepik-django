# AI Chat — backend (Django + DRF)

Бэкенд для AI-чата. Обеспечивает:

- Авторизацию (NextAuth)
- Подключение AI-моделей
- Обмен сообщениями
- Логику fallback
- API для фронта

## 🔗 Связан с фронтом

Репозиторий: [ai-chat-next](https://github.com/lemon1964/ai-stepik-next.git)  
Продакшен: https://ai-stepik-django.onrender.com

## ⚙️ Стэк

- [Django 5](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [gunicorn](https://gunicorn.org/)

## 🚀 Установка

```bash
git clone https://github.com/lemon1964/ai-stepik-django.git
cd ai-chat-django
cp .env.example .env
pip install -r requirements.txt
```

## 🧪 Запуск в dev-режиме

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Откройте [http://localhost:8000](http://localhost:8000)

## 🌐 Продакшен

Хостинг: [Render](https://render.com)
URL: [https://ai-stepik-django.onrender.com](https://ai-stepik-django.onrender.com)
