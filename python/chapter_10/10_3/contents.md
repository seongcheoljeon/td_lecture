# 10-3. 메서드 오버라이드(override)

```python
class Set:
    def __init__(self, seq=None):
        self.seq = seq

    # ss & [1, 2, 3]
    def __and__(self, other):
        tmp = []
        for i in other:
            if i in self.seq:
                tmp.append(i)
        return tmp

    def __rand__(self, other):
        return self.__and__(other)

    # ss | [1, 2, 3]
    def __or__(self, other):
        tmp = self.seq[:]
        for i in other:
            if i not in tmp:
                tmp.append(i)
        return tmp

    def __ror__(self, other):
        return self.__or__(other)

    # len(ss)
    def __len__(self):
        return len(self.seq)

    # ss[2]
    def __getitem__(self, item):
        if not item < 0 and item > len(self.seq):
            return 1
        return self.seq[item]

    # ss[2] = 555
    def __setitem__(self, key, value):
        self.seq[key] = value

    # del ss[2]
    def __delitem__(self, key):
        del self.seq[key]

    # 1 in ss
    def __contains__(self, item):
        return item in self.seq

    # bool(ss)
    def __bool__(self):
        return self.seq != None

    # print(ss)
    def __repr__(self):
        return repr(self.seq)


ss = Set([1, 2, 3, 5])

print(ss.seq)
print('-' * 100)
print(ss & [3, 4, 5, 6])
print(ss | [1, 2, 3, 4, 5, 6])
print(ss[3])
print(len(ss))

print('-' * 100)
ss[2] = 555
print(ss)
del ss[3]
print(ss)
print(10 in ss)
print(1 in ss)
print(bool(ss))
```
