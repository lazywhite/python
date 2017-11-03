## Introduction
support for multiple virtualenv for same python version, a wrapper for virtualenv

## Installation
```
pip install virtualwrapper
mkdir ~/.virtualenvs
cat >> .zshrc<<EOF
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
EOF


lsvirtualenv
allvirtualenv

mkvirtualenv test
workon test
deactive

rmvirtualenv

cpvirtualenv <origin> <new>
<env> cdvirtualenv  cd ~/.virtualenvs/env
```

## Automaticlly activate venv

```
# ~/.zshrc

_virtualenv_auto_activate() {
    PWD=`pwd`
    if [ "$PWD" != "$MYOLDPWD" ]; then
        MYOLDPWD="$PWD"
        test -e '.venv' && workon `cat .venv`
    fi
}

precmd_functions+=(_virtualenv_auto_activate)

```

## 将virtualenv打包
```
(env)cdvirtualenv
virtualenv --relocatable .
env目录可直接拷贝使用
```

