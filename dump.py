from socket import socket
from logging import log, ERROR

CHUNK_SIZE = 64 * 1024
DEFAULT_ADDRESS = 'localhost'
DEFAULT_PORT = 4444


def loglevel_decorator(loglevel):
    def wrapper(*args, **kwargs):
        log(loglevel, *args, **kwargs)

    return wrapper

loge = loglevel_decorator(ERROR)

def from_port_to_file(address, port, output_file):
    try:
        sock = socket()
        sock.connect((address, port))

        with open(output_file, "w") as file:
            received_data = sock.recv(CHUNK_SIZE).decode("utf-8")
            while received_data:
                file.write(received_data)
                received_data = sock.recv(CHUNK_SIZE)
    except Exception as err:
        loge(err)


if __name__=='__main__':
    loge('Please use CLI interface, defined in __main__.py')