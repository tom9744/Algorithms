def solution(number, k):
    stack = []

    for num in map(int, number):
        # [반복] 스택의 마지막 요소가 현재값보다 작다면, 스택에서 제거하고 K를 1 감소시킨다.
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k = k - 1
        # 현재값을 스택에 추가한다.
        stack.append(num)

    # K개 만큼 숫자를 제거하지 못한 경우
    if k > 0:
        stack = stack[:len(number) - k]

    # 스택에 남은 요소를 문자형으로 변환하고, 하나로 합친다.
    return "".join(map(str, stack))