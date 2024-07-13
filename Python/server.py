import socket
import threading

clients = []

def broadcast(message, conn):
    for client in clients:
        if client != conn:
            try:
                client.sendall(message)
            except Exception as e:
                print(f"Error sending message to client: {e}")
                clients.remove(client)

def handle_client(conn, addr):
    with conn:
        print(f'Connected by {addr}')
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received from {addr}: {data.decode()}')
                broadcast(data, conn)
            except Exception as e:
                print(f"Error handling client {addr}: {e}")
                break
    clients.remove(conn)
    print(f'{addr} disconnected')

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server listening on {host}:{port}')
        while True:
            conn, addr = s.accept()
            clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
