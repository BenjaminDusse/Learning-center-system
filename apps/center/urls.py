from django.urls import path
from center import views

app_name = 'center'
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("learning_center/", views.learning_center, name="learning_center"),
    
]
