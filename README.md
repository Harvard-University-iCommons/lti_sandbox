LTI Sandbox
=======================

This is a sample project that can be used to experiment with building LTI tools.

After you've cloned the repository locally, these are the steps to get up and running:

### Start the virtual machine with Vagrant:

```
vagrant up
```

Vagrant will create an Ubuntu virtual machine and provision it with everything you will need to run the sandbox application.  This includes creating a new Python virtualenv using the `mkvirtualenv` command, and installing the project's Python dependencies using `pip`.

When the startup process has completed, log in to your new machine:

```
vagrant ssh
```

The Python virtualenv that was created during the provisioning step, `lti_sandbox`, will already be activated, and you'll be moved into the project directory.

### Set up the sqlite database:

```
./manage.py syncdb
```

### Run the server:

```
python manage.py runserver 0.0.0.0:8000 
```

