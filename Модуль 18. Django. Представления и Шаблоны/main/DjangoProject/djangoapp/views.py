from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def func(request):
    return render(request, 'func_template.html')

class ClassTemplate(TemplateView):
    template_name = 'ClassTemplate.html'
    
def cycle(request):
    list = ['aa', 'bb', 'cc', 'dd', 'ee']
    list_num  = [1.1232, 2.007, 3.543, 4.8931, 5]
    context = {
        'list': list,
        'list_num': list_num,
    }
    return render(request, 'cycle.html', context)

def if_else(request):
    list = ['aa', 'bb', 'cc', 'dd', 'ee']
    len_list = len(list)
    list_num  = [1.1232, 2.007, 3.543, 4.8931, 5]
    sum_list_num = sum(list_num)
    context = {
        'list': list,
        'len_list': len_list,
        'list_num': list_num,
        'sum_list_num': sum_list_num,
    }
    return render(request, 'if_else.html', context)

def static_show(request):
    return render(request, 'static.html')

def inheritence(request):
    return render(request, 'inheritence.html')

def get_request(request):
    name = request.GET.get('name', 'Guest')
    age = request.GET.get('age', '0')
    return HttpResponse(f'Hello, {name}, {age}')

def post_request(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        return HttpResponse(f'You said {message}')
    return render(request, 'post_request.html')

def error_request(request):
    return HttpResponse('Hello!', status=400, reason='!!!')
