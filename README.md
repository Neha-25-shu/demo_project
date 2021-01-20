# Welcome to Blog Website
[![](https://img.shields.io/pypi/pyversions/Django.svg)](https://python.org/downloads/)
[![](https://img.shields.io/badge/django-2.0%20%7C%202.1%20%7C%202.2-success.svg)](https://djangoproject.com/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://choosealicense.com/licenses/mit/)

Blog with Django web framework. 


Django packages provides a set of module  for user Registration Authentication and Authorization 

# Documentation
  -------------
  http://django-rest-auth.readthedocs.org/en/latest/
  
  -------------
  https://docs.djangoproject.com/en/3.1/


# Technology Stack We have used

1. Python 3.6
2. Django 3.1.2
3. Django REST Framework
4. sqlite3 Database
5. Google Chrome v.83.0.4103.61    
6. Google Chrome driver v.83.0.4103.61
7. Css
8. Html
9. Bootstrap


# Project Structure:

    .
    ├── blog
    ├── API.md : API documentation
    ├── README.md : documentation file
    │   ├── __init__.py
    │   ├── settings.py : settings file for the project.
    │   ├── urls.py : base urls for apps of the projects
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    ├── marketing
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations : database migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   ├── models.py : database models for app
    │   ├── tests.py : test cases for view
    │   └── views.py : These views are called by url name
    ├── media
    ├── posts
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── requirements.txt : requirements needs to be install
    ├── static_in_env
    │   ├── css
    │   ├── fonts
    │   ├── icons-reference
    │   ├── img
    │   ├── js
    │   └── vendor
    └── templates
        ├── base.html
        ├── blog.html
        ├── contact.html
        ├── footer.html
        ├── header.html
        ├── head.html
        ├── index.html
        ├── post_confirm_delete.html
        ├── post_create.html
        ├── post.html
        ├── scripts.html
        ├── search_results.html
        └── sidebar.html
        

# Features:
  ---------
  * User registration

  * User email verification

  * Change password - with password reset email.
  
  * Users profile
  
  * Create, Update, Edit & Delete Posts
  
  * Comments
  
  * Search , pagination
  
  
  

## APIs Details

   See documentation [here.](./API.md)
  
  
## Run the project Locally ##

i. Clone the repository.

ii. Go to directory of manage.py and install the requirements.

	pip install -r requirements.txt
	
**Note:**
You may configure the virtual environment if required.

For instructions, click here : https://virtualenv.pypa.io/en/latest/installation/
    


**Note:**
By default, dbSqlite3 database is used. You may also use different database in local_settings file if required.

iii. Run migrations

	    python manage.py migrate

iv. Ready to run the server.

	  python manage.py runserver


# Linting:

	make lint


# Testing:

	python manage.py test
