1. EXPRESIONES REGULARES
expresion de Correo electrónico
Opciones:

a) ^\w+@\w+.\w+$ 
b) ^.\d+.@.*.[a-z]{2,4}$ 
c) ^[\w-]+(.[\w-]+)*@([\w-]+.)+[a-zA-Z]{2,7}$ correcta
d) ^\d+@\w+.\w+$ 

 Análisis
  a)
El . no está escapado → significa “cualquier carácter”
Podría aceptar cosas inválidas como usuario@dominioXcom
 b)
Empieza con cualquier carácter (.)
Exige números → no sirve para correos normales
 d)
^\d+ → solo números al inicio ❌
Un correo no es solo números
 c) (CORRECTA)
^[\w-]+(.[\w-]+)*@([\w-]+.)+[a-zA-Z]{2,7}$

✔ Permite:

usuario con letras, números, guiones
subdominios
dominio válido

 Teléfono: +57 300 1234567
Opciones:

a) ^\d{2} \d{3} \d{7}$ 
b) ^+\d{2} \d{3} \d{7}$ 
c) ^+\d{1,3} \d{3} \d{4,7}$ 
d) ^+57 \d{3} \d{7}$  (casi)


La correcta sería:

^\+57 \d{3} \d{7}$
 
 2. RECURSIVIDAD CON MEMORIZACIÓN 
  Problema

La función recalcula MUCHO:

contar_rutas(3,3)

repite llamadas como:

contar_rutas(2,2)
contar_rutas(1,2)
etc

 Solución: MEMOIZACIÓN
memo = {}

def contar_rutas(m, n):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 1

    memo[(m, n)] = contar_rutas(m - 1, n) + contar_rutas(m, n - 1)
    return memo[(m, n)]

print(contar_rutas(3,3))  # 20
 Qué hiciste aquí

 Guardaste resultados
 Evitaste repetir cálculos
 Bajaste de exponencial → casi O(m*n)




 CONJUNTOS
plan_cine = {"Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía"}
plan_series = {"Pedro", "Sofía", "Marta", "Andrés", "Lucía", "Valentina"}
 1. Usuarios únicos

 Unión

todos = plan_cine | plan_series
 2. Ambos planes

 Intersección

ambos = plan_cine & plan_series

Resultado:
{"Pedro", "Sofía", "Lucía"}

 3. Solo Cine

 Diferencia

solo_cine = plan_cine - plan_series
 4. Exclusivos de un solo plan

 Diferencia simétrica
exclusivos = plan_cine ^ plan_series

 5. Verificar usuario
"Carlos" in plan_series  # False

 6. Porcentaje premium
Paso 1: ambos
ambos = plan_cine & plan_series
Paso 2: total
total = plan_cine | plan_series
Paso 3: porcentaje
porcentaje = (len(ambos) / len(total)) * 100

 Resultado aproximado
ambos = 3
total = 9

≈ 33.33%


  COMPLEJIDAD 
 Código
for i in range(n):
    for j in range(i + 1, n):
 Análisis
Primer loop → n
Segundo loop → n

 Total:

 Complejidad:
O(n²)
 ¿Qué pasa si duplicas la lista?

Si n → 2n:

 (2n)² = 4n²

 El tiempo se cuadruplica

 Mejor solución (O(n))

Usando un set:

def encontrar_pares(lista, objetivo):
    vistos = set()

    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            print(f"Par: ({num}, {complemento})")
        vistos.add(num)
 Por qué funciona
Buscas en O(1)
Recorres una sola vez

 Total: O(n)

 RESUMEN
Tema	Respuesta clave
Regex correo	c
Regex teléfono	ninguna (faltó \+)
Memoización	usar diccionario
Conjuntos	`
Complejidad	O(n²) → optimizable a O(n)