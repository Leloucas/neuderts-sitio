from django.conf.urls import url
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.portfolio_detail, name="detail"),
]
