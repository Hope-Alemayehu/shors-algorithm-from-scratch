# shors-algorithm-from-scratch

An in-depth implementation of Shor's Algorithm from scratch, simulating quantum operations without relying on external libraries. Designed to explore the mechanics of quantum factorization step by step

The core steps of Shors algorithm:

1. Classical Preprocessing

- chosing a random number a 1 < a <N. N is the number we want to factor
- check if the gcd(a,N) > 1......if yes we found the factor so it terminiates early

2. Quantum Period Finding

- this is the heart of the quantum part and what makes shors algoritsm exponetially faster than the classical method

3. Classical Postprocessing
