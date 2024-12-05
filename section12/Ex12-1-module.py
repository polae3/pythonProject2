'''
파일명: Ex12-1-module.py

모듈 사용법
import 모듈명
'''


import converter

miles = converter.kilometer_to_miles(150)
print(f'150km = {miles} miles')

pound = converter.gram_to_pound(1000)
print(f'1000g = {pound} pounds')