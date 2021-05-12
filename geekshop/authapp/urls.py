from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    # host:8000/auth/login
    path('login/', authapp.login, name='login'),
    # host:8000/auth/logout
    path('logout/', authapp.logout, name='logout'),
    path('profile/', authapp.edit, name='edit'),
    path('register/', authapp.register, name='register'),

]
