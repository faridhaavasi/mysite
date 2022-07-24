from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('articel_list',views.Articel_list),
    path('detail/<int:id>',views.detail),
    path('add_article',views.add_articel),
]
