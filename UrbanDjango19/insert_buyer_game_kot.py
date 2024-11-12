import os
import django

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango19.settings')
django.setup()

# Шаг 1: Импортируем необходимые модели
from task1.models import Buyer, Game, Task1GameBuyer


# Создаем 3 записи в таблице Buyer
buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=25)  # старше 18
buyer2 = Buyer.objects.create(name='Bob', balance=50.00, age=17)    # младше 18
buyer3 = Buyer.objects.create(name='Charlie', balance=150.00, age=30)  # старше 18

# Создаем 3 записи в таблице Game
game1 = Game.objects.create(title='Game A', cost=30.00, size=1.5, description='Fun game A', age_limited=True)   # с ограничением по возрасту
game2 = Game.objects.create(title='Game B', cost=20.00, size=2.0, description='Fun game B', age_limited=False)  # без ограничения по возрасту
game3 = Game.objects.create(title='Game C', cost=40.00, size=3.0, description='Fun game C', age_limited=True)   # с ограничением по возрасту

# Связываем покупателей с играми
# Все игры должны быть доступны Charlie (buyer3)
game1.buyer.set([buyer1, buyer3])  # Игра 1 доступна Alice и Charlie
game2.buyer.set([buyer1, buyer2, buyer3])  # Игра 2 доступна всем
game3.buyer.set([buyer1, buyer3])  # Игра 3 доступна Alice и Charlie

# Проверка записей
print("Buyers:")
for buyer in Buyer.objects.all():
    print(f'Buyer: {buyer.name}, Age: {buyer.age}, Balance: {buyer.balance}')

print("\nGames:")
for game in Game.objects.all():
    print(f'Game: {game.title}, Age Limited: {game.age_limited}, Buyers: {[b.name for b in game.buyer.all()]}')

