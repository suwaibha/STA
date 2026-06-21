try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))

    if num2 == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError as e:
    print("Error:", e)