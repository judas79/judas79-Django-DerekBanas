# L2 instead of django.conf.urls.url "deprecated"
# matches url in browser to url in project
from django.urls import path

from . import views


urlpatterns = [
    # match 'whats in here with whats in the browser, then if matched, do tied in function, in views.py
    path('', views.index, name='index'),
    ]