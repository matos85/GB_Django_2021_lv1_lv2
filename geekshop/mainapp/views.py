from django.shortcuts import render

from mainapp.models import Product, ProductCategory

from django.shortcuts import get_object_or_404


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    product_1 = ProductCategory.objects.all()[0]

    context = {
        'page_title': 'католог',
        'product_1': product_1,
        'categories': categories,
    }
    return render(request, 'mainapp/products.html', context)

def category(request, pk):
    pass



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


# def products(request):
#     product_1 = Product.objects.all()[0]
#
#     context = {
#         'page_title': 'каталог',
#         'product_1': product_1,
#     }
#     return render(request, 'mainapp/products.html', context)

# еще не использовл
# def productsnew(request):
#     products = Product.objects.all()[:4]
#
#     context = {
#         'slogan': 'Супер удобные стулья',
#         'topic': 'Тренды',
#         'products': products,
#     }
#     return render(request, 'index.html', context)


# еще не использовл
# def categories(request, pk=None):
#     print(pk)
#     title= 'продукты'
#     categories = ProductCategory.objects.all()
#     if pk is not None:
#         if pk ==0:
#             products = Product.object.all().order_by('price')
#             category = {'name': 'все'}
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.object.filter(category_id__pk=pk).order_by('price')
#     context = {
#         'title': title,
#         'categories': categories,
#         'category': 'category',
#         'products': 'products',
#     }
#     return render(request, 'products_list.html', context=context)
