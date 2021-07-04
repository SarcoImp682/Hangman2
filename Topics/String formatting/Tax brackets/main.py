income = int(input())
if 0 <= income <= 15527:
    calc = 0
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
    calc = 0.15
elif 42708 <= income <= 132406:
    percent = 25
    calc = 0.25
else:
    percent = 28
    calc = 0.28
calculated_tax = income * calc
print(f"The tax for {income} is {percent}%. That is {round(calculated_tax)} dollars!")