with open('fu.txt', 'w') as my_file:
    for i in range(1000):
        if i == 0:
            my_file.write('fuck you 1 time\n')
        else:
            my_file.write(f'fuck you {i} times\n')