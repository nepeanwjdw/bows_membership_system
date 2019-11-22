from django.urls import include, path, re_path
from .views import RetrieveEmployeeView, RegisterEmployeeView, EmployeeDetailsView, TopUpView

urlpatterns = [
    re_path(r'^users/get-id/(?P<card_id>[a-zA-Z0-9]{16})/$', RetrieveEmployeeView.as_view()),
    re_path('^users/register/(?P<card_id>[a-zA-Z0-9]{16})/$', RegisterEmployeeView.as_view()),
    re_path(r'^users/get-details/(?P<id>\d{6})/$', EmployeeDetailsView.as_view()),
    re_path(r'^users/top-up/(?P<id>\d{6})/$', TopUpView.as_view()),
    path('users/', include('rest_auth.urls')),
]
