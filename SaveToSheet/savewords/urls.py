from django.urls import path, include
from .views import input_words, download_excel

urlpatterns = [
    path('', input_words, name='input_words'),
    path('download/', download_excel, name='download_excel'),
]