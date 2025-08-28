# 1- eine operation, 2 zahlen, input vom user, programm gibt ergebnis
# 2- mehrfachberechnungen ohne programm neu zu starten, fehlermeldungen bei falschem datentyp/div durch 0
# 3- wurzel und expontialfkt, mehrere operationen und zahlen, menü mit optionen statt freie eingabe
# 4- gui mit tkinter, parser für ausdrücke -> punkt vor strich
import sys

# operations
addition = ["+", "plus"]
subtraction = ["-", "minus"]
multiplication = ["*", "x", "times", "mal"]
division = ["/", "durch", "divided by"]
modulo = ["%", "mod", "modulo"]

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
        num_1 = input_parts[0]
        op_1 = input_parts[1]
        num_2 = input_parts[2]

    op = "no input"
    result = "no result"

    if op_1 in addition:
        op = " + "
        result = str(float(num_1) + float(num_2))

    elif op_1 in subtraction:
        op = " - "
        result = str(float(num_1) - float(num_2))

    elif op_1 in multiplication:
        op = " * "
        result = str(float(num_1) * float(num_2))

    elif op_1 in division:
        try:
            op = " / "
            result = str(float(num_1) / float(num_2))
        except ZeroDivisionError:
            print("Division through Zero not possible.")
            continue

    elif op_1 in modulo:
        op = " mod "
        result = str(float(num_1) % float(num_2))

    else:
        print("Invalid operator. Calculation not possible.")
        continue

    print("Result: " + num_1 + op + num_2 + " = " + result)
