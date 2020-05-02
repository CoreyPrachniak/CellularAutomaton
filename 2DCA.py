import numpy as np
import time


def entry_retrieve(state, position, movement):
    x, y = position
    x_movement, y_movement = movement

    x_max = len(state[:][0]) - 1
    y_max = len(state[0]) - 1

    x_entry = -1 if x + x_movement < 0 else 0 if x + x_movement > x_max else x + x_movement
    y_entry = -1 if y + y_movement < 0 else 0 if y + y_movement > y_max else y + y_movement

    return state[x_entry][y_entry]


def live_neighbors_count(state, position):
    x, y = position
    counter = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i, j) != (0, 0):
                if entry_retrieve(state, position, (i, j)) == 1:
                    counter += 1

    return counter


def apply_rule(state, position):
    x, y = position
    current_state = state[x][y]
    live_count = live_neighbors_count(state, position)

    if current_state == 0:
        if live_count == 3:
            return 1
        else:
            return 0
    else:
        if live_count in [2, 3]:
            return 1
        else:
            return 0


def print_state(state):
    state_width = len(state[:][0])
    state_height = len(state[0])

    for y in range(state_height):
        for x in range(state_width):
            if state[x][-(y + 1)] == 1:
                print("\033[7;34;40m  \033[0m", end="  ")
            else:
                print("  ", end="  ")
        print(" ")
        print(" ")

    return


def game_of_life(state, no_generations, sleep_time):
    state_width = len(state[:][0])
    state_height = len(state[0])
    next_state = np.zeros((state_width, state_height))
    print_state(state)

    for i in range(no_generations - 1):
        for x in range(state_width):
            for y in range(state_height):
                next_state[x][y] = apply_rule(state, (x, y))

        state = np.array(next_state)
        time.sleep(sleep_time)
        print_state(state)
        print(" ")


initial_state = np.random.randint(2, size = (25, 25))


game_of_life(initial_state, 100, 0.25)