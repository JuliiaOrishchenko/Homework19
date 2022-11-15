def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1



