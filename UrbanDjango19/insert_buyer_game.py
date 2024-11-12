import os
import django

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango19.settings')
django.setup()

# Шаг 1: Импортируем необходимые модели
from task1.models import Buyer, Game, Task1GameBuyer

# Шаг 2: Создаём объекты Buyer - Создаем трех покупателей
buyer1 = Buyer(name="Иван Иванов", balance=5000, age=25)
buyer1.save()

buyer2 = Buyer(name="Петр Петров", balance=3000, age=17)
buyer2.save()

buyer3 = Buyer(name="Анна Сидорова", balance=7000, age=30)
buyer3.save()


# Шаг 3: Создаём объекты Game - Создаем три игры
game1 = Game(title="Игра 1", cost=1500, size=20, description="Описание Игры 1", age_limited=True)
game1.save()

game2 = Game(title="Игра 2", cost=2500, size=50, description="Описание Игры 2", age_limited=False)
game2.save()

game3 = Game(title="Игра 3", cost=3500, size=75, description="Описание Игры 3", age_limited=True)
game3.save()


# Шаг 4: Связываем покупателей с играми - Назначаем покупателей играм
# Иван Иванов приобретает все игры
Game.objects.get(id=1).buyer.set([buyer1])
Game.objects.get(id=2).buyer.set([buyer1])
Game.objects.get(id=3).buyer.set([buyer1])

# Петр Петров (младше 18 лет) может приобрести только игру без возрастных ограничений
Game.objects.get(id=2).buyer.add(buyer2)

# Анна Сидорова приобретает две игры с возрастными ограничениями
Game.objects.get(id=1).buyer.add(buyer3)
Game.objects.get(id=3).buyer.add(buyer3)

