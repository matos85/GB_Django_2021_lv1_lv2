from django.shortcuts import render

from mainapp.models import Product


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'продукты'
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    contacts = [
        {'city': 'Москва',
         'phone': '+7918-88-888-8888',
         'email': 'info1@geebrains.ru',
         'address': 'Впределах МКАД'
         },
        {'city': 'Санкт-Петербург',
         'phone': '+7918-88-444-8888',
         'email': 'info2@geebrains.ru',
         'address': 'Впределах КАД'
         },
        {'city': 'Не Москва',
         'phone': '+7918-88-411-8888',
         'email': 'info3@geebrains.ru',
         'address': 'В пределах центра'
         }
    ]

    context = {
        'page_title': 'контакты',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    product_1 = Product.objects.all()[0]

    context = {
        'page_title': 'каталог',
        'product_1': product_1,
    }
    return render(request, 'mainapp/products.html', context)
