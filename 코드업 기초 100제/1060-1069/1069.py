# 1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기

integer = input()

dict = {
    "A": "best!!!",
    "B": "good!!",
    "C": "run!",
    "D": "slowly~"
}

if integer in dict:
    print(dict[integer])
else:
    print("what?")
