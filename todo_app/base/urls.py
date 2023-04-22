from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('todo/<str:pk>', views.todo, name= "todo"),
    path('create_todo/', views.createTodo, name = "create_todo"),
    path('update_todo/<str:pk>', views.updateTodo, name = "update_todo"),

]