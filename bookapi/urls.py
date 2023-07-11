from django.urls import path, include
from .import views


urlpatterns = [
    path('',views.BookView.as_view()),
    path('list/',views.BookView.as_view()),
    path('list/<int:pk>',views.BookView.as_view())
]
 