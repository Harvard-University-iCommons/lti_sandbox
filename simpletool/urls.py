from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'simpletool.views.index', name='index'),

    url(r'^lti_tool$', 'simpletool.views.lti_tool', name='lti_tool'),

    url(r'^tool_config$', 'simpletool.views.tool_config', name='tool_config'),

    url(r'^another_page$', 'simpletool.views.another_page'),

)
