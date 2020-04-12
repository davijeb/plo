from django.urls import path

from . import views

app_name = 'ploadmin'

urlpatterns = [
    path('', views.test, name='test'),
    path('detail/<int:user_id>', views.detail, name='detail'),
    path('<int:user_id>/results/', views.results, name='results'),
    path('<int:user_id>/vote/', views.vote, name='vote'),
    path('index', views.index, name='index'),
]