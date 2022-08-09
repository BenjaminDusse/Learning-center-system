from django.urls import path
from center import views

app_name = 'center'
urlpatterns = [
    path("", views.home, name="home"),

]
