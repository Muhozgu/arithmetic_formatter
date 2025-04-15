def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        left, operator, right = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2

        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        dashes.append('-' * width)

        if display_answers:
            if operator == '+':
                result = str(int(left) + int(right))
            else:
                result = str(int(left) - int(right))
            results.append(result.rjust(width))

    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)

    if display_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))