from django.urls import path
from django.conf.urls.static import static
from pbrlwebapp import settings

from preferences import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:query_id>/', views.query, name='query')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)