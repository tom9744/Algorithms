class Solution:
    # 나의 풀이 (Runtime: 188ms, Memory: 18.6MB)
    def reverseString(self, strs: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        strs.reverse()

    # 책의 투포인터 풀이 (Runtime: 200ms, Memory: 18.6MB)
    def answer_with_two_pointer(self, strs: list) -> None:
        left = 0
        right = len(strs) - 1

        while left < right:
            # 포인터가 가르키는 두 원소의 자리를 바꾼다.
            strs[left], strs[right] = strs[right], strs[left]

            left += 1
            right -= 1
