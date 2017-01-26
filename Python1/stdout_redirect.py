# перенапрввление вывода
import sys
tmp_out = sys.stdout
with open(r'out.txt', 'a') as f:
    sys.stdout = f

    print('Redirect out')
    print(14)

sys.stdout = tmp_out
