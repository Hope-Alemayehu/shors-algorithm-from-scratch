import utils  # Classical helper functions (like GCD, modular exponentiation)
import quantum_sim  # Quantum simulation functions (like QFT, state prep)
import period_finding  # Period finding logic
import random

def main():
    # Step 1: Input the number to factor
    N = int(input("Enter the number to factor (N): "))
    
    # Step 2: Check if N is already a prime or a power of a prime
    if utils.is_prime_or_power(N):
        print(f"{N} is either a prime or a power of a prime. No need for factoring.")
        return

    # Step 3: Choose a random number 'a' such that 1 < a < N
    while True:
        a = random.randint(2, N - 1)
        if utils.gcd(a, N) == 1:  # Ensure gcd(a, N) = 1
            break

    print(f"Random number chosen: a = {a}")

    # Step 4: Simulate the quantum part to find the period 'r'
    r = quantum_sim.find_period(a, N)
    if r is None:
        print("Failed to find a period. Try again with a different random number.")
        return

    print(f"Period found: r = {r}")

    # Step 5: Check if the period is valid
    if r % 2 != 0 or pow(a, r // 2, N) == N - 1:
        print("Period is not valid for factorization. Try again with a different random number.")
        return

    # Step 6: Compute the factors of N
    factor1 = utils.gcd(pow(a, r // 2) - 1, N)
    factor2 = utils.gcd(pow(a, r // 2) + 1, N)

    print(f"Factors of {N}: {factor1} and {factor2}")

if __name__ == "__main__":
    main()
