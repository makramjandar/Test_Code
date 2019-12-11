#!/usr/local/bin/python
# Code Fights Weak Numbers Problem


x = 10 if a > b else 11


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    yield n if n > 1
        

     for i*i in range (2,n+1)
        if n % i == 0:
        
         
gen_exp = (x ** 2 while i * i <= n if n % i == 0 else i += 1 )


list({(yield i) for i in range(3)})





def weakNumbers(n):
    def get_divisors(n):
        divs = []
        for i in range(1, n + 1):
            count = 0
            for d in range(1, i + 1):
                if i % d == 0:
                    count += 1
            divs.append(count)
        return divs

    divs = get_divisors(n)
    weaks = [sum([1 for item in divs[:i + 1] if item > div]) for i, div
             in enumerate(divs)]
    return [max(weaks), weaks.count(max(weaks))]


def main():
    tests = [
        [9, [2, 2]],
        [1, [0, 1]],
        [2, [0, 2]],
        [7, [2, 1]],
        [500, [403, 1]],
        [4, [0, 4]]
    ]

    for t in tests:
        res = weakNumbers(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: weakNumbers({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: weakNumbers({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
