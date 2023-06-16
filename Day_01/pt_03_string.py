

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

print(origin[15:]) # index 15~ 끝까지
print(origin[15:-7]) # 음수는 뒤에서부터 인덱스 -1 부터시작

print('I ate %s apples' % ('three')) # % string formating
print('I ate %d apples' %(3))
print('pi is %f' % 3.14159265359)
print('pi is %10.2f' % 3.14159265359)

# 날짜 문자열 포맷팅
import datetime as dt
curr_dt = dt.datetime.now()
fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')
print(curr_dt)
print('오늘 날짜는 %s 입니다.' % curr_dt.strftime('%Y년 %m월 %d일')) 
# C#/Java yyyy년MM월dd일

# 최신 포맷팅
apple_num = 3
print(f'i ate {apple_num:0.4f} apples')
apple_num = 'three'
print(f'i ate {apple_num} apples')
print(f'오늘 날짜는{fmt_dt}입니다.')

# 문자열 함수 
# Life is short, You need Python
print(origin.count('e')) # 문자,문자열의 개수
print(origin.find('Python')) # 문자나 문자열 차는 시작 인덱스 -1은 없음

print('/'.join(origin)) # 문자(열) join에 있는 문자열이랑 하나씩 조인하는 것
print(origin.upper()) # 전부 대문자
print(origin.lower()) # 전부 소문자
print(origin.capitalize()) # 문자열의 시작단어만 대문자로
print(origin.title()) # 단어의 첫번째 단어만 대문자로

print('start' + '    Hello    ' + 'end') # 기본
print('start' + '    Hello    '.lstrip() + 'end') # 왼쪽   공백 지우기
print('start' + '    Hello    '.rstrip() + 'end') # 오른쪽 공백 지우기
print('start' + '    Hello    '.strip()  + 'end')  # 양쪽  공백 지우기

# 스플릿 모든것을 단어별로 짤라버린다. 배열(리스트)
result = origin. replace(',','').split(' ')
print(result)


