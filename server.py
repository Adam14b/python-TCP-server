import socket

def start_server():
    HOST = 'localhost'
    PORT = 9090

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Подключение от {client_address}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Получено: {data.decode()}")
                    client_socket.sendall(data)
                    print(f"Отправлено эхо: {data.decode()}")

if __name__ == '__main__':
    start_server()
