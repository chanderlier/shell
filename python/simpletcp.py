from socket import socket


def main():
    client = socket()
    client.connect(('192.168.1.6', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == "__main__":
    main()
