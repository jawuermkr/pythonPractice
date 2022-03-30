
def codifica(palabra):
    result = ''
    count = 1
    for k in range(0, len(palabra)-1):
        if k < len(palabra):
            if palabra[k] == palabra[k+1]:
                count += 1
            else:
                # Concatenation with the palabra counting new letter
                if count == 1:
                    result = result + f'{palabra[k]}'
                else:
                    result = result + f'{count}{palabra[k]}'
                count = 1
        else:
            if count == 1:
                result = result + f'{palabra[k]}'
            else:
                result = result + f'{count}{palabra[k]}'

    return result


palabra = "stttaaarrt"
coded = codifica(palabra)
print(coded)
