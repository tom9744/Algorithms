# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 나의 풀이 (Runtime: 28ms, Memory: 14.3MB)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        
        # 리스트 1, 리스트 2에서 가장 작은 값을 선택해 새로운 리스트를 만든다.
        while l1 or l2:
            if l1 is None:
                if head is None:
                    head = l2
                    tail = head
                else:
                    tail.next = l2
                break
            if l2 is None:
                if head is None:
                    head = l1
                    tail = head
                else:
                    tail.next = l1
                break
            
            if l1.val < l2.val:
                # 처음 값을 삽입하는 경우, head와 tail을 초기화한다.
                if head is None:
                    head = l1
                    tail = head
                # 그렇지 않은 경우, push()를 수행한다.
                else:
                    tail.next = l1
                    tail = tail.next
                # 선택한 값을 기존 리스트에서 제거한다.
                l1 = l1.next
            else:
                if head is None:
                    head = l2
                    tail = head
                else:
                    tail.next = l2
                    tail = tail.next
                l2 = l2.next

        return head


    # 책의 재귀 함수를 이용한 풀이 (Runtime: 40ms, Memory: 14.3MB)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not li) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if li:
            li.next = self.mergeTwoLists(l1.next, l2)
        return l1