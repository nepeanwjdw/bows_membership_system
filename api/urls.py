from django.urls import path

from . import views

urlpatterns = [
    path('users/<card_id>/', views.RetrieveEmployee.as_view()),
]
