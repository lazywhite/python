## Installation

```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

source ~/.bash_profile

echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

```
## Usage
```
wget http://mirrors.sohu.com/python/2.7.9/Python-2.7.9.tar.xz
mv Python-2.7.9.tar.xz ~/.pyenv/cache/
pip install 2.7.9
pip global 2.7.9
```
