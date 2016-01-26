import eventlet


def myhandle(client_sock, client_addr):
    print("client connected", client_addr)

eventlet.serve(eventlet.listen(('127.0.0.1', 9999)), myhandle)