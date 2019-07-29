from django.urls import path, include

from . import views


app_name = 'minerals'
urlpatterns = [
    path('', views.minerals_home, name='minerals-home'),
    path('<int:pk>', views.mineral_detail, name='minerals-detail'),
    path('random/', views.mineral_random, name='minerals-random'),
    path('search/', views.search_page, name='minerals-search'),
    path('search_by_letter/', views.search_by_letter, name='minerals-search_by_letter'),
    path('search_by_group/', views.search_by_group, name='minerals-search_by_group'),
    path('search_by_diaphaneity/', views.search_by_diaphaneity, name='minerals-search_by_diaphaneity'),
]
