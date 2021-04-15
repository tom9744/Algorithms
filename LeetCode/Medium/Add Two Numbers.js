class ListNode {
    constructor(value) {
      this.val = value;
      this.next = null;
    }
  }
  
class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  
  push(value) {
    const newNode = new ListNode(value);
    
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      const currentTail = this.tail;
      currentTail.next = newNode;
      this.tail = newNode;
    }
    
    this.length++;
    
    return this;
  }
}

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
  const result = [];
  let currOne = l1;
  let currTwo = l2;
  let carry = 0;
  
  while(currOne || currTwo) {
    // 노드가 null인 경우, 0으로 대체한다.
    const numOne = currOne ? currOne.val : 0; 
    const numTwo = currTwo ? currTwo.val : 0;
    // 이전 계산에서 넘어온 carry 변수를 함께 더한다.
    const sum = numOne + numTwo + carry;
    
    // 자리올림이 필요한 경우, carry 변수에 1을 저장한다.
    result.push(sum > 9 ? sum % 10 : sum);
    carry = sum > 9 ? 1 : 0;
    
    if (currOne) currOne = currOne.next;
    if (currTwo) currTwo = currTwo.next;
    
    // [Edge Case] 맨 끝에서 자리올림이 발생하는 경우 처리
    if (!currOne && !currTwo && carry === 1) result.push(1); 
  }
  
  // 단방향 연결 리스트를 생성한다.
  const linkedList = new SinglyLinkedList();
  
  result.forEach(digit => { linkedList.push(digit); });
  
  return linkedList.head;
};