import socket
import pickle

def send_data(what_is_sent, who_recives, port=61000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((who_recives, port))
        data_to_send = pickle.dumps(what_is_sent)
        s.sendall(data_to_send)

def receive_data(who_recives, port=61000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((who_recives, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk: break
                data += chunk
            return pickle.loads(data)
