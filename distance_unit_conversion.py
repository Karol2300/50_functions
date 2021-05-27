distance_units_ls = {'milimeters': 1000,
                     'centimeters': 100,
                     'meters': 1,
                     'kilometers': 1000,
                     'miles': 1609,
                     'nautical miles': 1852}

unit_convertet = str(input(f"Please input unit that you want to convert {distance_units_ls.keys()}:"))
units_value = float(input(f"Please input number of units that you want to convert :"))
target_unit = str(input(f"Please input your target unit {distance_units_ls.keys()}:"))

def conversion(converted = unit_convertet, value = units_value, target = target_unit ):
    if (converted == 'milimeters' or converted == 'centimeters') and (target == "meters" or target == "kilometers" or target == "miles" or target == "nautical miles"):
        target_value = round((1/distance_units_ls[converted]) * value / distance_units_ls[target], 2)
        return target_value

    elif (converted == 'nautical miles' or converted == 'miles'or converted == 'kilometers') and (target == "milimeters" or target == 'centimeters' or target == 'meters'):
        target_value = round((distance_units_ls[converted] * distance_units_ls[target]) * value, 2)
        return target_value
    else:
        target_value = round((distance_units_ls[converted] / distance_units_ls[target]) * value, 2)
        return target_value


print(conversion())