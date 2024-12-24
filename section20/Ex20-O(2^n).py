'''
파일명: Ex20-O(2^n).py

0(2^n)
    지수 시간 복잡도, 피보나치 수열처럼 재귀적 알고리즘

'''

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(8))