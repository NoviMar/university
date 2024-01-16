LEFT_A = 'A'
RIGHT_A = 'A'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
MARKER = 'X'


def q0(bracket_sequence, index):
    if bracket_sequence[index] == CLOSE_BRACKET:
        bracket_sequence[index] = MARKER
        return 'q1', index - 1
    elif bracket_sequence[index] == RIGHT_A:
        return 'q2', index - 1
    else:
        return 'q0', index + 1
    
def q1(bracket_sequence, index):
    if bracket_sequence[index] == OPEN_BRACKET:
        bracket_sequence[index] = MARKER
        return 'q0', index + 1
    elif bracket_sequence[index] == LEFT_A:
        print("0")
        return 'stop', None
    else:
        return 'q1', index - 1
    
def q2(bracket_sequence, index):
    if bracket_sequence[index] == OPEN_BRACKET:
        print("0")
        return 'stop', None
    elif bracket_sequence[index] == LEFT_A:
        print("1")
        return 'stop', None
    else:
        return 'q2', index - 1
    
def evaluate_expression(expression):
    bracket_sequence = [LEFT_A] + list(expression) + [RIGHT_A]
    index = 1
    state = 'q0'
    while state != 'stop':
        state, index = eval(state)(bracket_sequence, index)


string = input('Введите скобочную последовательность: ')