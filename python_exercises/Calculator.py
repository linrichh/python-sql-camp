# 1- eine operation, 2 zahlen, input vom user, programm gibt ergebnis - done
# 2- mehrfachberechnungen ohne programm neu zu starten, fehlermeldungen bei falschem datentyp/div durch 0 - done
# 3- wurzel und expontialfkt - done, mehrere operationen und zahlen, menü mit optionen statt freie eingabe
# 4- gui mit tkinter, parser für ausdrücke -> punkt vor strich

# operations
addition = ["+", "plus"]
subtraction = ["-", "minus"]
multiplication = ["*", "x", "times", "mal"]
division = ["/", "durch", "divided by"]
modulo = ["%", "mod", "modulo"]
power = ["^", "hoch", "**"]
root = ["rt", "wurzel", "sqrt"]

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
        try:
            num_1 = float(input_parts[0])
            op_1 = input_parts[1]
            num_2 = float(input_parts[2])
        except ValueError:
            print("Error: can't calculate with this. try again. numbers and operators only.")
            continue


    op = "no input"
    result = "no result"

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
