from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # TODO - you fill in here.

    nums = {i:True for i in range(2,n+1)}
    primes = []

    while nums:
        prime = nums.pop()
        primes.append(prime)
        i = 2
        while prime*i <= n:
            if prime*i in nums:
                nums.remove(prime*i)
            i += 1

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
