from random import randint

sales_quantity = randint(1, 100)
print(sales_quantity)

def sales_change(sales_quantity = sales_quantity):
    sales_value = []
    sales_change_ls = []

    for sale in range(0, sales_quantity):
        sales_value.append(randint(20, 80))
    print(sales_value)

    for element in range(1, sales_quantity):
        sales_change = f"{round((sales_value[element] - sales_value[element-1])/sales_value[element-1]* 100, 2)}%"
        sales_change_ls.append(sales_change)
    print(len(sales_change_ls))
    print(sales_change_ls)
    return sales_change



sales_change()