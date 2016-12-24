from bottle import  Bottle, view, template, request, response, redirect
import bottle_mysql as bm
import bottle_session
import bottle_redis
import redis

#import pdb

app = Bottle()

#pdb.set_trace()
#app.config.load_config('config.ini')
#plugin = bm.Plugin(dbhost=app.config['mysql']['dbhost'], dbuser='root', dbpass='root', dbname='test')
sqlplugin = bm.Plugin(dbuser='root', dbpass='root', dbname='test')
app.install(sqlplugin)

session_plugin = bottle_session.SessionPlugin(cookie_lifetime=600)

redis_plugin = bottle_redis.RedisPlugin()
conn_pool = redis.ConnectionPool(host='localhost', port=6379)

session_plugin.connection_pool = conn_pool
redis_plugin.redisdb = conn_pool
app.install(session_plugin)
app.install(redis_plugin)


@app.route('/login', method='POST')
def login(db, session):
    postbody = request.body.read()
    print postbody
    username = request.forms.get("username")
    password = request.forms.get("password")
    db.execute("select password from user where name=%s", (username,))
    row = db.fetchone()
    if row and (password == row.get("password")):
        session['username'] = username
        redirect('/login')
    else:
        return "password not correct"

@app.route('/login', method='GET')
def login(session):
    username = session.get('username')
    if username:
        redirect('/user')
    else:
        return template('login')

@app.route('/logout', method='GET')
def logout(session):
    del(session['username'])
#    return 'logout'
    redirect("/login")


@app.route('/user')
def user(db, session):
    username = session.get('username')
    if not username:
        redirect("/login")
    else:
        return template('user', name=username)

