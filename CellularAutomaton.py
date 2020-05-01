def rule_to_array(rule):
    array = list(bin(rule))
    del array[1]
    array = list(map(lambda x: int(x), array))
    for i in range(8 - len(array)):
        array.insert(0, 0)

    return array


def left_value(state, position):
    if position == 0:
        return state[-1]

    return state[position - 1]



def right_value(state, position):
    if position == 42:
        return state[0]

    return state[position + 1]



def which_rule_decimal(transition_rule, state, position):

    return 2**2*left_value(state, position) + 2**1*state[position] + 2**0*right_value(state, position)



def apply_rule(transition_rule, state, position):

    return transition_rule[-(which_rule_decimal(transition_rule, state, position) + 1)]



def print_state(state):
    for i in state:
        if i == 1:
            print("\033[7;34;40m   \033[0m", end=" ")
        else:
            print("\033[1;30;47m   \033[0m", end=" ")
    print(" ")
    print(" ")

    return



def cellular_automata(transition_rule, state, no_generations):
    next_state = [0]*43
    print_state(state)
    for i in range(no_generations - 1):
        for j in range(43):
            next_state[j] = apply_rule(transition_rule, state, j)

        state = list(next_state)
        print_state(state)

    return



initial = [0]*43
initial[21] = 1

print("Please enter the rule number:")
rule_number = int(input())

cellular_automata(rule_to_array(rule_number), initial, 100)

