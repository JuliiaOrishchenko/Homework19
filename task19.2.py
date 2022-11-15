def in_range(end, start=0, step=1):
    temp = []
    counter = 0
    while start + counter < end:
        temp.append(start+counter)
        counter += step
    return temp


for i in in_range(10, 5, 2):
    print(i)
