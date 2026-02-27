# Simulator file for question 1.
# Complete implementation of a universal RAM simulator.

from collections import defaultdict

variableList = []

# defaultdict returns 0 for undefined memory cells
memory = defaultdict(int)


# Creates the variable list and the memory dictionary.
# Initializes:
#   var 0 = input_len
#   memory[0..] = input array
def setupEnv(programArr, inputArr):
    variableList.clear()
    memory.clear()

    # create variables initialized to 0
    for i in range(programArr[0]):
        variableList.append(0)

    # variable 0 = input length
    variableList[0] = len(inputArr)

    # load input into memory
    for i in range(len(inputArr)):
        memory[i] = inputArr[i]


# Runs the given RAM program on the input.
def executeProgram(programArr, inputArr):

    setupEnv(programArr, inputArr)

    # remove first element (number of variables)
    programArr = programArr[1:]

    programCounter = 0

    while programCounter < len(programArr):

        cmd = programArr[programCounter][0]
        ops = programArr[programCounter][1:]

        # Assignment commands

        if cmd == "read":
            # ['read', i, j]
            # var_i = M[var_j]
            variableList[ops[0]] = memory[variableList[ops[1]]]

        if cmd == "write":
            # ['write', i, j]
            # M[var_i] = var_j
            memory[variableList[ops[0]]] = variableList[ops[1]]

        if cmd == "assign":
            # ['assign', i, j]
            # var_i = constant j
            variableList[ops[0]] = ops[1]

        # Arithmetic commands

        if cmd == "+":
            # ['+', i, j, k]
            # var_i = var_j + var_k
            variableList[ops[0]] = variableList[ops[1]] + variableList[ops[2]]

        if cmd == "-":
            # ['-', i, j, k]
            # var_i = max(var_j - var_k, 0)
            variableList[ops[0]] = max(
                variableList[ops[1]] - variableList[ops[2]],
                0
            )

        if cmd == "*":
            # ['*', i, j, k]
            # var_i = var_j * var_k
            variableList[ops[0]] = variableList[ops[1]] * variableList[ops[2]]

        if cmd == "/":
            # ['/', i, j, k]
            # var_i = var_j // var_k
            # division by 0 → 0
            if variableList[ops[2]] == 0:
                variableList[ops[0]] = 0
            else:
                variableList[ops[0]] = (
                    variableList[ops[1]] // variableList[ops[2]]
                )

        # Control command

        if cmd == "goto":
            # ['goto', i, j]
            # if var_i == 0 → jump to line j
            if variableList[ops[0]] == 0:
                programCounter = ops[1]
                continue

        # move to next instruction
        programCounter += 1


    output_ptr = variableList[1]
    output_len = variableList[2]

    return [
        memory[i]
        for i in range(output_ptr, output_ptr + output_len)
    ]
