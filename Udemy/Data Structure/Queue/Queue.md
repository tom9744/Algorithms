# Queue

큐(Queue)는 데이터의 추가/삭제만을 지원하며, 스택과 달리 선입선출(First-In-First-Out, FIFO)의 특성을 가진다. 선입선출이란, **가장 먼저 추가된 데이터가 가장 먼저 제거되는 특성**을 말한다.

큐의 추상자료형(Abstract Data Type, ADT)에 따라 다음과 같은 속성과 메서드를 가진다. 
 - [Prop] Front - 큐의 가장 앞에 대한 참조
 - [Prop] Back - 큐의 가장 뒤에 대한 참조
 - [Prop] Size - 큐의 길이
 - [Method] Enqueue - 큐의 가장 뒤에 데이터를 추가
 - [Method] Dequeue - 큐의 가장 앞에서 데이터를 제거

<br>

## 내장 배열을 이용한 구현

스택과 마찬가지로 Javascript의 내장 배열(*Array*)을 사용해 큐를 구현할 수 있다.

- `Array.prototype.push()`와 `Array.prototype.shift()`를 이용하는 방법
    - `push()`를 이용해 배열의 가장 뒤에 데이터를 추가한다. (Enqueue)
    - `shift()`를 이용해 배열의 가장 앞에서 데이터를 제거한다. (Dequeue)

- `Array.prototype.unshift()`와 `Array.prototype.pop()`을 이용하는 방법
    - `unshift()`를 이용해 배열의 가장 앞에 데이터를 추가한다. (Enqueue)
    - `pop()`을 이용해 배열의 가장 뒤에서 데이터를 제거한다. (Dequeue)

두가지 방법 모두 배열의 가장 앞에서 데이터를 추가/삭제하는 `shift()`, `unshift()` 메서드를 사용하기 때문에, **전체 배열의 인덱스 수정이 발생**하게 된다.

내장 배열을 사용해 스택을 구현할 때, `push()`와 `pop()`을 이용하면 효율적으로 구현할 수 있었지만, **내장 배열로 큐를 구현하는 것은 비효율적**이다.

따라서 최적의 성능이 요구되는 상황이라면 반드시 큐 자료구조를 직접 구현해 사용해야 한다.

<br>

## 연결 리스트를 이용한 구현

단방향 연결 리스트 또는 양방향 연결 리스트를 이용해 큐를 구현할 수 있다. 연결 리스트를 사용 해 큐를 구현하면, 인덱스에 대해 신경쓰지 않아도 되기 때문에 효율적이다.

다만 단방향 연결 리스트를 사용하는 경우, 리스트의 **맨 뒤에 데이터를 추가 및 제거하는 `pop()` 메소드의 시간 복잡도가 O(N)이라는 사실**을 기억해야 한다.

따라서, 단방향 연결 리스트를 사용해 큐를 구현하기 위해서는 `shift()`와 `push()` 메서드를 사용해야 한다.

> `unshift()`와 `pop()`을 사용하면, `pop()`의 시간 복잡도가 O(N)이기 때문에 큐의 조건을 만족하지 못한다.