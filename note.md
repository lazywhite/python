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

