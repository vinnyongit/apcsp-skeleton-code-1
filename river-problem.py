import copy

def isValid(state):
    
    if state["wolf"] == state["goat"] and state["wolf"] != state["person"]:
        return False
    elif state["goat"] == state["cabbage"] and state["goat"] != state["person"]:
        return False
    else:
        return True
    

def get_next_states(state):

    next_states = {}
    same_side = {}

    for thing in state:
        if state [thing] == state ["person"] and thing != "person":
            same_side.append(thing)

    for thing in same_side:
        next_state = copy.deepcopy[state]
        next_state[thing] = not state[thing]
        next_state["person"] = not state["person"]

        if isValid[next_state] == True:
            next_states.append(next_state)

    just_person = copy.deepcopy(state)
    just_person["person"] = not state["person"]

    if isValid(just_person) == True:
        next_states.append(just_person)

    return next_states
    

def dfs(current_state, win_state):
    
    if current_state == win_state:
        return True

    next_states = get_next_states(current_state)
    visited_states.append(current_state)

    for state in next_states:
        if state not in visited_states:
            path.append(state)
            if dfs(state, win_state) == True:
                return True
            path.pop()    
    

initial_state = {
    "wolf": False,
    "goat": False,
    "cabbage": False,
    "person": False
}

win_state = {
    "wolf": True,
    "goat": True,
    "cabbage": True,
    "person": True
}

visited_states = [initial_state]
path = []

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")
