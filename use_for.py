for i in range(4):
    for j in range(4):
        print('*',end='')
    print()

print('-'* 30)

for i in range(5):
    for j in range(i):
        print('*', end='')
    print()

print('-'* 30)

for i in range(6):
    for j in range(6-i):
        print('*', end='')
    print()

print('-'* 30)

for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    print('*'*(2*i+1),end='')
    print()

print('-'* 30)

row = eval(input(':'))
while(row%2==0):
    row = eval(input(':'))
for i in range((row+1)//2):
    for j in range((row+1)//2-i):
        print('_', end='')
    print('*'*(2*i+1),end='')
    print()
for i in range((row-1)//2):
    for j in range(i+2):
        print('_', end='')
    print('*'*(row-2-2*i),end='')
    print()

print('-'* 30)

row = eval(input(':'))
while(row%2==0):
    row = eval(input(':'))
for i in range((row+1)//2):
    for j in range((row+1)//2-i):
        print('_', end='')
    for k in range(2 * i + 1):
        if k == 0 or k == 2*i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range((row-1)//2):
    for j in range(i+2):
        print('_', end='')
    for k in range(row-2-2*i):
        if k == 0 or k == row-2-2*i-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()