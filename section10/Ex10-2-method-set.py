'''
파일명: Ex10-2-method-set.py
'''


# 교집합 intersection()
s1 = {'apple','banana','cherry',3}
s2 = {'apple','banana','orange',3}
result = s1.intersection(s2)
print('교집합')
print(result)
print(s1 & s2)

# 합집합 union()
s1 = {'apple','banana','cherry',3}
s2 = {'apple','banana','orange',3}
result = s1.union(s2)
print('합집합')
print(result)
print(s1 | s2)

# 차집합 difference()
s1 = {'apple','banana','cherry',3}
s2 = {'apple','banana','orange',3}
result = s1.difference(s2)
print('차집합')
print(result)
print(s2 - s1)