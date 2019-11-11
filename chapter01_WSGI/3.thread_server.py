# -*- coding: utf-8 -*-#
"""
Name:         3.thread_server
Author:       weiheng
Date:         2019/11/11
Description:  多线程版web服务器
"""
import socket
from threading import Thread

EOL1 = "\r\n"
EOL2 = "\n\r\n"
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


def handler_connection(conn, address):
    import time
    time.sleep(50)
    print("111111111111")
    conn.send(response.encode("utf-8"))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    print("http://127.0.0.1:8080")
    server.setblocking(0)  # 设置非阻塞

    try:
        while 1:
            try:
                conn, address = server.accept()
            except Exception:
                continue
            t = Thread(target=handler_connection, args=(conn, address))
            t.start()
    except Exception:
        pass




    # thread = Thread(target=handler_connection, args=(conn, address))
    # thread.start()
