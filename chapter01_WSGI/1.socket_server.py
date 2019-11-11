# -*- coding: utf-8 -*-#
"""
Name:         socket_server
Author:       weiheng
Date:         2019/11/5
Description:  简单的Socket服务器
"""

import socket
HOST = "127.0.0.1"
PORT = 8000

html = """
<!DOCTYPE HTML>
<html>
<header>
    <meta charset="utf-8">
    <title>Hello World</title>
</header>
<body>
Hello World
</body>
</html>
"""
response_header = [
    "HTTP/1.1 200 OK",
    "Server: socketServer",
    "Content-Type: text/html",
    'Content-Length: {}\r\n'.format(len(html)),
    html,
]
response = "\r\n".join(response_header)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print("http://{}:{}".format(HOST, PORT))
while 1:
    conn, addr = server.accept()
    conn.send(response.encode("utf-8"))


