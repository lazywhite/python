python manage.py runserver [<ip>:<poort>]
pip install django-extensions
INSTALLED_APPS.append('django_extensions')
python manage.py shell_plus [ --<type> ] (bython > ipython > pure)

mysite/settings.py
    SHELL_PLUS_PRE_IMPORTS = (
            ('polls.models', '*'),
            ('django.utils', 'timezone'),
            )

    SHELL_PLUS_DONT_LOAD = ['<app_name>', '<app_name>']


python manage.py makemigrations <app> # create migration files with ID
./manage.py sqlmigrate <app> <id> 
./manage.py migrate # actually do the migration


./manage.py shell_plus # enter interactive environment


<img src="{% static "my_app/myexample.jpg" %}" alt="My image"/>
