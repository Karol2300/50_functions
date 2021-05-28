from random import randint


invest_value = randint(100, 1000)
cash_flow_ls = []
cash_flow_num_ls = []

def future_value_s():
    r = float(input("Please input interest rate:"))
    t = int(input("Please input investment period:"))
    cap_value = round(invest_value * (1 + (r * t)), 2)
    print(invest_value)
    print(t)
    print(cap_value)


future_value_s()

def future_value_m():
    r = float(input("Please input interest rate:"))
    t = int(input("Please input investment period:"))
    cap_num = int(input("Please input capitalization number:"))
    cap_value = round(invest_value * ((1 + (r/cap_num)) ** (t * cap_num)), 2)
    print(invest_value)
    print(t)
    print(cap_value)


future_value_m()

def future_value_c():
    r = float(input("Please input interest rate:"))
    t = int(input("Please input invest period:"))
    cap_value = round(invest_value * ((2.71828182)**(t*r)) ,2)
    print(invest_value)
    print(t)
    print(cap_value)

future_value_c()

