# Práctica con Variables 10
# Declara dos variables, llamadas nombre y edad.

# Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

nombre = 'Tony Soprano'
edad = 51

# Práctica con Variables 11
# Crea tres variables:

# nombre
# apellido
# nombrecompleto

# A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente, construye la variable nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio).
nombre = 'Julia'
apellido = 'Roberts'
nombrecompleto = nombre + ' ' + apellido

# Práctica con Variables 12
# Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:

# Estás tomando un curso de curso

# Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable. Recuerda agregar un espacio antes de concatenar la variable al resto del texto.

curso = 'Python'
print('Estas tomando un curso de ' + curso)


# Práctica con Integers 13
# Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

# Imprime el tipo de dato de dicha variable.

num_entero = 10;
print(type(num_entero))

# Práctica con Floats 14
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

# Imprime el tipo de dato de dicha variable.

num_decimal = 10.2
print(type(num_decimal))

# Práctica con Tipos de Datos Numéricos 15
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

# Para ello, crea dos variables:

# num1 = 7.5

# num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

num1 = 7.5
num2 = 2.5

print(type(num1 + num2))


# Práctica con Conversiones 16
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:

num1 = 7.5
print(type(int(num1)))


# Práctica con Conversiones 17
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:

num2 = 10
print(type(float(num2)))

# Práctica con Conversiones 18
# Suma los valores de num1 y num2.

# No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().

num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))