
def is_divisible_by_4 (number):
    return number % 4 == 0


print(is_divisible_by_4(12))

board_size = 99


def chessboard(n = board_size):
    full_mark ="# "
    rev_full_mark = " #"
    half_mark_1 = " "
    half_mark_2 = "#"

    if n % 2 == 0:
        for i in range(0, n):
            if i % 2 == 0:
                print(int(n/2) * full_mark)
            else:
                print(int(n / 2) * rev_full_mark)
    else:
        for i in range(0, n):
            if i % 2 == 0:
                print((int((n-1) / 2) * full_mark) + half_mark_2)
            else:
                print((int((n-1) / 2) * rev_full_mark) + half_mark_1)


chessboard()

def format_date(day, month, year):
    days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31)
    months = { 1 : 'stycznia',
               2 : 'lutego',
               3 : 'marca',
               4 : 'kwietnia',
               5 : 'maja',
               6 : 'czerwca',
               7 : 'lipca',
               8 : 'sierpnia',
               9 : 'września',
              10 :'października',
              11 :'listopada',
              12 :'grudnia'}

    if year > 0:
        if month in months.keys():
            if (day > 0 and day <= days_in_months[month-1]):
                print(day, months[month], year)

            else:
                return print(None)
                # print('Fault, check day number')
        else:
            return print(None)
            # print('Fault, check month number')
    else:
        return print(None)
        # print('Fault, check year number')

format_date(12, 10, 2020)

the_sentence = 'Java is the best, but PHP is the bestest'


def censor(sentence = the_sentence):
    forbidden_list = ["Java", "C#", "Ruby","PHP"]
    sliced_sentence = list(sentence.split())

    for x in range(0, len(sliced_sentence)):
            if sliced_sentence[x-1] in forbidden_list:
                sliced_sentence[x-1] = "****"
            else:
                pass
    string_sentence =" "
    return print((string_sentence.join(sliced_sentence)))



censor()

def convert_to_usd(zlotys):
    return(round(zlotys / 3.85,2))




# poniższe linijki przetestują Twoją funkcję:
print("385PLN = ", convert_to_usd(385), "USD")
print("100PLN = ", convert_to_usd(100), "USD")

gross = 1000
vat = 0.23

def calculate_net(gross = gross, vat = vat):
    return(round(gross/(1 + vat),2))

print(calculate_net())

temp = 15


def check_type():
    if type(temp) == int:
        result = temp * 5
        return print(result)

    elif type(temp) == float:
        result = temp / 5
        return print(result)

    elif type(temp) == str:
        return print(temp)

    else:
        return


check_type()

fib_lenght = 20


def fib(n=fib_lenght):
    fibonacci_ls_fin = []

    if n == 1:
        fibonacci_ls_fin.append(0)

    elif n == 2:
        fibonacci_ls_fin.append(0)
        fibonacci_ls_fin.append(1)

    elif n > 2:
        fibonacci_ls_fin.append(0)
        fibonacci_ls_fin.append(1)
        for i in range(2, n):
            fibonacci_ls_fin.append(fibonacci_ls_fin[i - 2] + fibonacci_ls_fin[i - 1])


    print(fibonacci_ls_fin[n-1])


fib()