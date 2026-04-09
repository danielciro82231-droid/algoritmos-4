 1. Expresiones Regulares (Regex)
🔹 Conceptos clave

Una regex es un patrón para buscar texto.

Símbolos básicos:
. → cualquier carácter
\d → dígito (0–9)
\w → letra o número
\s → espacio
^ → inicio de línea
$ → fin de línea
Cuantificadores:
* → 0 o más
+ → 1 o más
? → 0 o 1
{n} → exactamente n
{n,m} → entre n y m
Ejemplos
1. Validar un número
^\d+$

✔ Solo números

2. Validar un correo simple
^\w+@\w+\.\w+$
 Ejercicio típico

 Validar una placa tipo: ABC123

Solución:

^[A-Z]{3}\d{3}$
 Tip para parcial
Te piden: “cadena que empiece en…” → usa ^
Te piden: “que termine en…” → usa $
“solo letras” → [A-Za-z]+
🔗 2. Listas Enlazadas
🔹 Concepto

Estructura donde cada nodo apunta al siguiente.

[Dato | next] -> [Dato | next] -> null
🔹 Operaciones clave
1. Insertar al inicio
def insertar_inicio(head, valor):
    nuevo = Nodo(valor)
    nuevo.next = head
    return nuevo
2. Recorrer lista
def imprimir(head):
    actual = head
    while actual:
        print(actual.valor)
        actual = actual.next
3. Buscar elemento
def buscar(head, x):
    actual = head
    while actual:
        if actual.valor == x:
            return True
        actual = actual.next
    return False
    
     Ejercicio típico

👉 Invertir una lista enlazada

def invertir(head):
    prev = None
    actual = head

    while actual:
        siguiente = actual.next
        actual.next = prev
        prev = actual
        actual = siguiente

    return prev
 Tip para parcial
Siempre usa un puntero actual
Cuidado con perder referencias (next)
Dibuja la lista si te bloqueas
 3. Recursividad
 Concepto

Una función que se llama a sí misma.

Siempre tiene:

Caso base (cuando se detiene)
Caso recursivo
 Ejemplo clásico: factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
 Ejercicio típico

 Sumar elementos de un arreglo

def suma(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + suma(arr, n-1)
 Tip para parcial
Pregúntate:
 “¿cómo reduzco el problema?”
Encuentra SIEMPRE el caso base primero


 4. Conjuntos (Sets)
 Concepto

Colección sin elementos repetidos.

 Operaciones
A = {1,2,3}
B = {3,4,5}
Unión → A | B
Intersección → A & B
Diferencia → A - B
 Ejercicio típico

 Verificar si dos listas tienen elementos en común

def tienen_comun(a, b):
    return len(set(a) & set(b)) > 0
 Tip
Si hay duplicados → usa set
Problemas de pertenencia → in
 5. Recursividad con Memorización (DP básico)
 Problema

La recursión repite cálculos → lento

 Solución: memoización

Guardar resultados ya calculados.

 Ejemplo: Fibonacci
 Lento
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 Con memoización
memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
 Ejercicio típico

 Caminos en una cuadrícula

memo = {}

def caminos(m, n):
    if m == 1 or n == 1:
        return 1

    if (m, n) in memo:
        return memo[(m, n)]

    memo[(m, n)] = caminos(m-1, n) + caminos(m, n-1)
    return memo[(m, n)]
 Tip de parcial (CLAVE)

Si ves:

Fibonacci
caminos
combinaciones

 Usa memoización sí o sí

 Estrategia
 Si ves regex:
Identifica patrón → arma por partes
 Si ves listas:
Dibuja nodos
Usa punteros
 Si ves recursión:
Define caso base primero
 Si ves repetición de cálculos:
Usa memoización
 Mini simulacro
1. Regex

 Validar número de celular (10 dígitos)

^\d{10}$
2. Lista enlazada

 Contar nodos

def contar(head):
    if not head:
        return 0
    return 1 + contar(head.next)
3. Recursividad

 Potencia

def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b-1)
4. Memoización

 Escaleras (puedes subir 1 o 2 pasos)

memo = {}

def formas(n):
    if n <= 2:
        return n

    if n in memo:
        return memo[n]

    memo[n] = formas(n-1) + formas(n-2)
    return memo[n]
 Último consejo (muy importante)
