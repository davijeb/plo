from django.urls import path

from . import views

app_name = 'ploadmin'

urlpatterns = [
    path('', views.test, name='test'),
    path('detail/<int:user_id>', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('modify/<int:user_id>', views.modify, name='modify'),
    path('index', views.index, name='index'),
]