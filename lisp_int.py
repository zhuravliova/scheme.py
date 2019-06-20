lisp1 = r"(+ 2 (* 2 (* 4 (/ 8 2))))"
lisp2 = r"(define (size 2))"

def calc(expression):
    operands = expression[1:-1].split(' ')
    if operands[0] == '+':
        return int(operands[1]) + int(operands[2])
    elif operands[0] == '-':
        return int(operands[1]) - int(operands[2])
    elif operands[0] == '*':
        return int(operands[1]) * int(operands[2])
    elif operands[0] == '/':
        return int(int(operands[1]) / int(operands[2]))
    elif operands[0] == 'define':
#        operands[1][1:] + ' = '
 #       eval(operands[1][1:] + ' = ' +  operands[2][:-1])
        exec(operands[1][1:] + ' = ' + operands[2][:-1])
        var = operands[2][:-1]
        if exec(" " + operands[1][1:] + """ == var"""):
            return var


def unpack(lisp):
    while lisp.count('(') != 1:
        inside_oper = lisp[int(lisp.rfind('(')): 1 + int(lisp.find(')', lisp.rfind('(')))]   #вичісление внутр операнда
        new = lisp[0: int(lisp.rfind('('))] + str(calc(inside_oper)) + lisp[1 + int(lisp.find(')', lisp.rfind('('))):]  #поменять процесс удаления лишних )))))
        return unpack(new)
    else:
        return calc(lisp)


print(unpack(lisp1))

print(calc(lisp2))


