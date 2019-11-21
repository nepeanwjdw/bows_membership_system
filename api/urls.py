from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^users/get-id/(?P<card_id>[a-zA-Z0-9]{16})/$', views.RetrieveEmployee.as_view()),
    re_path(r'^users/top-up/(?P<id>\d{6})/$', views.TopUpBalance.as_view()),
    path('users/', include('rest_auth.urls')),
]
