## 1. install pycrypto-2.6.1 on Mac 10.12
```
configure: error: C preprocessor "clang++" fails sanity check

方法： **sudo** pip install pycrypto
```
## 2. django template unicode decode error
```
manage.py
    reload(sys)
    sys.setdefaultencoding('utf8')

path/to/template.html
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    </head>
views.py
    # -*- coding: utf-8 -*-
```
