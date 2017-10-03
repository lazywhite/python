## 一、Template
```
Using the template system in Python is a three-step process:

1. You configure an Engine.
2. You compile template code into a Template.
3. You render the template with a Context.
```
## 二、Model
### 2.1 Model Meta
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
### 2.2 Model conclusion
```
每个model映射到数据库的一张表
每个model自动包含一个主键字段 id = models.AutoField(primary_key=True), 除非其他的字段属性中包含primary_key
让django管理model, 需要将app配置在INSTALLED_APPS中

```
### 2.3 Model 继承
前提: 父类必须继承django.db.models.Model  
一. 抽象父类, 不创建任何table, 只是用来定义子类的公共属性   

  
```
    class Meta:
        abstract = True
```
  
二. 继承类  
  
```
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

两个model均会产生真实的表, Restaurant表会包含name, address两个OneToOneField字段
```
   
三. 代理类   

```
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class NewManager(models.Manager):
    pass

class MyPerson(Person):
    objects = NewManager() ## 替换默认的model manager
    class Meta:
        proxy = True

    def do_something(self):
        pass
```

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
### 4.3 usage
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
### 4.4 settings.py
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

```

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

### 12. QuerySet API
```
return QuerySets
    filter(): 返回对象QuerySet
        Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
    exclude()
        users = User.objects.exclude(body_text__icontains="food")
    annotate()
        q = Blog.objects.annotate(Count('entry'))
    order_by()
        Entry.objects.order_by('headline')
    reverse()
        Entry.objects.order_by('headline').reverse()
    distinct()
        Permission.objects.values("content_type_id").distinct() 
    values(): 返回字典QuerySet
    values_list(): 返回tuple QuerySet
    dates()
        User.objects.dates("date_joined", "day")
    datetimes()
    none(): 返回一个空的QuerySet对象
    all()
        
    select_related()
        select_related主要针一对一和多对一关系进行优化。
        User.objects.select_related().all()
    prefetch_related()
        对于多对多字段（ManyToManyField）和一对多字段进行优化
    extra(): 子查询
        Entry.objects.extra(where=['headline=%s'], params=['Lennon'])
        Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
        Entry.objects.extra(select={'new_id': "select id from tb where id > %s"}, select_params=(1,), order_by=['-nid'])

        Blog.objects.extra(
        select={
            'entry_count': 'SELECT COUNT(*) FROM blog_entry WHERE blog_entry.blog_id = blog_blog.id'
        },)
    defer()
        Entry.objects.defer("headline", "body")
        Entry.objects.defer("body").filter(rating=5).defer("headline")

        You can defer loading of fields in related models
        Blog.objects.select_related().defer("entry__headline", "entry__body")

    only()
        Users.objects.only("username") 返回的QuerySet中每个user对象仅有username属性
    using()
        Entry.objects.using('backup')
    select_for_update() # 加行锁
        entries = Entry.objects.select_for_update().filter(author=request.user)
    raw()
        for user in User.objects.raw("select * from auth_user"):
            print user.username
    date
         Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1)) 
         Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))        
    year
         Entry.objects.filter(pub_date__year=2005) 
         Entry.objects.filter(pub_date__year__gte=2005)
    month
           Entry.objects.filter(pub_date__month=12) 
           Entry.objects.filter(pub_date__month__gte=6)
    day
         Entry.objects.filter(pub_date__day=3) 
         Entry.objects.filter(pub_date__day__gte=3)
    week
         Entry.objects.filter(pub_date__week=52) 
         Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)
    time
         Entry.objects.filter(pub_date__time=datetime.time(14, 30))

    limit
        Entry.objects.all()[5:10]
        不支持负数下标

do not return QuerySets
    get()
        group = Group.objects.get(pk=2)
        group = Group.objects.get(name="admin")
    create()
        p = Person.objects.create(first_name="Bruce", last_name="Springsteen")

        p = Person(first_name="Bruce", last_name="Springsteen")
        p.save(force_insert=True)
    get_or_create()
    update_or_create()
    bulk_create()
        Entry.objects.bulk_create([
            Entry(headline='This is a test'),
            Entry(headline='This is only a test'),
        ])
    count()
        Entry.objects.filter(headline__contains='Lennon').count()
    in_bulk()
    iterator()
    latest()
        Entry.objects.latest('pub_date')
    earliest()
        Entry.objects.earliest('pub_date')
    first()
        p = Article.objects.order_by('title', 'pub_date').first()
    last()
        p = Article.objects.order_by('title', 'pub_date').last()
    aggregate()
    exists()
        entry = Entry.objects.get(pk=123)
        if some_queryset.filter(pk=entry.pk).exists():
            print("Entry contained in queryset")
    update(): 返回受影响的行数
        Entry.objects.filter(pub_date__year=2010).update(comments_on=False, headline='This is old')
    delete()
        Entry.objects.filter(blog=b).delete()
    as_manager()

