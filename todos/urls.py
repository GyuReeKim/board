from django.urls import path
from . import views # '.' 대신 'todos'를 써도 된다. '.' : 같은 폴더

# app을 여러개 생성해 줄 수 있기 때문에 app_name으로 묶어준 후 변수를 설정해주는 편이 좋다.
app_name = 'todos'

urlpatterns = [
    # Read
    path('', views.index, name="index"),
    # Create
    path('new/', views.new, name="new"), # new/라는 경로를 new라는 변수에 저장해서 사용한다.
    path('create/', views.create, name="create"),
    # new와 create를 합친다.
    path('add/', views.add, name="add"),
    # Delete
    path('<int:id>/delete/', views.delete, name="delete")
]