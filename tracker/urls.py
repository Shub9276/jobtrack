from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name = 'signup'),
    path('applications/',views.application_list, name='application_list'),
    path('applications/add/', views.application_add, name='application_add'),
    path('applications/<int:pk>/edit/',views.application_edit, name = 'application_edit'),
    path('applications/<int:pk>/delete/',views.application_delete, name = "application_delete"),
    path('applications/<int:pk>/status/', views.application_set_status, name='application_set_status'),
    path('match/', views.match_view, name='match'),
]