data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

entrada = str(input())


def paices(entrada):
    if(entrada in data):
        print(data[entrada])
    else:
        print("Not found")


paices(entrada)
