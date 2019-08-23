src = r"(+ 2 (* 2 (* (+ 4 1) (/ 8 2))))"
lisp2 = r"(define (size 2))"


def parse(src):
    src = str(src.replace('(', ' ( ').replace(')', ' ) '))
    tokens = src.split()
    while '(' in tokens or ')' in tokens:
        open_paren = len(tokens) - tokens[-1::-1].index('(') - 1
        close_paren = tokens.index(')', open_paren)
        internal_seq = convert(tokens[open_paren + 1:close_paren])
        tokens = tokens[:open_paren] + [internal_seq] + tokens[close_paren + 1:]
    return tokens[0]


def convert(seq):
    res = []
    for item in seq:
        try:
            try:
                res.append(int(item))
            except ValueError:
                res.append(float(item))
        except (ValueError, TypeError):
            res.append(item)
    return res


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
