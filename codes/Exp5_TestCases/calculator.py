# calculator.py - Simple Calculator per lab manual specification
def _num(x):
    if isinstance(x, bool):
        raise ValueError
    if isinstance(x, (int, float)):
        return x
    return float(x) if '.' in str(x) else int(x)   # raises ValueError for 'abc'

def calculate(a, op, b):
    try:
        a, b = _num(a), _num(b)
    except (ValueError, TypeError):
        return 'Error: Invalid input'
    if op == '+':   r = a + b
    elif op == '-': r = a - b
    elif op in ('*', 'x', '×'): r = a * b
    elif op in ('/', '÷'):
        if b == 0:
            return 'Error: Division by zero'
        r = a / b
    else:
        return 'Error: Invalid operator'
    if isinstance(r, float):
        r = round(r, 6)
        if r.is_integer() and op not in ('/', '÷') and not (isinstance(a, float) or isinstance(b, float)):
            r = int(r)
    return r

if __name__ == '__main__':
    while True:
        s = input('Enter A op B (e.g. 10 / 3) or q: ').split()
        if s[:1] == ['q']: break
        if len(s) != 3: print('Error: Invalid input'); continue
        print(calculate(s[0], s[1], s[2]))
