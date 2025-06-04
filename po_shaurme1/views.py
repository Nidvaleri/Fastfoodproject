from django.shortcuts import render

def home(request):
    dishes = [
        {"name": "Популярное блюдо", "image_url": "/static/images/shaurma.jpg"},
        {"name": "Популярное блюдо", "image_url": "/static/images/shaurma.jpg"},
        {"name": "Популярное блюдо", "image_url": "/static/images/shaurma.jpg"},
    ]
    reviews = [
        {"text": "Супер!", "author": "Анна"},
        {"text": "Вкусно! Вкусно .", "author": "Иван"},
    ]
    return render(request, 'index.html', {'dishes': dishes, 'reviews': reviews})

def menu(request):
    return render(request, 'menu.html')

def reviews(request):
    return render(request, 'reviews.html')

def contacts(request):
    return render(request, 'contacts.html')

def order(request):
    return render(request, 'order.html')
