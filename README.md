# Quantum Cryptographic Primitives

This repository contains implementations of quantum cryptographic primitives over BB84 using Qiskit.  
To execute it all you need is to have installed [docker](https://www.docker.com/) on your machine.  
The following primitives are implemented:  
- Bit Commitment
- Coin Flip
- Oblivious Transfer

You can also create your own implementations using the code on the `template` folder.

**To build containers use:**
``` bash
docker-compose up --build -d coin_flip_alice coin_flip_bob
```

**To access a container use:**
``` bash
docker exec -it coin_flip_alice bash
```

**You can stop the containers using:**
``` bash
docker-compose down
```

**Once inside the container, to start the communication use the command `run`**  
(Make sure to start the Bob container first, since that one is the first to receive data and needs to be listening before Alice send the qubits)

**Container names:**
```
bit_commitment_alice
bit_commitment_bob
coin_flip_alice
coin_flip_bob
oblibious_transfer_alice
oblibious_transfer_bob
template_alice
template_bob
```
