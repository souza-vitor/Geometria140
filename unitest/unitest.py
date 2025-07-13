def calcular_cubo(aresta):
    if aresta <= 0:
        raise ValueError("A aresta precisa ser um numero positivo.")
    else:
        return 6 * aresta * aresta

def calcular_paralelogramo(base, altura):
    return base * altura

def calcular_piramide(base, apotema):
    if base <= 0 or apotema <= 0:
        raise ValueError('A base e a apotema precisa ser um numero positivo.')
    else:
        area_base = base * base
        area_apotema = (base * apotema) / 2
        alateral = 4 * area_apotema
        
        return area_base + alateral 