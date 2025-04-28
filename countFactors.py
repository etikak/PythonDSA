import math

def count_factors_optimised(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i == N / i:
                count += 1
            else:
                count += 2
    return count



if __name__ == "__main__":
    n = 24
    print(f"count for factors for number {n}: {count_factors_optimised(n)}")
