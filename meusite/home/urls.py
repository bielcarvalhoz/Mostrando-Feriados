from django.urls import path
from . import views

urlpatterns = [
    path('', views.TemplateHomeView.as_view(), name='home'),
]
