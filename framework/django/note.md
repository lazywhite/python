## 一、Template
```
Using the template system in Python is a three-step process:

1. You configure an Engine.
2. You compile template code into a Template.
3. You render the template with a Context.
```
## 二、Model
### 2.2 Model Meta
```
class Meta:
    abstract = True # define as "abstract base class"
    app_label = 'myapp' # declare which app it belong to
    db_table = 'music_album' # define table name, use lowercase name for MySQL, 
                            # for Oracle, django will shorten table name and turn 
                            # them uppercase, use quoted name to prevent this 
                            # like db_table = '"name_left_in_lower"'
    db_tablespace  # used when backend database support tablespace
    default_manager_name
    default_related_name
    get_latest_by = 'order_data' # default field to use in latest() and earliest() methods
    managed = True   # whether django will be in charge of the lifecycle of this Models
    proxy = True  # use in "proxy model"
    verbose_name = u'中文'   # human readable name
    verbose_name_plural = 'stories' #复数名称
```
### 2.3 Model Manager
## 三、URL dispatch
1. To capture a value from the URL, just put parenthesis around it.  
2. There’s no need to add a leading slash, because every URL has that. For example, it’s ^articles, not ^/articles.  
3. The 'r' in front of each regular expression string is optional but recommended. It tells Python that a string is “raw” – that nothing in the string should be escaped. See Dive Into Python’s explanation.  
4. named regular-expression groups is (?P<name>pattern)  

## 四、Localization
###4.1 install gettext tool
```
brew install gettext
brew link --force gettext
rehash # makemessage will find "msguniq" command
```
### 4.2 get browser language
```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # other middleware ...
)

browser_locale = request.LANGUAGE_CODE
```
###4.2 usage
```
1. use translation in template file
from django.template import Context
locale = request.LANGUAGE_CODE 
context = Context({'LANGUAGE_CODE':locale})
return render_to_response('local/index.html', context=context )

{% load i18n %}
{% trans "Welcome" %}
2. use translation in python file
from django.utils.translation import ugettext as _, activate
activate(browser_locale)
return HttpResponse(_("Welcome"))

3. mkdir polls/locale
4. django-admin makemessages -l zh -e html 
        -l: locale name
        -e: extension name, default is 'html' 'txt', could be 'xml'
        # run this command in "project root" or "app dir", 
5. django-admin compilemessages

```
### 4.3 settings.py
```
LOCALE_PATHS :a list of directories where django look for translation files
USE_I18N = True # 开启国际化支持
LANGUAGE_CODE = 'en' # global locale setting

USE_L10N = False # whether localized formatting of data should be enabled
```

## 五、Topic
### 1. migrations
```
python manage.py makemigrations polls # create migration files with ID
./manage.py sqlmigrate polls 0001
./manage.py migrate # actually do the migration

mysql> drop table snippets;
mysql> delete from django_migrations where app='snippets';
bash> rm -rf snippets/migrations
```
### 2. django ipython shell
```
pip install django-extensions
INSTALLED_APPS.append('django_extensions')
python manage.py shell_plus [ --<type> ] (bython > ipython > pure)

mysite/settings.py
    SHELL_PLUS_PRE_IMPORTS = (
            ('polls.models', '*'),
            ('django.utils', 'timezone'),
            )

    SHELL_PLUS_DONT_LOAD = ['<app_name>', '<app_name>']

```
### 7. django cache
```
type
    memcached
    redis
    database cache table
    filesystem cache
    local memory cache
    dummy cache
```
### 8. manage.py and django-admin
```
python manage.py startproject <pro_name>
python manage.py startapp <app_name>
python manage.py runserver [<ip>:<poort>]

"django-admin" is a command line tool,  "manage.py" does the same thing as "django-admin"
but take care of a few things for you
1. put your project's package on sys.path
2. sets the "DJANGO_SETTINGS_MODULE" environment variable pointing to "settings.py"

``

### 9. ManyToMany field all objects
```
a.mtm.all()
```
### 10. template filter and tag
```
filter: {{ var|length }}
tag: {% if %}  
```
### 11. django-apps
[django-bootstrap3](https://github.com/dyve/django-bootstrap3)
[django-rest-jwt]( http://getblimp.github.io/django-rest-framework-jwt/)

### 12. ORM CRUD
```
obj = Table(arg1=arg1, arg2=arg2); obj.save()
obj.delete()

