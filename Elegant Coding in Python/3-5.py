def read_lines_for_python(file_name, file_type):
    if file_type not in ('txt', 'csv'):
        raise ValueError('Not correct file type')
    if not file_name:
        raise IOError('File not found')

    with open(file_name, 'r') as fileread:
        for line in fileread:
            if 'python' in line:
                return 'Found Python'

if not read_lines_for_python(None ,'txt'):
    print('Python not found')