Field  Lookups
    in
        Entry.objects.filter(id__in=[1, 3, 4])

        inner_qs = Blog.objects.filter(name__contains='Cheddar') 
        entries = Entry.objects.filter(blog__in=inner_qs)

    gt; gte
        Entry.objects.filter(id__gt=4)
        Entry.objects.filter(id__gte=4)

    startswith; istartswith
    endswith; iendswith

    exact; iexact
        Entry.objects.get(id__exact=14)
        Entry.objects.get(id__exact=None)
    contains; icontains
    range
        start_date = datetime.date(2005, 1, 1)
        end_date = datetime.date(2005, 3, 31) 
        Entry.objects.filter(pub_date__range=(start_date, end_date))

    isnull
        Entry.objects.filter(pub_date__isnull=True)
        
    search(只能用在有全文索引的地方)
        Entry.objects.filter(headline__search="+Django -jazz Python")

    regex; iregex
        Entry.objects.get(title__regex=r'^(An?|The) +')


aggregation function
    avg
        User.objects.aggregate(Avg('id'))
    min
        User.objects.aggregate(Min('id'))
    max
        User.objects.aggregate(Max('id'))
    count
        User.objects.count()
    sum
        ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
        ModelName.objects.aggregate(Sum('field_name'))

Query Related tools
    Q()
        Q()对象就是为了便于处理复杂的过滤条件
        使用符号&或者|将多个Q()对象组合起来传递给filter()，exclude()，get()等函数。当多个Q()对象组合起来时，Django会自动生成一个新的Q()。
        逗号之间的Q是and关系, '|' 或, '~' 取反
        Q()对象可以结合关键字参数一起传递给查询函数，不过需要注意的是要将Q()对象放在关键字参数的前面
        News.objects.get(
            Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
            question__startswith='Who')
    Prefetch()
    prefetch_related_objects()


直接执行SQL语句
    User.objects.raw() || Manager.raw()
        name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
        Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)
    django.db.connection + django.db.transaction

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
AutoField: 自增的IntegerField
BigAutoField: 自增的BigIntegerField
BigIntegerField
BinaryField: 存储raw binary数值的字段, 只接受bytes
BooleanField: bool字段, 只能存储True/False, 默认值是None, 如果希望可以存储null值, 使用NullBooleanField
CharField: 字符串字段, max_length设置最大长度
DateField: 对应datetime.date, 以下属性只能三选一, 不能同时使用
    auto_now = False # 每当object被save()时, 自动设置为当前时间
    auto_now_add = False # 记录object被创建的时间
    default 默认值 
DateTimeField: 对应datetime.datetime
DecimalField: 对应Decimal
    max_digits = 5
    decimal_places = 2
DurationField: 对应timedelta 存储微秒为单位的bigint
EmailField: 一个开启了email验证的CharField
FileField: 
    upload_to='uploads/%Y/%m/%d/'
    storage
FilePathField
FloatField: 对应float类型
ImageField: 添加了image验证的FileFiled, 底层是varchar类型, 默认max_length=100
    height_field
    width_field
IntegerField: int字
GenericIPAddressField: 按照字符串来存取
    protocol=("both"|"IPv4"|"IPv6")
    unpack_ipv4=(True|False)
PositiveIntegerField: unsigned int
PositiveSmallIntegerField: unsigned small int
SlugField: 只能存储包含数字, 字母, 下划线, 连接符的varchar, max_length默认50
SmallIntegerField: small int
TextField: 对应mysql text类型字段, 接受<textarea>提交的值
TimeField: 对应datetime.time
URLField: 存储url的CharField, max_length默认为200
UUIDField:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```
#### 17.2 Field Option
```
null: 数据库字段值允许为null
blank: form表单验证中, 允许空值
choices: 
    class Person(models.Model):
        SHIRT_SIZES = (
            ('S', 'Small'),  #<option value="S">Small</option>
            ('M', 'Medium'),
            ('L', 'Large'),
        )
        name = models.CharField(max_length=60)
        shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

db_column # 对应表的字段名, 如果不设置, 使用field name
db_index=<Bool> # 是否在当前字段建立索引
default # 字段默认值, 可以是callabled的
editable # 默认为True, 如果为False, 则admin, ModelForm均不会编辑此字段, 并且跳过表单验证
error_message # 设置自定义出错信息
help_text # form widget中的字段帮助信息
primary_key # 标示当前字段为table主键, 只读, 如果修改一个存在的object的主键值, 会产生一个新的object, 老的object仍然保留
unique # 字段值唯一

unique_for_date
    title = models.CharField(unique_for_date="pub_date") # 不允许出现title和pub_date字段值重复的行
    pub_date = models.DateField() 
    #pub_date = models.DateTimeField() # 只会检测date部分
unique_for_year
unique_for_month

validators(list) 

Verbose Field Names
    ForeignKey, ManyToManyField, OneToOneField, 通过verbose_name属性设置
        sites = models.ManyToManyField(Site, verbose_name="list of sites")
    普通字段, 通过第一个optional parameter设置
        first_name = models.CharField("person's first name", max_length=30)
        first_name = models.CharField(max_length=30)  # verbose_name会是first name, 将下划线转化为空格
