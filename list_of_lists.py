name = ['ThinkPad x220', 'HP Probook xse12', 'Fujitsu Lifebook']
manufacturer_name = ['Lenovo', 'Hewlett Packard', 'Fujitsu Siemens']
country = ['China', 'USA', 'Japan']
category = ['Notebook','Notebook','Notebook']
price_category = ['Premium', 'Mid range', 'Premium']

def list_of_lists(name = name, manufacturer = manufacturer_name, country = country, prod_cat = category, price_cat = price_category):
    product_specs_ls = list(zip(name, manufacturer, country, prod_cat, price_cat))
    return product_specs_ls


print(list_of_lists())


def list_of_lists_unpacking(ls = list_of_lists()):
    ls_lenght = len(ls[0])
    for element in range(0, ls_lenght):
        splitted_list = [item[element].split(",") for item in ls]
        print(splitted_list)
    return splitted_list


list_of_lists_unpacking()