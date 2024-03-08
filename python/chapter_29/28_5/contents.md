# 28-5. 스택(Stack) & 큐(Queue)

## Stack

> 리스트는 대표적인 선형 자료구조이다. 스택 또한 선형 자료구조의 일종이다.

### 스택의 이해

스택 자료구조를 비유할 수 있는 예는 주변에서 쉽게 찾아볼 수 있다. 예를 들면 "쌓아 올려진 접시"가 있다.   
스택은 다음과 같은 특성을 지닌다.

> 먼저 들어간 것이 나중에 나온다. 다른 말로는 나중에 들어간 것이 먼저 나온다. 
> 
> 이렇듯 스택은 나중에 들어간 것이 먼저 나오는 구조이다 보니 '후입선출 방식의 자료구조'라고도 불리고,
> 영어로 'LIFO(Last-In, First-Out) 구조의 자료구조'라고도 불린다.

### 스택 ADT의 정의

+ 데이터를 넣는다 : push
+ 데이터를 꺼낸다 : pop
+ 이번에 꺼낼 데이터가 무엇인지 들여다 본다 : peek

스택을 대표하는 넣고, 꺼내고, 들여다 보는 연산을 가리켜 각각 push, pop, peek라고 한다.   
따라서 스택의 ADT는 다음과 같이 정의가 되며, 이것이 스택의 보편적인 ADT이다.

### 스택 자료구조의 ADT

+ is_empty(stack: Stack) -> bool
  + 스택이 빈 경우 true, 그렇지 않은 경우 false
+ push(stack: Stack, data: Data) -> None
  + 스택에 데이터를 저장한다. 매개변수 data로 전달도니 값을 저장
+ pop(stack: Stack) -> data
  + 마지막에 저장된 요소 삭제
  + 삭제된 데이터는 반환
  + 해당 함수 호출을 위해 데이터가 하나 이상 존재함이 보장되어야 한다
+ peek(stack: Stack) -> data
  + 마지막에 저장된 요소를 반환하되 삭제하지 않는다.
  + 해당 함수 호출을 위해 데이터가 하나 이상 존재함이 보장되어야 한다

```python
class Stack:
    def __init__(self, data: list):
        self.__data = data

    def push(self, data) -> None:
        self.__data.append(data)

    def pop(self):
        if self.is_empty():
            raise ValueError('stack memory error!')
        return self.__data.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError('stack memory error!')
        return self.__data[-1]

    def is_empty(self) -> bool:
        if len(self.__data) == 0:
            return True
        return False


s = Stack([])

s.push(1)
s.push(2)
s.push(3)
s.push(4)

while not s.is_empty():
    print(s.pop())
```

### Stack을 이용한 수식 트리
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


class CalculateExp:
    @staticmethod
    def precedence(op):
        if op == '(' or op == ')':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return -1

    @staticmethod
    def is_operator(term):
        return term in ('+', '-', '*', '/')

    @staticmethod
    def has_higher_precedence(op1, op2):
        return CalculateExp.precedence(op1) >= CalculateExp.precedence(op2)

    @staticmethod
    def infix_to_postfix(expression: str) -> str:
        res = ''
        stack = Stack()

        for exp in expression:
            if exp.isnumeric():
                res += exp
            elif exp == '(':
                stack.push(exp)
            elif exp == ')':
                while stack.peek() != '(':
                    res += stack.pop()
                stack.pop()
            elif CalculateExp.is_operator(exp):
                if (not stack.is_empty()) and (stack.peek() != '(') and CalculateExp.has_higher_precedence(stack.peek(), exp):
                    res += stack.pop()
                stack.push(exp)

        while not stack.is_empty():
            res += stack.pop()

        return res

    @staticmethod
    def eval_postfix(expression: str) -> float:
        stack = Stack()

        for exp in expression:
            if exp.isnumeric():
                stack.push(float(exp))
            elif exp != ' ':
                n2 = stack.pop()
                n1 = stack.pop()
                if exp == '+':
                    res = n1 + n2
                elif exp == '-':
                    res = n1 - n2
                elif exp == '*':
                    res = n1 * n2
                else:
                    res = n1 / n2
                stack.push(res)
        return stack.pop()
```

to be continue...


