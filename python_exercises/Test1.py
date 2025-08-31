# 1- eine operation, 2 zahlen, input vom user, programm gibt ergebnis - done
# 2- mehrfachberechnungen ohne programm neu zu starten, fehlermeldungen bei falschem datentyp/div durch 0 - done
# 3- wurzel und expontialfkt - done, mehrere operationen und zahlen, menü mit optionen statt freie eingabe
# 4- gui mit tkinter, parser für ausdrücke -> punkt vor strich

# operations
operators = {
    "addition": ["+", "plus"],
    "subtraction": ["-", "minus"],
    "multiplication": ["*", "x", "times", "mal"],
    "division": ["/", "durch", "divided by"],
    "modulo": ["%", "mod", "modulo"],
    "power": ["^", "hoch", "**"],
    "root": ["rt", "wurzel", "sqrt"],
}
brackets = ["(", ")"]


def is_number(input_part):
    try:
        float(input_part)
        return True
    except ValueError:
        return False


def is_op(input_part):
    if input_part in operators:
        return True
    else:
        return False


def get_op(input_part):
    for op_type, syns in operators.items():
        if input_part in syns:
            return op_type
    return None


# inputs
status = True
while status:
    input_whole = input("Type \"exit\" to stop calculator. What should i calculate?: ")
    if input_whole == "exit":
        status = False
        print("Calculator closed.")
        break
    else:
        input_parts = input_whole.split()
        count_parts = len(input_parts)

        numbers = []
        ops = []

        try:
            if is_number(input_parts[0]):
                numbers.append(float(input_parts[0]))
            else:
                print("Error: Needs to start with a number. Try again.")

            i = 1
            while i <= count_parts:
                if is_number(input_parts[i]):
                    numbers.append(float(input_parts[i]))
                    i += 1
                elif is_op(input_parts[i]):
                    ops.append(get_op(input_parts[i]))
                    i += 1
                else:
                    print("Error. Please use numbers or operators.")
                    continue

        except ValueError:
            print("Error: can't calculate with this. try again. numbers and operators only.")
            continue

"""
    if op_1 in addition:
        op = " + "
        result = str(num_1 + num_2)

    elif op_1 in subtraction:
        op = " - "
        result = str(num_1 - num_2)

    elif op_1 in multiplication:
        op = " * "
        result = str(num_1 * num_2)

    elif op_1 in division:
        try:
            op = " / "
            result = str(num_1 / num_2)
        except ZeroDivisionError:
            print("Error: Division through Zero not possible.")
            continue

    elif op_1 in modulo:
        op = " mod "
        result = str(num_1 % num_2)

    elif op_1 in power:
        op = "^"
        result = str(num_1 ** num_2)

    elif op_1 in root:
        try:
            op = "√"
            result = str(num_2 ** (1 / num_1))
        except ZeroDivisionError:
            print("Error: The 0th root is not defined. Try again.")
            continue

    else:
        print("Error: Invalid operator. Calculation not possible.")
        continue

    print("Result: " + str(num_1) + op + str(num_2) + " = " + result)
"""
