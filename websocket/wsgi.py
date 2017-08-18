def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/echo':
        ws = environ["wsgi.websocket"]
        message = ws.receive()
        ws.send(message)
