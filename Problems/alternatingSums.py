def alternatingSums(a):
    # teamOne = [n for i, n in enumerate(a) if i % 2 == 0]
    # teamTwo = [n for i, n in enumerate(a) if i % 2 == 1]
    # return (sum(teamOne), sum(teamTwo))
    return (sum(a[::2]), sum(a[1::2]))
