# 코딩테스트 연습 > 해시 > 전화번호 목록 (Level2)
def solution(phone_book):
    # 람다식을 이용해, 전화번호부를 1) 알파벳 순, 2) 길이 순으로 정렬한다.
    phone_book.sort(key=lambda elem: [elem, len(elem)])

    # 정렬되어 있는 상태이므로, 숫자의 앞/뒤만 확인하면 된다.
    for index in range(len(phone_book) - 1):
        number = phone_book[index]
        next_number = phone_book[index + 1]

        # 다음 수가 현재 숫자로 시작하는 경우 False 반환.
        if number == next_number[:len(number)]:
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123","456","789"]))  # True
print(solution(["12","123","1235","567","88"]))  # False
