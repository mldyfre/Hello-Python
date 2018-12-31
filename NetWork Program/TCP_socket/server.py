# 1.创建socket套接字
# 2.绑定IP和端口
# 3.进行监听
# 4.接收、发送数据
import socket

def main(target, port):
    # 1.创建socket套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定IP和端口
    server.bind((target, port))

    # 3.进行监听
    server.listen(10)
    print("[*] Listening on %s:%d" % (target, port))

    # 4.接受、发送数据
    while True:
        client, addr = server.accept()

        print("[*] Accept from %s:%d" % (addr[0], addr[1]))
        response = client.recv(1024) 
        # 为什么不用管server。
        # 原因当服务端建立监听后，可能有很多客户端来进行连接。如果用一个server不能代表很多个客户端，用client代表每一个客户端连接过来的套接字。
        print(response)
        client.send(b"[*] successful to connection...")
        client.close()

if __name__ == "__main__":
    target = '0.0.0.0'
    port = 4444
    main(target, port)