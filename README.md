# Commands

# Start new Project. (sudo apt install python3-django)
* django-admin startproject mysite

# Run Server
* python manage.py runserver [portNumber]
* portNumber is optional. Also, you can pass a range of portnumbers (0:8000).

# Create app
* python manage.py startapp appName

# Create table in database
* python manage.py migrate

# Store changes as a migration
* python manage.py makemigrations appName

# sqlmigrate takes migration names and returns their SQL
* python manage.py sqlmigrate appName 0001

# migrate applies changes to the database
* python manage.py migrate

# Python shell
* python manage.py shell

# Create an admin user
* python manage.py createsuperuser

