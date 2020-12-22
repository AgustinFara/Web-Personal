from django.urls import path
from . import views


#patts de la app polls
app_name = 'cv'
urlpatterns = [
    path('about', views.about, name='about'), #Página sobre mi  
    path('cv', views.cv, name='cv'), #Experiencia Laboral
    path('tech', views.tech, name='tech'), #Tecnologías
]