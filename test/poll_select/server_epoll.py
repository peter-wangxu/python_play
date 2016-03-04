#!ur/bin/env python

import socket, select
import Queue


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 10000)
serversocket.bind(server_address)
serversocket.listen(1)
serversocket.setblocking(0)

timeout = 20
epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

message_queues = {}
fd_to_socket = {serversocket.fileno(): serversocket}
while True:
    print "waiting connections..."
    events = epoll.poll(timeout)
    if not events:
        print 'epoll timeout, '
        continue
    print 'there are ', len(events), ' events, begin to process.'
    for fd, event in events:
        socket = fd_to_socket[fd]
        if event & select.EPOLLIN:
            if socket == serversocket:
                connection ,address = serversocket.accept()
                print "new connection:", address
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                fd_to_socket[connection.fileno()] = connection
                message_queues[connection] = Queue.Queue()
            else:
                data = socket.recv(1024)
                if data:
                    print "Received:", data, "Client:", socket.getpeername()
                    message_queues[socket].put(data)
                    epoll.modify(fd, select.EPOLLOUT)
        elif event & select.EPOLLOUT:
            try:
                msg = message_queues[socket].get_nowait()
            except Queue.Empty:
                print socket.getpeername(), 'Queue empty'
                epoll.modify(fd, select.EPOLLIN)
            else:
                print "Send :", data, "Client:", socket.getpeername()
                socket.send(msg)
        elif event & select.EPOLLHUP:
            epoll.unregister(fd)
            fd_to_socket[fd].close()
            del fd_to_socket[fd]
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
