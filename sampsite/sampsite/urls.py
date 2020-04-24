"""sampsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# L2 loads urls for our admin site
from django.contrib import admin

# L2 instead of django.conf.urls.url "deprecated"
# matches url in browser to url in project
from django.urls import path

# L2 # reference the url files that are in our polls application using 'include'
# matches url in browser to url in project, uses regular expressions, like 'url' did,
# or non regular expressions as 'path' did
from django.urls import include, re_path

# L2 pass in local function hello_world from the views.py file
from .views import hello_world, root_page, random_number

# reference the url files that are in our polls application
# from django.conf.urls import include

urlpatterns = [
    # L2 match 'whats in here with whats in the browser, then if matched, do tied in function, in views.py
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world),
    re_path(r'^$', root_page),
    # L2 the urlpatterns using 'path' take two lines to do what re_path does in one
    # random number entered in url by user 'random/1000'
    # path('random/<int:max_rand>', random_number),
    # no number entered by user, only 'random' in the url lets default, 100 be used
    # path('random/', random_number),
    # the chronological order of these two statement matters
    re_path(r'^random/(\d+)$', random_number),
    re_path(r'^random/', random_number),
    # use import include to reference urls from poll app
    re_path('polls/', include('polls.urls')),
]
