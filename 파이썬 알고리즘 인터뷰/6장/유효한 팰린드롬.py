class Solution:
    # 나의 풀이 (Runtime: 56ms, Memory: 15.4MB)
    def isPalindrome(self, string: str) -> bool:
        str_list = []
        answer = True

        # 소문자로 변환한 후 0-9, a-z에 해당하는 문자만 추출한다.
        for char in string.lower():
            if (48 <= ord(char) <= 57) or (97 <= ord(char) <= 122):
                str_list.append(char)

        # 중앙 인덱스를 구하고, 길이의 짝/홀 여부에 따라 적절히 반으로 나눈다.
        length = len(str_list)
        middle = length // 2
        left = str_list[: middle]
        right = str_list[middle:] if length % 2 == 0 else str_list[middle + 1:]

        # 좌/우 배열을 비교해 일치 여부를 판별한다.
        for idx, elem in enumerate(left):
            if elem != right[len(right) - idx - 1]:
                answer = False

        return answer

    # 책의 배열을 이용한 풀이 (Runtime: 288ms, Memory: 19.6MB)
    def answer_with_array(self, string: str) -> bool:
        chars = []
        # 문자열과 숫자만 필터링한다.
        for char in string:
            if char.isalnum():
                chars.append(char.lower())

        while len(chars) > 1:
            left = chars.pop(0)
            right = chars.pop()

            if left != right:
                return False

        return True

    # 책의 데크(Deque)를 이용한 풀이 (Runtime: 56ms, Memory: 19.1MB)
    def answer_with_deque(self, string: str) -> bool:
        # 데크 자료형을 사용할 수 있도록 선언한다.
        from collections import deque
        chars = deque()

        for char in string:
            if char.isalnum():
                chars.append(char.lower())

        while len(chars) > 1:
            left = chars.popleft()
            right = chars.pop()

            if left != right:
                return False

        return True


