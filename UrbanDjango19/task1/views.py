from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, Post
from django.core.paginator import Paginator
#from django.core.paginators import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.hashers import make_password


def post_list(request):
    # получаем все посты
    posts = Post.objects.all()
    # создаем пагинатор
    # paginator = Paginator(posts, 5) # 5 постов на странице
    per_page = int(request.GET.get('per_page', 5))
    paginator = Paginator(posts, per_page)  # Пагинация с учетом выбранного значения
    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page', 1)
    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)
    # передаем контекст в шаблон

    context = {
        'page_posts':page_posts,
        'paginator':paginator,
        'per_page':per_page,  # Передаем выбранное значение per_page в контекст
    }

    return render(request, 'post_list.html', context)


# Список существующих пользователей
users = ['Иван Иванов', 'Анна Сидорова']

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            age = form.cleaned_data['age']

            if password1 != password2:
                form.add_error('password2', 'Пароли не совпадают')
            elif age < 18:
                form.add_error('age', 'Вы должны быть старше 18 лет')
            elif Buyer.objects.filter(name=username).exists():
                form.add_error('username', 'Пользователь с таким именем уже существует')
            else:
                buyer = Buyer.objects.create(name=username, balance=5000.00, age=age)
                buyer.save()
                return render(request, 'fifth_task/registration_success.html', {'username':username})
        else:
            pass  # Оставляем форму без изменений, если она невалидная
    else:
        form = UserRegister()

    context = {
        'form': form
    }
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        age = int(request.POST.get('age'))

        if password1 != password2:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь с таким именем уже существует'
        else:
            buyer = Buyer.objects.create(name=username, balance=5000.00, age=age)
            buyer.save()
            return render(request, 'fifth_task/registration_success.html', {'username':username})

    return render(request, 'fifth_task/registration_page.html', info)


def platform(request):
    return render(request, 'platform.html')


def games(request):
    # Получаем все записи из таблицы Game
    all_games = Game.objects.all()

    # Формируем контекст для передачи в шаблон
    context = {
        'games':all_games
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')

