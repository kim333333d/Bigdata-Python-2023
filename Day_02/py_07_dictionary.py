# 딕셔너리
# 키 값은 중복 불가 (Primary Key)
# 키 값에 배열 불가 (무조건 하나, 변하지 않는 값으로 하나)
iron_man = {'name' : 'Tony Stark', 'address' : 'New York', 'armer' : 'Repluser Arm'}

print(iron_man)

# 아래 두개 결과 동일
print(iron_man.get('name'))
print(iron_man['name'])

# Key는 중복 허용 X
d1 = {1 : 'a', 1 : 'b'}
print(d1)

# Value 중복 허용 O
d2 = {1 : 'test', 2 : 'test'}
print(d2)

print(iron_man.keys())

for item in iron_man.keys():
    print(item)

print(iron_man.values())

print(iron_man.items())
print(iron_man)