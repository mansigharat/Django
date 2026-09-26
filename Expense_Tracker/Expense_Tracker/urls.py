from django.contrib import admin
from django.urls import path
from expenses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', expenses , name="expense"),
    path('update_expense/<id>',update_expense,name='update_expense'),
    path('delete_expense/<id>',delete_expense,name="delete_expense"),
    path('login/',login_page,name="login_page"),
    path('', register_page, name="register_page"),
    path('logout/' , logout_page , name = "logout_page"),
]

