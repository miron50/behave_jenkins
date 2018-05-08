import socket, datetime

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind(('', 2222))
        server_sock.listen(1)

        sock, addr = server_sock.accept()
        data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
        sock.send(data.encode())
        sock.close()