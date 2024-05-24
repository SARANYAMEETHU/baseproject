from . import views
from django.urls import path

app_name = 'Search_app'
urlpatterns = [
        path('search/', views.SearchResult, name='SearchResult'),

]
