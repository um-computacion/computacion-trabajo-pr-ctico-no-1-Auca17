valores = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def decimal_to_roman(decimal) -> str: 
    if not 1 <= decimal <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999")

    resultado = []
    resto = decimal

    for valor, simbolo in valores:
        cuenta, resto = divmod(resto, valor)
        resultado.append(simbolo * cuenta)
        if resto == 0:
            break
    return "".join(resultado)

if __name__ == "__main__":
    print(decimal_to_roman(int(input("Ingrese número para probar: "))))