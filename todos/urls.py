from django.urls import path
from . import views # '.' 대신 'todos'를 써도 된다. '.' : 같은 폴더

urlpatterns = [
    path('', views.index),

    path('new/', views.new),
    path('create/', views.create),
]