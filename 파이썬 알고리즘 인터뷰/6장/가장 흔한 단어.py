import collections, re


class Solution:
    # 나의 풀이 (Runtime: 36ms, Memory: 14.5MB)
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        # 구두점을 제외하고, 소문자로 변환한 뒤, 단어 별로 쪼갠다.
        pre_processed = re.sub('[^a-zA-Z]', ' ', paragraph).lower().split()

        # 전처리된 단어 배열 중, 금지어를 제외한다.
        filtered = [word for word in pre_processed if word not in banned]

        # 단어의 등장 빈도수를 계산한다.
        frequency = collections.Counter(filtered)

        # 가장 많이 등장한 단어를 출력한다.
        return frequency.most_common(1)[0][0]

    # 책의 리스트 컴프리헨션, Counter 풀이 (Runtime: 36ms, Memory: 14.3MB)
    def answer_with_list_comprehension(self, paragraph: str, banned: list) -> str:
        # 구두점을 공백 ' '으로 변환하고, 소문자로 변환하며, 금지어에 있는 단어를 제외한다.
        pre_processed = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        # Counter를 이용해 빈도수를 센다.
        counts = collections.Counter(pre_processed)

        # 가장 빈도수가 높은 것의 key를 반환한다.
        return counts.most_common(1)[0][0]
