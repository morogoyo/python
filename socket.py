import socket

def resolve(host):
    return socket.gethostbyaddr(host)


# resolve('tunerhonda.com')


socket.gethostbyname("tunerhonda.com")


print('test')