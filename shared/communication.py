import socket
import pickle
import time

def ensure_reciever_is_ready(seconds=1):
    time.sleep(seconds)

def send_data(what_is_sent, who_recives, port=61000):
    ensure_reciever_is_ready()
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


from shared.quantum import QuantumCircuit, Statevector

def send_qubits(circuit_array, who_recives, port=None):
    if port is not None: send_data([Statevector(qc).data for qc in circuit_array], who_recives, port)
    else:                send_data([Statevector(qc).data for qc in circuit_array], who_recives)

def recieve_qubits(who_recives, port=None):
    if port is not None: state_vectors = receive_data(who_recives, port)
    else:                state_vectors = receive_data(who_recives)
    qc_array = [QuantumCircuit(1, 1) for _ in range(len(state_vectors))]
    for qc, sv in zip(qc_array, state_vectors):
        qc.initialize(sv, 0)
    return qc_array
