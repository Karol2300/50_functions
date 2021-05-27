from random import randint

sales_quantity = randint(1, 100)
print(sales_quantity)

def sales_share(sales_quantity = sales_quantity):
    sales_value = []
    sales_share_ls = []

    for sale in range(0, sales_quantity):
        sales_value.append(randint(20, 80))

    sales_value_sum = sum(sales_value)
    for element in range(0, (sales_quantity)):
        sales_shares = f"{round((sales_value[element] / sales_value_sum) * 100, 2)}%"
        sales_share_ls.append(sales_shares)
    print(len(sales_share_ls))
    print(sales_share_ls)



sales_share()