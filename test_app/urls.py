from django.urls import path

from . import views

app_name = 'test_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:param>/', views.str_param, name='str_param'),
    path('<int:param>', views.int_param, name='int_param'),
]
