class Solution:
    # 나의 풀이 (Runtime: 28ms, Memory: 14.2MB)
    def reorderLogFiles(self, logs: list) -> list:
        letters = []
        digits = []

        # 숫자/문자 여부를 확인하고, 알맞은 배열애 나누어 저장한다.
        for log in logs:
            first_word = log.split()[1]

            if first_word.isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 문자를 기준으로 정렬하되, 동일한 경우 Identifier를 기준으로 정렬한다.
        letters.sort(key=lambda elem: (elem.split()[1:], elem.split()[0]))

        return letters + digits
