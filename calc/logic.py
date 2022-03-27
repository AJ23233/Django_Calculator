

def performoperation(operator, preOperand, postOperand):
    if postOperand == '':
        return preOperand
    side1 = int(preOperand)
    side2 = int(postOperand)

    switcher = {
        '+': side1 + side2,
        '-': side1 - side2,
        '*': side1 * side2,
        '/': side1 / side2
    }

    func = switcher.get(operator, lambda: 'Invalid operation')
    return str(func)


def isoperator(operator):

    for i in range(10):
        if str(i) == operator:
            return False

    a = ['+', '-', '*', '/']

    for i in a :
        if operator == i:
            return True

    raise Exception("invalid input")

def calculate(x):

    # The expression can be solved using in-build eval function of math module as well
    # y= eval(x)
    # return y
    y = list(x)
    i = 0
    preOperand = ''
    postOperand = ''
    isPreOp = True
    operator = ''
    try:
        while i < len(y):

            if isoperator(y[i]):

                 if isPreOp:
                     isPreOp=False
                 else:
                     preOperand = performoperation(operator, preOperand, postOperand)
                     postOperand = ''

                 operator = y[i]

            else :
                if isPreOp:
                    preOperand += y[i]
                else:
                    postOperand += y[i]
            i += 1

        preOperand = performoperation(operator, preOperand, postOperand)

    except Exception:
        preOperand = 'Invalid Operation'

    return preOperand