from typing import List


class Solution:
    # 나의 풀이 (Runtime: 96ms, Memory: 17.2MB)
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        frequency = {}
        answer = []

        for string in strings:
            # 문자열을 정렬해 애너그램인 경우, 동일한 문자열로 만든다.
            key = "".join(sorted(string))

            # 해당 문자열을 Key로 사용해 딕셔너리를 구성한다.
            if key in frequency:
                frequency[key].append(string)
            else:
                frequency[key] = [string, ]

        # 구성한 딕셔너리를 순회하며, 정답을 생성한다.
        for key in frequency:
            answer.append(frequency[key])

        return answer