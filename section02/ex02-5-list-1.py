'''
리스트(List)
    -순서가 있는 데이터 집합
    -중복 허용, 수정 가능
    -다양한 자료형 포함 가능
'''

#1. 리스트 생성과 접근
pokemon_list = ['피카츄', '라이츄', '파이리']
print('리스트 전체:', pokemon_list)
print('첫번째 포켓몬:', pokemon_list[0])
print('리스트 길이:', len(pokemon_list))
print('첫번째 포켓몬 문자열 길이:', len(pokemon_list[0]))

print(pokemon_list[0:2])
print(pokemon_list[0:2][1])
p2 = ['피카츄', '라이츄']
print(p2[1])

# 문자열 len()
print('문자열 길이:', len('Hello'))

#2. 리스트 슬라이싱
fruit_list = ['블루베리', '바나나', '사과', '자몽', '체리', '망고']
print(fruit_list[2:5])
print(fruit_list[1:])
print(fruit_list[-2:])
print(fruit_list[::-1]) # 역순으로 출력
print(fruit_list[5:2:-1]) # 역순으로 출력
print(fruit_list[:3])
# 스텝 테스트 2: ['블루베리', '사과, '체리]
print('스텝테스트 2:', fruit_list[0:6:2]) #하나 걸러 하나씩 출력

#3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1, 2, 3, 4, 5]
boolean_list = [True, False, True]
mixed_list = [' 문자열', 100, True, 3.14]

#4. 단일 항목 수정
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_list[1] = '잠만보'
print(pokemon_list)

#5. 범위 수정
evolution_list = ['피카츄', '라이츄', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['라이츄Z', '메가파이리']
print(evolution_list)
