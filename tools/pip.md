# upgrade pip
pip install -U pip setuptools

# output installed packages in requirements format
pip freeze > requirements.txt 

## cache requirements in local and install from local
alias pipcache='pip install --download ${HOME}/.pip-packages'
alias pipinstall='pip install --no-index --find-links=file://${HOME}/.pip-packages/'

pipcache Django==1.5 # Put Django-1.5.tar.gz in ~/.pip-packages
pipinstall Django==1.5 # Install ~/.pip-packages/Django-1.5.tar.gz
 
pipcache -r requirements.txt # Cache all the requirements of a project
pipinstall -r requirements.txt # Install all requirements from the cache

## virtualenv
virtualenv --always-copy --relocatable

## ~/.pip/pip.conf
```
[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
```
