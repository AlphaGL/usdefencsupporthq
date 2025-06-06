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



     # Loan Requests CRUD
    path('admin/loaderrequests/', views.RequestLoaderListView.as_view(), name='loaderrequest_list'),
    path('loader_requests/add/', views.RequestLoaderCreateView.as_view(), name='loaderrequest_add'),
    path('loaderrequests/<int:pk>/', views.RequestLoaderDetailView.as_view(), name='loaderrequest_detail'),
    path('admin/loader_requests/<int:pk>/edit/', views.RequestLoaderUpdateView.as_view(), name='loaderrequest_edit'),
    path('admin/loaderrequests/<int:pk>/delete/', views.RequestLoaderDeleteView.as_view(), name='loaderrequest_delete'),


    path('form/Xb9_72hZk-LD39vPQfA1', views.FormSubmitSuccess.as_view(), name='form_success'),


        # Admin login and dashboard
    path('logout/', views.logout_view, name='logout'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]

