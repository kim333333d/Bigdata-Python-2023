#변수  
import sys
number = 2111111111111111111111123123213123123213
value = sys.maxsize + 1 # sys.maxsize 파이썬 시스템에서 제공하는 최고숫자
print(number)
print(value + 1)

#8진수
value2 = 0o12
print(value2)

#16진수
value2 = 0xFF
print(value2)

#문자
value2 = 'Hello, python'
print(value2)

value2 = False
print(value2 == False)

#사칙연선, 수학식

#정수 + 소수점
print(20 / 3)
#정수
print(21 // 3)
#나머지 #배수를 구할때 사용
print(14 % 3)
#제곱연산
print(2 ** 10)