
from django.urls import path,include, re_path
from . import  views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'minor'

urlpatterns = [

    path('',views.HomeView.as_view(),name='new-home'),
    path('project/<int:pk>/',views.ProjectDetailView.as_view(), name= 'project'),
    path("group-registration/", views.group_registration,name='group-registration'),
    path("faculty-registration/", views.faculty_registration,name='faculty-registration'),
    path('login/', views.user_login,name='user-login'),
    path('logout/', views.user_logout,name = 'user-logout'),
    path('project-form/', views.project_form_view, name = 'project-form'),
    path('coordinator-projects/', views.coordinator_home, name = 'coordinator-home'),
    path('mentor-approval/<int:pk>/', views.mentor_approval, name= 'mentor-approval'),
    path('hod-approval/<int:pk>/', views.hod_approval, name= 'hod-approval'),
    path('project/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
