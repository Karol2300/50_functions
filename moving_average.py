from random import randint
mov_average_period = 4
element_num = randint(mov_average_period, 20)
element_base_val = randint(10, 20)


def moving_average(period = mov_average_period, base_val = element_base_val, element_number = element_num):
    element_no_ls = []
    element_value_ls = []
    moving_average_ls = []
    for element in range(0, period-1):
        moving_average_ls.append("xx")

    for element in range(0, element_number):
        element_var = randint(-10, 10)/10
        element_value = round(base_val * element_var, 2)
        element_value_ls.append(element_value)
        element_no_ls.append(element)
    print(element_value_ls)

    for element in range(0, (element_number - period + 1)):
        moving_avg = round(sum(element_value_ls[element:element+period])/period, 2)
        moving_average_ls.append(moving_avg)
    print(moving_average_ls)


moving_average()