'''
파일명: Ex10-1-method-string.py

메소드(method)
    특정 객체가 가지고 있는 함수를 의미한다
    객체명.메소드() 사용 가능

'''

# String 객체 format 메소드
print('10자리 폭 왼  쪽 정렬 "{:<10d}"'.format(123))
print('10자리 폭 오른쪽 정렬 "{:>10d}"'.format(123))
print('10자리 폭 가운데 정렬 "{:^10d}"'.format(123))

print('10자리 폭 왼  쪽 정렬 채움문자 "{:*<10d}"'.format(123))
print('10자리 폭 오른쪽 정렬 채움문자 "{:*>10d}"'.format(123))
print('10자리 폭 가운데 정렬 채움문자 "{:*^10d}"'.format(123))

print("{:*^10d}".format(123))

# Join 메소드 추가 예제
s = '-'.join('python')
print(s)
s = '+'.join(['a','b','c','d','e'])
print(s)

# split() 메소드 추가예제
s='010-1234-5678'
result=s.split('-')
print(result)
print(f'010-****-{result[2]}')

# strip(), lstrip(), rstrip() 공백제거 메소드
s='     apple      '
result=s.strip()
print(result)

s='     apple      '
result=s.lstrip()
print(result)

s='     apple      '
result=s.rstrip()
print(result)

# replace 메소드
s='    a  p  p  l  e    '
result=s.replace(' ',"")
print(result)

s='Life is too short'
result=s.replace('short','long')
print(result)

