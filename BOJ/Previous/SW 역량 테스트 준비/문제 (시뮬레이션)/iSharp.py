# 3568: iSharp
#
# 처음에는 정규표현식을 사용할지 고민했지만, 연산자의 종류가 다양하지 않아서
# 그냥 조건문으로 하드코딩하여서 풀이하였다.
#
# 공백(' ')으로 구분되어 있으므로 split() 함수를 사용해 각각으로 나누고,
# 변수 선언문 각각(a*[]& 등...)에 대하여 추가 연산자와 변수명을 구분하는 작업을 수행한다.
#
# 이 때, '['와 ']'는 뒤집어서 배열에 넣어주어야 reverse() 메서드를 수행할 때
# 그 결과가 정상적으로 출력된다.

statement = input().split()
dataType, variables = statement[0], statement[1:]

for var in variables:
    varName = []
    extraOperators = []

    for each in var:
        if each == "," or each == ";":
            continue
        elif each == "*" or each == "&":
            extraOperators.append(each)
        elif each == "[":
            extraOperators.append("]")
        elif each == "]":
            extraOperators.append("[")
        else:
            varName.append(each)

    extraOperators.reverse()
    operator = dataType + "".join(extraOperators)
    variable = "".join(varName)

    print("{0} {1};".format(operator, variable))