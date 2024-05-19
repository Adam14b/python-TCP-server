import socket

def start_client():
    HOST = 'localhost'
    PORT = 9090

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        message = input("Введите сообщение: ").encode()
        client_socket.sendall(message)
        data = client_socket.recv(1024)
        print(f"Получено эхо: {data.decode()}")

if __name__ == '__main__':
    start_client()
