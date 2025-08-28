# 1- eine operation, 2 zahlen, input vom user, programm gibt ergebnis
# 2- mehrfachberechnungen ohne programm neu zu starten, fehlermeldungen bei falschem datentyp/div durch 0
# 3- wurzel und expontialfkt, mehrere operationen und zahlen, menü mit optionen statt freie eingabe
# 4- gui mit tkinter, parser für ausdrücke -> punkt vor strich

# operations
addition = ["+", "plus"]
subtraction = ["-", "minus"]
multiplication = ["*", "x", "times", "mal"]
division = ["/", "durch", "divided by"]
modulo = ["%", "mod"]

# inputs
input_whole = input(print("What should i calculate?: "))
input_parts = input_whole.split()
num_1 = input_parts[0]
op_1 = input_parts[1]
num_2 = input_parts[2]

op = "no input"
result = "no result"

if op_1 in addition:
    op = " + "
    result = str(float(num_1) + float(num_2))

if op_1 in subtraction:
    op = " - "
    result = str(float(num_1) - float(num_2))

if op_1 in multiplication:
    op = " * "
    result = str(float(num_1) * float(num_2))

if op_1 in division:
    op = " / "
    result = str(float(num_1) / float(num_2))

if op_1 in modulo:
    op = " % "
    result = str(float(num_1) % float(num_2))

print("Result: " + num_1 + op + num_2 + " = " + result)
