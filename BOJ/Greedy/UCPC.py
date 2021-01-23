# 15904 :  UCPC는 무엇의 약자일까?
#
# UCPC를 구성하는 각 문자를 배열로 만들고, 문자를 하나 꺼내면서
# 주어진 문자열에 존재하는지 검사한다. 이때, UCPCPC도 UCPC가 포함되므로 "I love UCPC"로 출력해야 한다.
# 이 부분은 문제가 좀 이상한듯...

string = input()
counter = 0
targets = ["U", "C", "P", "C"]
target = targets.pop(0)

for char in string:
    if char is target:
        counter += 1
        if len(targets) > 0:
            target = targets.pop(0)
        else:
            break

if counter == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")