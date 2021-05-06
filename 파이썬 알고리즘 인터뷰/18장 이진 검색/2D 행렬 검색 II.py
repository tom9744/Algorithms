from typing import List


class Solution:
    # 투 포인터 풀이 (Runtime: 164ms, Memory: 20.7MB)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            # 타겟보다 행의 마지막 요소가 작으면, 다음 행으로 넘어간다.
            if row[-1] < target:
                continue
            # 타겟과 행의 마지막 요소가 같으면, 즉시 반환한다.
            elif row[-1] == target:
                return True

            # 타겟보다 행의 마지막 요소가 크면, 왼쪽 방향으로 탐색해 나간다.
            for idx in range(len(row) - 1, -1, -1):
                if row[idx] < target:
                    break
                elif row[idx] == target:
                    return True

        return False

    # 투 포인터 풀이 (Runtime: 176ms, Memory: 20.6MB)
    def searchMatrix_bruteforce(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            for col in row:
                if col == target:
                    return True

        return False
