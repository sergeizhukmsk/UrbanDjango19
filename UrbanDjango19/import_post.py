import os
import django
from task1.models import Post

# Создаём объекты
post1 = Post.objects.create(title='Первый пост', content='Содержание первого поста')
post2 = Post.objects.create(title='Второй пост', content='Содержание второго поста')

# Получаем первый созданный объект
post = Post.objects.first()

# Меняем заголовок
post.title = 'Новый заголовок'

# Сохраняем изменения
post.save()

### Шаг 3: Выборка всех объектов из базы данных
# Получаем все записи из модели Post:

all_posts = Post.objects.all()
for post in all_posts:
    print(post.title)


### Шаг 4: Удаление одного объекта
# Удаляем первый объект из базы данных:

first_post = Post.objects.first()
first_post.delete()

### Шаг 5: Фильтрация объектов
# Фильтруем посты по дате публикации или автору:
#### Пример фильтрации статей, созданных в 2024 году:

from datetime import date

posts_in_2024 = Post.objects.filter(created_at__year=2024)

#### Пример фильтрации статей, созданных конкретным пользователем (например, администратором):

admin_posts = Post.objects.filter(author__username='admin')

