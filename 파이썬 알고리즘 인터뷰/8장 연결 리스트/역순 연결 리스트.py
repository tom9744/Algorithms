# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 나의 풀이 (Runtime: 32ms, Memory: 15.6MB)
    def reverseList(self, head: ListNode) -> ListNode:
        reverse_head = None
        
        while head:
            # shift()로 기존 리스트의 헤드를 잘라낸다.
            current_head, head = head, head.next
            current_head.next = None
            
            # unshift()로 잘라낸 헤드를 역순 연결 리스트에 추가한다.
            if reverse_head is None:
                reverse_head = current_head
            else:
                current_head.next, reverse_head = reverse_head, current_head
            
        return reverse_head
          
    # 책의 재귀 함수를 이용한 풀이 (Runtime: 40ms, Memory: 20.4MB)
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev

            return reverse(next, node)

        return reverse(head)

    # 책의 반복문을 이용한 풀이 (Runtime: 24ms, Memory: 15.6MB)
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev 



    