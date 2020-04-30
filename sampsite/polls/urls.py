# L2 instead of django.conf.urls.url "deprecated"
# matches url in browser to url in project
from django.urls import re_path
# L2
from . import views

# namespace to Django knows to use these names within the polls directory
app_name = 'polls'

urlpatterns = [
    # match 'whats in here with whats in the browser, then if matched, do tied in function, in views.py
    # L2 polls/index
    re_path(r'^$', views.index, name='index'),
    # L3 polls/detail, using the question id
    re_path(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
    # L3 polls/results/
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # L3 polls/vote, using the question id
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]

