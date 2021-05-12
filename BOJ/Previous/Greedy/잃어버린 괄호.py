# 1541 : 잃어버린 괄호
#
# +와 -가 번갈아서 나타나므로, 무조건 A-(B+C)-(D+E)와 같은 형태로
# 괄호를 붙이면 최소값이 나오게 된다.


expression = input()
pluses = expression.split('-')

accumulate = 0

for index in range(len(pluses)):
    num = sum(list(map(int, pluses[index].split('+'))))

    if index is 0:
        accumulate = num
    else:
        accumulate -= num

print(accumulate)