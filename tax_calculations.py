def tax_calculations(gross_salary, children):
    if gross_salary < 1000:
        tax = 0.10
    elif gross_salary < 2000:
        tax = 0.12
    elif gross_salary < 4000:
        tax = 0.14
    else:
        tax = 0.18

    if gross_salary < 2000:
        tax -= children * 0.01
    else:
        tax -= children * 0.005

    net_salary = gross_salary - (gross_salary * tax)
    return net_salary

while True:
    try:
        gross_salary = int(input("What is your salary? "))
        children = int(input("How many children do you have? "))
        break
    except ValueError:
        print("Both values must be integers, try again")

print(f"Your net salary is: {tax_calculations(gross_salary, children)}")



