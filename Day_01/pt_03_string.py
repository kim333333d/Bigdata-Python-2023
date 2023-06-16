#문자열

value = "Hello World"
print(value)
print("Hello World")

print('저는 "아무개"입니다')
print("저는 '아무개'입니다")

#여러줄을 쓸때
value = '''
안녕하세요.
저는 프로그래머입니다.
프로그래밍을 잘합니다.
'''   # 여러줄 문장

print(value)

'''
애는 여러줄 주석으로 대체합니다.
파이선에는 여러줄 주석이 없어서 
여러줄 문자열로 이역할을 대신합니다.
'''

print('Hello' + 'World!') # (* 문자는 불가)
print('Hello' * 3) # Hello를 3번 반복하라 (+ 숫자는 안됨)

print(len('Life is short')) # 문자의 길이(공백포함)
print(len('인생은 짧아요.')) # 문자의 길이(공백포함, .도 포함)

origin = 'Life is short, You need Python'
print(origin[13])
print(origin[0] + origin[16] + 
      origin[19] + origin[20] + 
      origin[0].lower() + origin[15].lower())
print(origin[0:4]) # == print(origin[:4])
print(origin[8:13])
