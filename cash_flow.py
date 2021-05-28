from random import randint

cash_flow_size = randint(10, 100)
cash_flow_val_min = -100
cash_flow_val_max = 100

cash_flow_val_ls = []
cash_flow_num_ls = []

def cash_flow_generator():

    for element in range(1, cash_flow_size):
        cash_flow_val_ls.append(randint(cash_flow_val_min, cash_flow_val_max))
        cash_flow_num_ls.append(element)
    print(cash_flow_val_ls)
    print(cash_flow_num_ls)
    return cash_flow_val_ls
cash_flow_generator()


def dcf(val = cash_flow_val_ls, period = cash_flow_num_ls):
    dcf_ele_value_ls = []
    r = float(input("Please input discount rate:"))
    for element in range(1, cash_flow_size):
        dcf_ele_value = round(val[element-1]/((1+r) ** period[element-1]),0)
        dcf_ele_value_ls.append(dcf_ele_value)

    dcf_ele_value_sum = sum(dcf_ele_value_ls)
    print(dcf_ele_value_ls)
    print(dcf_ele_value_sum)


dcf()


