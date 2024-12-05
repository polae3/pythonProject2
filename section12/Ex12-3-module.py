'''
파일명: Ex12-3-module.py

as 키워드 별명 사용하기 (alias)
'''

import converter as cvt


miles = cvt.kilometer_to_miles(300)
print(f'300km = {miles} miles')