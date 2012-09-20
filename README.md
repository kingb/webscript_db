webscript_db
============

A web-interface and database backend for 'webscript'.

Quick Setup
-----------------

Django 1.3.3: pip install django==1.3.3
Tastypie: pip install django-tastypie

Add this directory to the PYTHONPATH so django can find the
webscript_backend django app.

  cd webscriptdb/
  python manage.py syncdb    # First time only to create DB
  python manage.py runserver 
