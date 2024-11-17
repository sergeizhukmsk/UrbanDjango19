import os
import django

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango19.settings')
django.setup()

from django.contrib.auth.models import User
from task1.models import Post
import random

# Создаем пользователей, если их еще нет
User.objects.create_user(username='sergeizhuk', email='admin@example.com', password='12345678')
users = User.objects.all()

# Генерируем записи
for i in range(50):
    user = random.choice(users)
    post = Post(
        title=f'Заголовок поста {i + 1}',
        content=f'Контент поста {i + 1}. Это просто пример текста.',
    )
    post.save()
