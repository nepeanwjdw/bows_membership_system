from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^users/(?P<card_id>[a-zA-Z0-9]{16})/$', views.RetrieveEmployee.as_view()),
]
