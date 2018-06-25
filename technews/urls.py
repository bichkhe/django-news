"""technews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from boards import views
from accounts  import views as accounts_views
urlpatterns = [

    # TEST
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^boards/$', views.index, name='index'),
    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
   


    
]

