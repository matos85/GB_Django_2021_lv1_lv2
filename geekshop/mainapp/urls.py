from django.urls import path
# from .views import index, products, contact

# from mainapp import urls
import mainapp.views as mainapp
# from geekshop import settings



app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contacts'),

    path('category/<int:pk>/', mainapp.category, name='category'),
]
