'''
파일명: Ex08-2-break.py
'''

i = 0
while i <= 7:
    '''
    i=0
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=1
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=2
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=3
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=4
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=5
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=6
    j=0, 1, 2, ... 6, 7(프린트 안함)
    *******
    i=7(프린트 안함) 
    '''
    j = 0
    while j < 7:
        print('*', end='')
        j += 1
    print()
    i += 1

i = 0
while i <= 7:
    '''
    i=0, 1
    i j
    '''
    j = 0
    while j < i+1:
        print('*', end='')
        if j == 3:
            break
        j += 1
    print()
    i += 1