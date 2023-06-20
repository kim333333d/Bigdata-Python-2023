# 파일 입출력
# DB open / close Network open / close File open / close

# 파일 생성
import os
cur_path = os.getcwd() #현재 파이썬 경로
# print(cur_path)

filename = './Day_03/sample.txt'
# filename = 'C:/Temp/sample.txt'
# filename = 'C:\\Source\\Bigdata-Python-2023\\Day_03\\test.txt' #절대경로
# filename = 'C:/Source/Bigdata-Python-2023/Day_03/test2.txt' #절대경로 리눅수/유닉스와 동일
f = open(filename, mode='wt', encoding='utf-8') # 텍스트 파일 생성(ascii코드 기본)

f.write('인생은 실전이야 존만아~\n')
f.write('인생 씁다') # 마지막 문장에는 \n을 쓰지 않는다.

f.close() # 무조건 닫아
print(f'{filename}이(가) 생성되었습니다.')

# 파일 읽기

fr = open(filename, mode='rt', encoding='utf-8') # 파일 읽기
while True: # 무한루프
    Line = fr.readline() # 한줄씩 읽기
    if not Line: break   # 읽을 줄이 없으면 빠져나감
    print(Line, end='')  # \n과 엔터가 두번 들어감

fr.close() # 반드시 닫기
