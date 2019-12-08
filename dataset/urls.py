from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<slug:category>/', views.category_stats),
    path('groups/<slug:group>/', views.group_dist),
    path('img/<slug:image>/', views.image_workers),
    path('img/<slug:image>/<slug:group>/', views.image_dist),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)