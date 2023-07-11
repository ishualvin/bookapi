from django.urls import path, include
from .import views


urlpatterns = [
    path('resume/',views.ProfileView.as_view(),name='Resume'),
    path('list/',views.ProfileView.as_view(),name='ListResume')
]
 