Table.objects.get(pk=1)
Table.objects.filter
Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
```
### 13. QuerySet API
```
return QuerySets
    filter()
    exclude()
    annotate()
    order_by()
    reverse()
    distinct()
    values()
    values_list()
    dates()
    datetimes()
    none()
    all()
    select_related()
    prefetch_related()
    extra()
    defer()
    only()
    using()
    select_for_update()
    raw()
do not return QuerySets
    get()
    create()
    get_or_create()
    update_or_create()
    bulk_create()
    count()
    in_bulk()
    iterator()
    latest()
    earliest()
    first()
    last()
    aggregate()
    exists()
    update()
    delet()
    as_manager()
filed lookup
    exact
    iexact
    contains
    icontains
    in
    gt
    gte
    lt
    lte
    startswith
    istartswith
    endswith
    iendswith
    range
    date
    year
    month
    day
    week_day
    hour
    minute
    second
    isnull
    search
    regex
    iregex
aggregation function
    expression
    output_field
    **extra
    Avg
    Count
    Max
    Min
    StdDev
    Sum
    Variance
Query Related tools
    Q()
    Prefetch()
    prefetch_related_objects()


result = table.objects.filter(string__contains='pattern')  # like 
result = table.objects.filter(name='pattern')  # '=' 
```

### 14. cookie and session
```
response.set_cookie('username', "bob")
request.COOKIE.get('username')

request.session['username'] = 'bob'

```
#### 14.1 Redis Session
```
pip install django-redis-sessions

mysite/setting.py
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_HOST = 'localhost'
    SESSION_REDIS_PORT = 6379
    SESSION_REDIS_DB = 0
    SESSION_REDIS_PASSWORD = ''
    SESSION_REDIS_PREFIX = 'session'
    SESSION_REDIS_SOCKET_TIMEOUT = 1

```
### 15. change user password
```
from django.contrib.auth.models import User
usr = User.objects.get(username='your username')
usr.set_password('raw password')
usr.save()
```

### 16. customized template filter
```
after adding templatetags, need to restart server
```
### 17. django field 
#### 17.1 Field Type
```
AutoField
BigAutoField
BigIntegerField
BinaryField
BooleanField
CharField
CommanSeperatedField
DateField
DatetimeField
DecimalField
DurationField
EmailField
FileField
FilePathField
FloatField
ImageField
IntegerField
GenericIPAddressField
PositiveIntegerField
PositiveSmallIntegerField
SlugField
SmallIntegerField
TextField
TimeField
URLField
UUIDField
```
#### 17.2 Field Option
```
null
blank
choices
db_column # name of database column
db_index # whether create database index for this column
default # could be a callable object
editable # used for admin site
error_message # override the default message when error occured
help_text # used for form widget
primary_key
unique
unique_for_date
unique_for_year
unique_for_month
verbose_name 
validators # a list of validators run for this field
```
#### 17.3 Relationship fields
```
ForeignKey (many to one)
    on_delete
    limit_choices_to
    related_name
    related_query_name
    to_field
    db_constraint
    swappable

ManyToManyField
OneToOneField
```
### 18. display sql query
```
from django.db import connection
print connection.queries

all = MyModel.objects.filter(name="my name")
print all.query
```
### 19. django-bootstrap3
```
pip install django-bootstrap3

INSTALLED_APPS
    bootstrap3

```
### 19. Response 
```
render(request, 'template', context=locals())
render_to_response will be depracated
return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
```
### 20 Template Comment
```
{% comment %} {% endcomment %}
{# oneline comment $}
```

## 六、 Tips
```
ForeignKey.related_name: The name to use for the relation from the related object back to this one
If you’d prefer Django not to create a backwards relation, set related_name to '+' or end it with '+'

If you need to create a relationship on a model that has not yet been defined, you can use the name of the model, rather than the model object itself:

To create a recursive relationship – an object that has a many-to-one relationship with itself – use models.ForeignKey('self', on_delete=models.CASCADE).
```

