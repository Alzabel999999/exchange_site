from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path("request_send", request_send, name="request_send"),
]
urlpatterns += staticfiles_urlpatterns()
