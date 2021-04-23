# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # 나의 풀이 (Runtime: 60ms, Memory: 14.1MB)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = None
        new_tail = None
        carry = 0
        
        while True:
            # 더 이상 남은 수가 없을 때, 자리올림수(carry)가 있다면 추가하고 종료한다.
            if not l1 and not l2:
                if carry == 1:
                    new_node = ListNode(carry)
                    new_tail.next = new_node
                    new_tail = new_tail.next
                break
            
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            summary = num1 + num2 + carry
            
            # 자리수와 자리올림수를 계산한다.
            value = summary % 10
            carry = 1 if summary > 9 else 0
            
            # 새로운 노드를 생성한다.
            new_node = ListNode(value)
            
            # 연결 리스트의 push() 메서드 방식으로 추가한다.
            if new_head is None:
                new_head = new_node
                new_tail = new_node
            else:
                new_tail.next = new_node 
                new_tail = new_tail.next
                
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            
        return new_head

    # 책의 풀이 (Runtime: 72ms, Memory: 14.3MB)
    def answer(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합을 계산한다.
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 자리수와 자리올림수를 계산한다.
            carry, value = divmod(sum + carry, 10)

            # 연결 리스트에 추가한다.
            head.next = ListNode(value)
            head = head.next

        return root.next