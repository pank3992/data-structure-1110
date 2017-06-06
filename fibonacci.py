
def fib(n):
    mem = [1, 1]

    def _fib(m):
        if len(mem) >= m:
            return mem[m - 1]
        else:
            mem.append(_fib(m - 1) + _fib(m - 2))
            return mem[m - 1]

    res = _fib(n)
    return res
