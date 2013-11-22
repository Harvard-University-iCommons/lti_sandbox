#!/bin/bash
export HOME=/home/vagrant
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a /home/vagrant/lti_sandbox -r /home/vagrant/lti_sandbox/lti_sandbox/requirements/local.txt lti_sandbox 