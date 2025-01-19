from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.characters, name='characters'),
    path('fight/', views.fight, name='fight'),
    path('notes/', views.notes, name='notes'),
    path('history/', views.history, name='history')
]