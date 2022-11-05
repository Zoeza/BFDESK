from django.urls import path
from . import views

app_name = 'record_reporting'


urlpatterns = [

    path('add-report', views.add_report, name="add-report"),
    path('submit-report/', views.submit_report, name="submit-report"),
    path('list-report/', views.list_report, name="list-report"),
    path('search-report/', views.search_report, name="search-report"),

]