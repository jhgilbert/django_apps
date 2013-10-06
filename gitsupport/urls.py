from django.conf.urls import patterns, url

from gitsupport import views

urlpatterns = patterns('',
    url(r'^danger_hook', views.danger_hook, name='danger_hook')
)
