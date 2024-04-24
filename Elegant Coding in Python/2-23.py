def tanzania(amount):
    calculate_tax = 0.5
    return calculate_tax * amount


def zambia(amount):
    calculate_tax = 0.7
    return calculate_tax * amount


def eritrea(amount):
    calculate_tax = 1
    return calculate_tax * amount


contry_tax_calculate = {
    'tanzania': tanzania,
    'zambia': zambia,
    'eritrea': eritrea
}


def calculate_tax(contry_name, amount):
    return contry_tax_calculate[contry_name](amount)


print(calculate_tax('tanzania', 100))
