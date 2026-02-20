#1503
#caso base
def suma_Digito(n):
    if n == 0:
        return 0
    else:
        return (n%10)+suma_Digito(n//10)   
        

print(suma_Digito(15033))        

