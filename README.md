# Quantum Cryptographic Primitives

This repository contains implementations of quantum cryptographic primitives over BB84 using Qiskit.  
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

**Once inside the container, to start the communication use:**  
(Make sure to start the Bob container first, since that one is the first to receive data and needs to be listening)
``` bash
run
```
