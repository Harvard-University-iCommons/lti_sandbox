from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from ims_lti_py.tool_config import ToolConfig

import logging

logger = logging.getLogger(__name__)


# Create your views here.

@require_http_methods(['GET'])
def index(request):
    logger.info("request to index.")
    return render(request, 'simpletool/index.html')


@login_required(login_url='error')
@require_http_methods(['POST'])
def lti_launch(request):

    if request.user.is_authenticated:
        return redirect('st:main_page')

    else:
        return redirect('error')


@login_required(login_url='error')
@require_http_methods(['GET'])
def main_page(request):
        return render(request, 'simpletool/main_page.html', {'request': request})


@login_required(login_url='error')
@require_http_methods(['GET'])
def another_page(request):

    lti_launch = request.session.get('LTI_LAUNCH', None)
    return render(request, 'simpletool/another_page.html', {'lti_launch': lti_launch})


@require_http_methods(['GET'])
def tool_config(request):
    if request.is_secure():
        host = 'https://' + request.get_host()
    else:
        host = 'http://' + request.get_host()

    url = host + reverse('st:lti_launch')

    lti_tool_config = ToolConfig(
        title='LTI Sandbox Simple Tool',
        launch_url=url,
        secure_launch_url=url,
    )
    # this is how to tell Canvas that this tool provides a course navigation link:
    course_nav_params = {
        'enabled': 'true',
        'default': 'enabled',
        'visibility': 'members',  # all enrollees can see it; other values: public, admins
        # optionally, supply a different URL for the link:
        # 'url': 'http://library.harvard.edu',
        'text': 'Simple Tool',
    }
    lti_tool_config.set_ext_param('canvas.instructure.com', 'course_navigation', course_nav_params)

    lti_tool_config.description = 'This is a simple LTI tool.'

    resp = HttpResponse(lti_tool_config.to_xml(), content_type='text/xml', status=200)
    return resp
