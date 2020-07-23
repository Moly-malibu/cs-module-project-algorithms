'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache={}):
    if n in cache:
        return cache[n]
    if cache is None:
        cache = {}
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        cache[n] = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

#NAIVE

def eating_cookies_naive(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache is not None and cache[n] > 0:
        return cache[n]
    else:
        if cache is None:
            cache = [0 for i in range(n+1)]
        cache[n] = eating_cookies_naive(n-1) + eating_cookies_naive(n-2) + eating_cookies_naive(n-3) 
    return cache[n]
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies_naive(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")