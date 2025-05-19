from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('request-call/', views.request_call_view, name='request_call'),
    path('track-soldier/', views.track_soldier_view, name='track_soldier'),
    path('book-flight/', views.book_flight_view, name='book_flight'),
    path('medical-report/', views.medical_report_view, name='medical_report'),
]

