# перенапрввление вывода
# C:\Python34\python simple_for_call.py 2> err.txt 1> out.txt

s = ''

with open(r'simple_for_call.py', 'r') as f:
    for line in f:
        s = ''.join([s, str(line)])

exec(s)
