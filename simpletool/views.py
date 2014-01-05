from django.shortcuts import render
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


@login_required
@require_http_methods(['POST'])
def lti_tool(request):

    if request.user.is_authenticated:
        return render(request, 'simpletool/lti_tool.html', {'request': request})

    else:
        return render(request, 'simpletool/error.html', {'message': 'Error: user is not authenticated!'})


def another_page(request):
    return render(request, 'simpletool/another_page.html')


@require_http_methods(['GET'])
def tool_config(request):
    host = 'http://' + request.get_host()
    secure_host = 'https://' + request.get_host()
    url = host + reverse('st:lti_tool')
    secure_url = secure_host + reverse('st:lti_tool')

    lti_tool_config = ToolConfig(
        title='LTI Sandbox Simple Tool',
        launch_url=url,
        secure_launch_url=secure_url,
    )
    lti_tool_config.description = 'This is a simple LTI tool.'
    resp = HttpResponse(lti_tool_config.to_xml(), content_type='text/xml', status=200)
    return resp
