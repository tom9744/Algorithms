class Solution:
    # 나의 풀이 (Runtime: 8224ms, Memory: 14.3MB)
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                sliced = s[i:j + 1]

                if len(sliced) < len(answer):
                    break

                if sliced == sliced[::-1] and len(answer) < len(sliced):
                    answer = sliced

        return answer

    # 투 포인터/슬라이딩 윈도우를 이용한 풀이 (Runtime: 256ms, Memory: 14MB)
    def answer_with_two_pointers(self, string: str) -> str:
        def expand(left: int, right: int) -> str:
            # 투 포인터가 범위 내에 있을 경우, 팰린드롬 여부를 검사한다.
            while left >= 0 and right < len(string):
                if string[left] == string[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return string[left + 1:right]

        # 문자열의 길이가 1이거나, 문자열 전체가 팰린드롬인 경우 즉시 반환한다.
        if len(string) < 2 or string == string[::-1]:
            return string

        result = ''

        for idx in range(0, len(string) - 1):
            # 짝수 길이, 홀수 길이 팰린드롬 여부를 확인하고 길이가 최대인 문자열을 저장한다.
            result = max(result,
                         expand(idx, idx + 1),
                         expand(idx, idx + 2),
                         key=len)

        return result
