'''
파일명: Ex11-2-function.py

매개변수
    함수는 다양한 입력값(매개변수)를 받을 수 있으며,
    입력값 바탕으로 작업을 수행한다.

'''
from tkinter.font import names

# 매개변수 있음, 리턴값 없음
def introduce(name,age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다. ')

introduce('Jay',36)

# 가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)

show('python','java','c++')



