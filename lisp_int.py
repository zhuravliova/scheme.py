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


def sub(minuend, *args):
    return -minuend if len(args) == 0 else minuend - sum(args)


def mul(*args):
    result = 1
    for item in args:
        result = result * item
    return result


def division(dividend, *args):
    if len(args) == 0:
        return 1 / dividend
    else:
        for item in args:
            dividend = dividend / item
        return dividend


ENV = {
    '+': lambda *args: sum(args),
    '-': sub,
    '*': mul,
    '/': division,
}


def evaluate(expression):
    fn = ENV[expression[0]]
    operands = []
    for exp in expression[1:]:
        if isinstance(exp, list):
            operands.append(evaluate(exp))
        else:
            operands.append(exp)
    return fn(*operands)
