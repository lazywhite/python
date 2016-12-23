from bottle import  Bottle, view, template
import bottle_mysql as bm

#import pdb

app = Bottle()

#pdb.set_trace()
app.config.load_config('config.ini')
#plugin = bm.Plugin(dbhost=app.config['mysql']['dbhost'], dbuser='root', dbpass='root', dbname='test')
plugin = bm.Plugin(dbuser='root', dbpass='root', dbname='test')
app.install(plugin)




@app.route('/user/<uid>')
def user(uid, db):
    db.execute('select name from user where id=%s', (uid,))

    row = db.fetchone()
    if row:
        name = row.get('name')
    else:
        name = 'guest'
    return template('user', name=name)

