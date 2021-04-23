# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 나의 리스트 슬라이싱을 이용한 풀이 (Runtime: 824ms, Memory: 46.9MB)
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        current_node = head
        
        # 연결 리스트를 배열의 형태로 변경한다.
        while current_node:
            array.append(current_node.val)
            current_node = current_node.next
        
        return array == array[::-1]
    

    # 책의 데크를 이용한 풀이 (Runtime: 816ms, Memory: 47.5MB)
    def isPalindrome(self, head: ListNode) -> bool:
        from collections import deque
        queue = deque()
        current = head

        while current:
            queue.append(current.val)
            current = current.next

        while len(queue) > 1:
            left, right = queue.popleft(), queue.pop()

            if left != right:
                return False

        return True

    # 책의 러너를 이용한 풀이 (Runtime: 672ms, Memory: 31.5MB)
    def answer_with_runnder(self, head: ListNode) -> bool:
        reverse = None
        slow = fast = head

        # 러너를 이용해 역순 연결 리스트를 생성한다.
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        
        # 연결 리스트의 길이가 홀수인 경우, 중앙값에 대한 예외처리
        if fast:
            slow = slow.next 

        # 팰린드롬 여부를 확인한다.
        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next

        return not reverse