```
#### 17.3 Relationship fields
```
ForeignKey
    特性
        recursive: 外键为自己
            models.ForeignKey('self', on_delete=models.CASCADE).
        lazy: 关联属性都是延迟加载的

    on_delete
        models.CASCADE: 跟随一起删除
        PROTECT: 禁止删除
        SET_NULL  当参考的行被删除, 设为null
        SET_DEFAULT 要求必须设置default属性
        SET(callable|value) 设置为callable返回的值
    limit_choices_to: 用在ModelForm解析中, 设置过滤条件
        limit_choices_to={'is_staff': True}, 


        def limit_pub_date_choices():
            return {'pub_date__lte': datetime.date.utcnow()}
        limit_choices_to = limit_pub_date_choices
    related_name: 反向引用的属性名, 默认为类名全小写
        值为"+", 表明不生成反向引用
    related_query_name
        # Declare the ForeignKey with related_query_name
        class Tag(models.Model):
            article = models.ForeignKey(
                Article,
                on_delete=models.CASCADE,
                related_name="tags",
                related_query_name="tag",
            )
            name = models.CharField(max_length=255)

        # That's now the name of the reverse filter
        Article.objects.filter(tag__name="important")

    to_field="uuid"
        外键参考的表的field, 默认是id, 可以是带有unique=True的其他field
    db_constraint: 数据库是否为外键创建约束, 默认为True
    swappable: 
    db_index: 默认为True, 若为False则只有外键, 不建立索引


ManyToManyField
    自连结
        friends = models.ManyToManyField("self", symmetrical=True)
        symmetrical默认为True, 标明双方访问是对等的
    through
        默认django会自己产生中间表, 用此选项指定想用的中间表
        当希望在映射关系中保存其他的信息时, 使用此方案
    through_fields
        手动指定中间表的哪些field用来做映射
    db_table: 手动指定产生的中间表的名称
    related_name: 默认为{{class|lower}}_set
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
### 20. Request and Response 
```
path variable
/user/{ID}/ : url(r'user/(?P<ID>\d+)/$', views.detail, name="userDetail")
    request param
/user?name='bob'&age=10
    request.GET.get('name')
```

```
render(request, 'template', context=locals())
render_to_response will be depracated
return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
```
### 21 Template Comment
```
{% comment %} {% endcomment %}
{# oneline comment $}
```
### 22 Logging
```
formatter
logger
handler
filter
```        

### 23 SMTP
```
## setting for SMTP
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


from django.core.mail import send_email
send_mail("subject", "body", "sender", ["receiver1", "receiver02"...])
send_mail("test", "test", "cppking@126.com", ["lazywhite@qq.com"])
```

### 24. Database Function
```
django.db.models.functions
    Cast
    Concat
    Greatest
    Least
    Length
    Lower
    Now
    Substr
    Upper

    ExtractYear
    Trunc
```

### 25. Validator
```
callable, 接受一个value作为参数, 抛出ValidationError表明验证失败, 否则正常
Built-in Validators
    RegexValidator
    EmailValidator
    URLValidator
    FileExtensionValidator

```

### 26. 对象级权限控制
```
配置文档 https://github.com/django-guardian/django-guardian

>>> from django.contrib.auth.models import User, Group
>>> jack = User.objects.create_user('jack', 'jack@example.com', 'topsecretagentjack')
>>> ct = ContentType.objects.get(pk=12)
>>> perm = Permission()
>>> perm.codename = "view_book12"
>>> perm.name = "can view book 12"
>>> perm.content_type = ct
>>> perm.save()
>>> book12 = Book.objects.get(pk=12)
>>> jack.has_perm('view_book12', book12)
False
>>> from guardian.models import UserObjectPermission
>>> UserObjectPermission.objects.assign_perm('view_book12', jack, obj=book12)
<UserObjectPermission: admins | jack | change_group>
>>> jack.has_perm('view_book12', book12)
True
>>> jack.has_perm('view_book12')
False
```
## 六、 Tips
```
python -c "import django; print(django.get_version())"

./manage.py createsuperuser --username=joe --email=joe@example.com

middleware 
    request会按照MIDDLEWARE_CLASSES定义的顺序被处理
    response按照相反顺序被处理

redirect("account:profile", permanent=True)
redirect("/user/login/", permanent=True)

DATABASE_ROUTER


## 逆向生成models.py
1. 在setting里面设置你要连接的数据库类型和连接名称，地址之类
2. django-admin.py startapp app
3. python manage.py inspectdb > app/models.py


无主键的model无法进行迭代
ALLOWED_HOSTS = [ * ]

返回301, 可能url路径少了'/'


python manage.py makemigration asset 
python manage.py migrate asset --database zabbix


./manage.py  makemigration <app> #不能添加--database
./manage.py  migrate <app> <0001> --fake --database=xx #跳过某些migration

```


