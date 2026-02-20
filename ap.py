def suma_lista(lista, acumulador=0 ):
    if len(lista) == 0:
        return 0
return suma_lista[1:] + lista([0] + acumulador)       


def potencia(base, exp):
    if exp == 0:
       return 1
return base * potencia(base, exp - 1)    

def potencia_tail(base, exp, acumulador=1):
    if exp == 0:
        return acumulador
    return potencia_tail(base., expo -1, base * acumulador)    
