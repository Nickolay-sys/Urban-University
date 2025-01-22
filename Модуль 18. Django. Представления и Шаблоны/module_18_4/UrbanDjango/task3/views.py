from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, "third_task/platform.html")

def games(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077',
                             'PayDay 2']}
    return render(request, "third/games.html", context)

def cart(request):
    return render(request, 'third_task/cart.html')