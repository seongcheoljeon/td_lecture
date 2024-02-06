# 15-1. 정규표현식(re)

## 문자열 변경 (Substitude)

sub 메서드를 이용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.

```python
import re

comp = re.compile(r'(blue|white|red)')

print(comp.sub('colour', 'blue socks and red shoes'))
print(comp.subn('colour', 'blue socks and red shoes'))
```

sub 메서드의 첫 번째 입력 인수는 "바꿀 문자열"이 되고, 두 번째 입력 인수는 "대상 문자열"이 된다. 바꾸기 횟수를 제어하려면 다음과 같은 
세 번째 입력 인수로 count값을 넘기면 된다.   

___comp.sub('colour', 'blue socks and red shoes', count=1)___

subn 역시 sub와 동일한 기능을 하지만 리턴되는 결과를 튜플로 리턴한다는 
차이가 있다. 리턴된 튜플의 첫 번째 요소는 변경된 문자열이고, 두 번째 요소는 바꾸기가 발생한 횟수이다.

### sub 메서드 사용 시 참조 구문 사용하기

```python
import re

comp = re.compile(r'''
    (?P<name>\w+)
    \s+
    (?P<phone>(\d+)[-]\d+[-]\d+)
''', re.VERBOSE)

print(comp.sub('\g<phone> \g<name>', 'zeon 010-1234-1234'))
```

위 예는 "이름 + 전화번호"의 문자열을 "전화번호 + 이름" 으로 바꾸는 예이다. sub의 바꿀 문자열 부분에 "\g<그룹명> 을 이용하면 정규식의 
그룹명을 참조 할 수 있다.그룹명 대신 참조 번호를 이용해도 마찬가지의 결과가 리턴된다.

### sub 메서드의 입력 인수로 함수 넣기

sub 메서드의 첫 번째 입력 인수로 함수를 넣을 수도 있다.

```python
import re

def dec2hex(match):
    val = int(match.group())
    return hex(val)

comp = re.compile(r'\d+')

print(comp.sub(dec2hex, 'call 65535 for printing. 45678 for user code.'))
```

dec2hex 함수는 match 객체(위에서 숫자에 마치되는)를 입력으로 받아 16진수로 변환하여 리턴하는 함수이다. sub의 첫 번째 입력 인수로 함수를 
사용할 경우, 해당 함수의 첫 번째 입력 인수에는 정규식과 매치된 match 객체가 입력된다. 그리고 매치되는 문자열은 함수의 리턴 값으로 바뀌게 된다.

```python
# example

import re

comp = re.compile(r'(?P<num>\d{3}[-]\d{4})[-]\d{4}')

s = '''
aaaa 010-1234-1234
bbbb 010-3456-9874
cccc 010-4321-3423
'''

result = comp.sub(r'\g<num>-####', s, re.MULTILINE)
print(result)
```