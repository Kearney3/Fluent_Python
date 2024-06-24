seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print(f'name:{module.__name__}, file:{module.__file__}')
        print(sepline)

    count = 0
    for attr in sorted(module.__dict__):
        print(f'{count:02d}) {attr}', end=' ')
        if attr.startswith('__'):
            print(f'<build-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(sepline)
        print(f'{module.__name__}) total: {count}')
        print(sepline)

if __name__ == '__main__':
    # import formats
    # listing(formats)
    # print(formats.__dict__)
    import pandas
    listing(pandas)
