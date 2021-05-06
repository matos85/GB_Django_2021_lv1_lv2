"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from mainapp import urls
import mainapp.views as mainapp
from geekshop import settings

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contacts'),
    # path('', include(urls)),

    path('admin/', admin.site.urls),

]

# если включен режим дебага
# то добавить к urlpatterns функцию статик.
# сделать доступ к папке медиа  будут доступны на продукт
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
