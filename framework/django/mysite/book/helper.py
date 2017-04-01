def handle_uploaded_file(f):
    with open('/srv/salt/files/scripts/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
