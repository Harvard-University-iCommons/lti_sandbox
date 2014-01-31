from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'simpletool.views.index', name='index'),

    url(r'^lti_launch$', 'simpletool.views.lti_launch', name='lti_launch'),

    url(r'^tool_config$', 'simpletool.views.tool_config', name='tool_config'),

    url(r'^main_page$', 'simpletool.views.main_page', name='main_page'),

    url(r'^another_page$', 'simpletool.views.another_page', name='another_page'),

)
