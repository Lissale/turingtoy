from typing import (
        Dict,
        List,
        Optional,
        Tuple,
)

import poetry_version

__version__ = poetry_version.exctract(source_files=__file)

def run_turing_machine(
    machine: Dict,
    input_: str,
    steps: Optional[int] = None,
) -> Tuple[str, List, bool]:

    state = machine["start state"]
    blank = machine["blank"]
    table = machine["table"]
    input_ = blank + input_
    i = 1

    execution_history = []

    while state not in machine["final states"]: #Lecture...

        if i < 0 or i >= len(input_):
            reading = blank
        else:
            reading = input_[i]

        historik = {"state": state, "reading": reading, "position": i, "memory": input_}

        action = table[state][reading] #Action à effectuer

        #Déplacement simple
        if action == "L":
            i -= 1
        elif action == "R":
            i += 1

        if isinstance(action, dict) and "write" in action.keys(): #Execution
            if i<0:
                input_ = action["write"] + input_
            else:
                input_ = input_[:i] + action["write"] + input_[i+1:]

        if isinstance(action, dict) and "R" in action.keys():
            i+=1
            state = action["R"]
        elif isinstance(action, dict) and "L" in action.keys():
            i-=1
            state = action["L"]

        historik["transition"] = state
        execution_history.append(historik)

    input_ = input_.strip(blank)
    return input_, execution_history, True
