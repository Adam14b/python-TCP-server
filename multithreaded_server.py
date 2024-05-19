import socket
import threading

def handle_client(client_socket, client_address):
    with client_socket:
        print(f"Подключение от {client_address}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено от {client_address}: {data.decode()}")
            client_socket.sendall(data)
            print(f"Отправлено эхо к {client_address}: {data.decode()}")

def start_server():
    HOST = 'localhost'
    PORT = 9090

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

if __name__ == '__main__':
    start_server()
