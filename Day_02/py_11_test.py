# Q1

Mr_Hong = {'KR' : 80, 'EN' : 75, 'MT' : 55}
num = 0

for item in Mr_Hong.values():
    num += item
print(f'홍길동의 평군점수는 {num/3} 입니다.')

# Q2

i = 13

if(i%2 == 0):
    print('짝수입니다.')
else:
    print('홀수입니다.')

result = 13 % 2 == 0
print(f'{i} 은 짝수? {result}')

# Q3

pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

# 04

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 05

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4 ,5]
aSet = (set(a))
b = list(aSet)
print(b)