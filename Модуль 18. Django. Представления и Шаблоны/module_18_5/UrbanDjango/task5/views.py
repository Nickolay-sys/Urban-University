from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_by_html(request):
    users = ['nikolay', 'alex', 'vasya']
    info = {}
    context = {
        'info': info,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >=18 and username not in users:
            return HttpResponse(f'Приветсвуем, {username}!')
        if password != repeat_password:
            info.update({'error': 'пароли не совпадают'})
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18'})
        if username in users:
            info.update({'error': 'Пользователь уже существует'})
    return render(request, 'fifth_task/registration_page.html', context)
            
            
def sign_up_by_django(request):
    users = ['nikolay', 'alex', 'vasya']
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form['username']
            password = form['password']
            repeat_password = form['repeat_password']
            age = form['age']
            if password == repeat_password and int(age) >=18 and username not in users:
                return HttpResponse(f'Приветсвуем, {username}!')
            if password != repeat_password:
                info.update({'error': 'пароли не совпадают'})
            if int(age) < 18:
                info.update({'error': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'error': 'Пользователь уже существует'})
        else: 
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context)
                