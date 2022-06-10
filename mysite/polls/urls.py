from django.urls import path
from . import views

urlpatterns = [
    # path関数 path(route,view,kwarges.name)
    path('', views.index, name='index'),
]