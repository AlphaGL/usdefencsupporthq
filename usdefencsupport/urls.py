from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('request-call/', views.request_call_view, name='request_call'),
    path('track-soldier/', views.track_soldier_view, name='track_soldier'),

    path('admin/soldiers/', views.SoldierListView.as_view(), name='soldier_list'),
    path('admin/soldiers/add/', views.SoldierCreateView.as_view(), name='soldier_add'),
    path('admin/soldiers/<int:pk>/edit/', views.SoldierUpdateView.as_view(), name='soldier_edit'),
    path('admin/soldiers/<int:pk>/delete/', views.SoldierDeleteView.as_view(), name='soldier_delete'),

    path('admin/requests/', views.RequestCallListView.as_view(), name='request_list'),
    path('admin/flights/', views.FlightBookingListView.as_view(), name='flight_list'),
    path('admin/reports/', views.MedicalReportListView.as_view(), name='report_list'),

    path('book-flight/', views.book_flight_view, name='book_flight'),
    path('medical-report/', views.medical_report_view, name='medical_report'),


    path('leavepass/', views.leavepass_list, name='leavepass_list'),
    path('leavepass/add/', views.leavepass_create, name='leavepass_add'),
    path('leavepass/<int:pk>/edit/', views.leavepass_edit, name='leavepass_edit'),
    path('leavepass/<int:pk>/delete/', views.leavepass_delete, name='leavepass_delete'),


        # Admin login and dashboard
    path('logout/', views.logout_view, name='logout'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]

