from libs.algorithm import algorithm as algo


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
        stack = algo.Stack()

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
        stack = algo.Stack()

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


if __name__ == '__main__':
    for expr in ('(3 + 5) * 2', '((1 + 2) * 3) / 4 + 5 * (6 - 7)'):
        postfix = CalculateExp.infix_to_postfix(expr)
        calc = CalculateExp.eval_postfix(postfix)
        print(f'{expr} -> {postfix} -> {calc}')