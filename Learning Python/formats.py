def commas(n):
    s = str(n)
    if len(s) <= 3:
        return s
    else:
        return commas(s[:-3]) + ',' + s[-3:]

def money(n, currency='$'):
    sign = '-' if n < 0 else ''
    n = abs(n)
    return sign + currency + commas(n)


if __name__ == '__main__':
    def selftest():
        print(commas(1234567.890))
        print(money(1234567890))
        print(money(1234567890, '£'))

    import sys
    if len(sys.argv)==1:
        selftest()
    else:
        print(money(int(sys.argv[1]), sys.argv[2] if len(sys.argv)>2 else '$'))
