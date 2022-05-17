'''
1) 입력 "17" => 1, 7로 만들 수 있는 소수 구하기
2) 입력은 1이상 7이하인 문자열
=> 소수의 범위 < 10000000
=> prime dict를 만들다보니 시간 너무많이씀 ㅠㅠ


import math
from itertools import permutations

def prime_dict(n):
    prime_dict = {i: 0 for i in range(2, n + 1)}
    for k in range(2, math.ceil(n ** 0.5)):
        c = 2
        while c * k <= n:
            if c * k in prime_dict:
                del prime_dict[c*k]
            c += 1
    return prime_dict

def solution(numbers):
    if int(numbers) == 0:
        return 0
    number_list = list(numbers)
    max_num = int(''.join(sorted(number_list, reverse=True)))
    n_prime = prime_dict(max_num)
    permu = []
    for i in range(len(number_list)):
        permu += list(map(lambda x: int(''.join(x)), permutations(number_list, i + 1)))
    answer = len(set(permu) & set(n_prime.keys()))

    return answer
'''

'''
1) 입력 "17" => 1, 7로 만들 수 있는 소수 구하기
2) 입력은 1이상 7이하인 문자열

idea > 
만들 수 있는 숫자를 구한 뒤 prime 체크 후 개수 세기
'''
import math
from itertools import permutations

def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    if int(numbers) == 0:
        return 0
    number_list = list(numbers)
    max_num = int(''.join(sorted(number_list, reverse=True)))
    permu = []
    for i in range(len(number_list)):
        permu += list(map(lambda x: int(''.join(x)), permutations(number_list, i + 1)))
    permu = list(set(permu))
    answer = 0
    for num in permu:
        if isPrime(num):
            answer += 1
    
    return answer