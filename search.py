element_list = ["Grubodziób", 'Szczygieł', 'Pliszka', 'Czyżyk','Zięba', 'Mazurek']
bird_name = input('Please enter bird name:')
def bird_search(bird = bird_name):
    if bird in element_list:
        return True
    else:
        return False

print(bird_search())