def validar(isbn):
    isbn = list(isbn.replace('-', ''))

    if len(isbn) > 10:
        return False

    if isbn[0] == 'X':
        isbn[0] = '10'

    res = 0
    for i in range(10):
        try:
            res += int(isbn[i])*(10-i)
        except ValueError:
            return False

    if res % 11 == 0:
        print("Código válido.")
    else:
        print("Código erroneo.")
    return res


code = "3-598-21508-8"
validar(code)
