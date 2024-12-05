'''
파일명: Ex11-3-function

Return
    함수는 작업을 수행한 결과를 변환(return)할 수 있다.
    반환된 값은 함수 호출한 위치에서 사용할 수 있다.
'''
from unittest import removeResult


def address():
    str='''우편번호 12345
서울시 은평구 수색동'''
    return str

result = address()
print(result)

def plus(num1,num2):
    return num1 + num2

result = plus(5,7)
print(result)