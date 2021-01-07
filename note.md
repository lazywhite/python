## 1. install pycrypto-2.6.1 on Mac 10.12
```
configure: error: C preprocessor "clang++" fails sanity check

方法： **sudo** pip install pycrypto
```
## 2. CentOS-7 更新pip
```
yum remove python-setuptools python-pip
python get-pip.py

```

## 3. requirements.txt
```
pyramid>=1.4,<1.5
```
## 4. http server
```
python -m SimpleHTTPServer 0.0.0.0:8000
python -m http.server --bind 0.0.0.0 8000

```


## docstring
```
# google风格
def func(arg1, arg2):
    '''主要用途说明

    详细说明

    Params:
        arg1 (str): 说明
        arg2 (str): 说明
    Returns:
        a dict
        example:
        {"foo": 100, "bar": 200}
    Raises:
        IOError: 

# reST风格, pycharm默认, 支持sphinx
def func(arg1: str, arg2: str) -> dict:
    '''
    this is a reST style

    :param arg1: description
    :param arg2: description
    :returns: result store in dict
    :raises IOError: io exception
    '''
    pass

        
class MyClass:
    '''主要说明
    
    详细说明

    Attibutes:
        foo (str): 说明
        bar (str): 说明
    '''
    def __init__(self, foo, bar):
        pass
```
