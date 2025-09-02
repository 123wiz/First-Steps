import re

def arithmetic_arranger(problems, solve=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first = []
    second = []
    lines = []
    results = []

    for problem in problems:
        if re.search("[^\s0-9+-]", problem):  # only digits, spaces, +, -
            if "/" in problem or "*" in problem:
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber, operator, secondNumber = problem.split()

        if len(firstNumber) > 4 or len(secondNumber) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = str(int(firstNumber) + int(secondNumber))
        else:
            result = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = firstNumber.rjust(length)
        bottom = operator + secondNumber.rjust(length - 1)
        line = "-" * length
        res = result.rjust(length)

        first.append(top)
        second.append(bottom)
        lines.append(line)
        results.append(res)

    arranged_problems = "    ".join(first) + "\n" + "    ".join(second) + "\n" + "    ".join(lines)
    if solve:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems
