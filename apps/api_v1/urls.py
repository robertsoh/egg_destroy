from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^scores$', views.ScoreCreateListAPIVIEW.as_view(), name='scores'),
]
