"""
计算文件中的行数和字数
"""

def countlines(filename):
    """
    计算文件中的行数
    """
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
        return count

def countwords(filename):
    """
    计算文件中的字数
    """
    with open(filename, 'r') as f:
        count = 0
        for line in f.read():
            count += len(line.split())
            # print(line, line.rsplit())
        return count

def printlines(filename):
    """
    打印文件中的每一行
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')

print(countlines('text.log'))
print(countwords('text.log'))
print(printlines('text.log'))
