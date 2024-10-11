class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) == int:  # 피연산자인 경우
            postfixList.append(token)
        elif token == '(':  # 여는 괄호는 스택에 쌓음
            opStack.push(token)
        elif token == ')':  # 닫는 괄호일 경우, 여는 괄호가 나올 때까지 팝
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:  # 연산자인 경우
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    # 스택에 남은 연산자를 모두 후위 표기 리스트에 추가
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    operandStack = ArrayStack()

    for token in tokenList:
        if type(token) == int:  # 피연산자인 경우
            operandStack.push(token)
        else:  # 연산자를 만나면 두 개의 피연산자를 꺼내 연산 수행
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            operandStack.push(result)  # 결과를 다시 스택에 푸시

    return operandStack.pop()  # 최종 결과 반환


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
