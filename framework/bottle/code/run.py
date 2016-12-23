from app import app
#from bottle import run

if __name__ == '__main__':
    app.run(host='localhost', port=8080, reloader=True)
