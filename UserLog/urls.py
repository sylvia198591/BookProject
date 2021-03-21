from django.urls import path
from UserLog import views
from django.conf.urls import url
from UserLog import views
from UserLog.views import ExampleView, CustomAuthToken
urlpatterns = [
    path('api/users/',ExampleView.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
]


