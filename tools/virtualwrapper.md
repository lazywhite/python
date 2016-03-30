## Installation
```
pip install virtualwrapper
mkdir ~/.virtualenvs
cat >> .zshrc<<EOF
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
EOF


lsvirtualenv

mkvirtualenv test
workon test

deactive

rmvirtualenv
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
