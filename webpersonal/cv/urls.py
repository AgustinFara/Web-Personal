from django.urls import path
from . import views


#patts de la app polls
app_name = 'cv'
urlpatterns = [
    path('about', views.about, name='about'), #Página sobre mi  
]