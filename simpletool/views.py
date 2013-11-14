from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from ims_lti_py.tool_provider import DjangoToolProvider

from time import time
import logging

logger = logging.getLogger(__name__)


# Create your views here.

@require_http_methods(['GET'])
def index(request):
    logger.info("request to index.")
    return render(request, 'simpletool/index.html')


@require_http_methods(['GET','POST'])
def lti_tool(request):

    if request.user.is_authenticated:
        return render(request, 'simpletool/lti_tool.html', {'request': request})

    else: 
        return render(request, 'simpletool/error.html', {'message': 'Error: user is not authenticated!'})

def another_page(request):
    return render(request, 'simpletool/another_page.html')

    
'''
@require_http_methods(['GET'])
def tool_config(request):
    host = request.scheme + '://' + request.host
    secure_host = 'https://' + request.host
    url = host + '/lti_tool'
    secure_url = secure_host + '/lti_tool'
    lti_tool_config = ToolConfig(
        title='Example Django Tool Provider',
        launch_url=url,
        secure_launch_url=secure_url)
    lti_tool_config.description = 'This example LTI Tool Provider supports LIS Outcome pass-back'
    resp = response(lti_tool_config.to_xml(), 200)
    resp.headers['Content-Type'] = 'text/xml' 
    return resp
'''





