LTI Sandbox
=======================

This is a sample project that can be used to experiment with building LTI tools.

After you've cloned the repository locally, these are the steps to get up and running:

### Create a python virtualenv:

```
mkvirtualenv <your env name>
```

### Install and customize the postactivate and postdeactivate scripts:

These two scripts set and unset certain environment variables for things like database passwords, API keys, etc upon activation or deactivation of the virtualenv.

```
cp virtualenv_config/post* $VIRTUAL_ENV/bin
```

Edit $VIRTUAL_ENV/bin/postactivate to set the environment variable values as appropriate.  

### Install the python package dependencies for this project:

```
pip install -r lti_sandbox/requirements/local.txt
```

### Run the server:

```
python manage.py runserver 0.0.0.0 
```

