from django.urls import path

from . import views

urlpatterns = [
    path('articel_list',views.Articel_list),
]
