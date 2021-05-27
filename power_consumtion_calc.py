home_equipment_num = int(input("How many household products do you want to calculate ?: "))
price_energy = float(input("Please provide energy price fo 1 Kwh ?: "))

def power_consumption_cost(equip_num = home_equipment_num, price = price_energy):
    home_equipment_ls = []

    for equip in range(1, equip_num +1):
        print(f"Please provide following info: name, labeled power consumption in Watts, how long it works during a day for equipment number {equip}")
        equipment_param = (input("equipment name: "), float(input("energy consumption in watts: ")), float(input("average daily work duration of equipment in hours: ")))
        home_equipment_ls.append(equipment_param)


    for equip in range(0, equip_num):
        daily_result = f"Your {home_equipment_ls[equip][0]} daily consumes {round((home_equipment_ls[equip][1] * home_equipment_ls[equip][2])/1000,2)} of Kwh"
        daily_result_price = f"Daily cost of your {home_equipment_ls[equip][0]} is: {(round((home_equipment_ls[equip][1] * home_equipment_ls[equip][2])/1000,2)) * price}"
        yearly_result = f"Your {home_equipment_ls[equip][0]} yearly consumes {round((home_equipment_ls[equip][1] * home_equipment_ls[equip][2])/1000,2)*360} of Kwh"
        yearly_result_price = f"Yearly cost of your {home_equipment_ls[equip][0]} is: {(round((home_equipment_ls[equip][1] * home_equipment_ls[equip][2])/1000,2)*360) * price}"
        print(daily_result,".", daily_result_price)
        print(yearly_result,".", yearly_result_price)
        print('---------------------------------------------------------------------------------')

    return daily_result, yearly_result, daily_result_price, yearly_result_price

power_consumption_cost()


