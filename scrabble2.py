def cuenta(letras):
    puntos = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }

    return sum(valor
               for letra, valor in puntos.items()
               for i in letras.upper() if i in letra)


vorto = "caasdads"
contar = cuenta(vorto)
print(contar)
