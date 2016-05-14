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


<img src="{% static 'my_app/myexample.jpg' %}" alt="My image"/>

django-admin.py makemessages -l zh
django-admin.py compilemessages

{% load i18n %}
{% trans "This is the title." %}



## URL dispatch
1. To capture a value from the URL, just put parenthesis around it.  
2. There’s no need to add a leading slash, because every URL has that. For example, it’s ^articles, not ^/articles.  
3. The 'r' in front of each regular expression string is optional but recommended. It tells Python that a string is “raw” – that nothing in the string should be escaped. See Dive Into Python’s explanation.  
4. named regular-expression groups is (?P<name>pattern)  


If there are any named arguments, it will use those, ignoring non-named arguments.
Otherwise, it will pass all non-named arguments as positional arguments.


The django.conf.urls.url() function can take an optional third argument which should be a dictionary of extra keyword arguments to pass to the view function.
url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),


Each captured argument is sent to the view as a plain Python string, regardless of what sort of match the regular expression make


we can specify default parameters for your views’ arguments. 


## Model
ForeignKey.related_name: The name to use for the relation from the related object back to this one
If you’d prefer Django not to create a backwards relation, set related_name to '+' or end it with '+'

If you need to create a relationship on a model that has not yet been defined, you can use the name of the model, rather than the model object itself:

To create a recursive relationship – an object that has a many-to-one relationship with itself – use models.ForeignKey('self', on_delete=models.CASCADE).

## Topic
No migrations to apply 
drop table snippets;
delete from django_migrations where app='snippets';

