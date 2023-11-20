class BinStr:
    def __init__(self, n_str = ''):
        self.n = n_str

    def __add__(left, right):
        string = ''
        smaller = left.n
        larger = right.n
        if len(right.n) < len(smaller):
            larger = left.n
            smaller = right.n

        offset = len(larger) - len(smaller)
        for i in range(len(larger) - 1, -1, -1):
            if i - offset < 0:
                string += larger[i]
            else:
                string += '1' if larger[i] == '1' or smaller[i - offset] == '1' else '0'
        return string[::-1]

    def __sub__(left, right):
        string = ''
        for l_d, r_d in zip(left.n[::-1], right.n[::-1]):
            string += '1' if l_d == '1' and r_d == '1' else '0'
        return string[::-1]

    def __eq__(left, right):
        return (left.n == right.n)

    def __gt__(left, right):
        #Just check which number is longer first
        if len(left.n) > len(right.n):
            return True
        if len(left.n) < len(right.n):
            return False

        # Make sure that they arent empty, after previous if statements, the lengths are the same
        if len(left.n) == 0:
            return False

        #Look for first different digit.
        for l_d, r_d in zip(left.n, right.n):
            if l_d == r_d:
                continue
            if l_d == '0':
                return False
            return True

    def __int__(self):
        sum = 0
        for bit in range(len(self.n)):
            pos = len(self.n) - 1 - bit
            if self.n[pos] == '1':
                sum += (2 ** bit)
        return sum

    def __str__(self):
        return '0b' + self.n


a = BinStr('10100')
b = BinStr('10100')

def compare_test():
    a = BinStr('10110')
    b = BinStr('')