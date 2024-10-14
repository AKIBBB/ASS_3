from django.urls import path
from .views import add_category, show_categories

urlpatterns = [
    path('add/', add_category, name='add_category'),
    path('show/', show_categories, name='show_categories'),
]
