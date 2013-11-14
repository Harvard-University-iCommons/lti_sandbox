from django.conf.urls import patterns, url



urlpatterns = patterns('',

    url(r'^$', 'simpletool.views.index'),

    url(r'^lti_tool$', 'simpletool.views.lti_tool'),

    url(r'^another_page$', 'simpletool.views.another_page'),
)

