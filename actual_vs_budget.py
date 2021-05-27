from random import randint

elements_name = ["Apple", "Banana", "Peach", "Mineral Water", "Bread", "Sweets", "Ice Cream", "Carrot", "Potato", "Mustard"]
num_of_elements = len(elements_name)


def actual_vs_budget(num_of_elements = num_of_elements):
    element_number = []
    element_budget_value = []
    element_actual_value = []
    element_value_diff = []
    element_percentage_diff = []


    for element in range(0, num_of_elements):
        element_number.append(element)
        element_budget_value.append(randint(1, 100))
        element_actual_value.append(randint(0, 400))
        element_value_diff.append(round(element_actual_value[element] - element_budget_value[element],1))
        element_percentage_diff.append(f"{round(element_value_diff[element] / element_budget_value[element] * 100, 1)} %")
        element_data = list(zip(elements_name, element_budget_value, element_actual_value, element_value_diff, element_percentage_diff))
    headings = ["en", "ebv", "eav", "evd", "epd"]
    print(headings)
    for element in range(0, len(element_data)):
        print(element_data[element])

actual_vs_budget()

