from django.urls import path
from . import views
urlpatterns = [
    path("",views.HomeApp.PageHome,name='home'),
]
