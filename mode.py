def mode(L):
    if len(L) == 0:
        return None

    counters = []
    for x in L:
        for c in counters:
            if c[0] == x:
                c[1] += 1
                break
        else: # Runs if the for loop finishes and did *not* break.
            counters.append([x, 1])   

    frequency_of_mode = 0
    m = 0
    for i in range(len(counters)):
        if counters[i][1] > frequency_of_mode:
            frequency_of_mode = counters[i][1]
            m = counters[i][0]

    return m

L = []
while True:
    inp = input()
    if inp == '':
        break
    L.append(inp)
print(f'mode: {mode(L)}')

#f strings
s = f''