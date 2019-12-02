from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<slug:category>/', views.category_stats),
    path('img/<slug:group>/', views.group_dist),
]