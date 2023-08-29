from django.urls import path
from . import views


urlpatterns = [
  path('job/',views.JobApp.PageJob,name='job'),
  path('Job_Single/<str:Slug>',views.JobApp.PageSingle,name='Job_Single'),
  path('PostJob/',views.JobApp.PagePostJob,name='PostJob'),
  path('JobEdit/',views.JobApp.PageEditJob,name='JobEdit'),
  path('JobDisplay/',views.JobApp.PageDisplayJob,name='JobDisplay'),
 
 
]