# entrada = input('¡Hola! Introduce tu edad:')

# edad = 0

# if entrada.isnumeric():
#     edad = int(entrada)
# else :
#     print('Dato incorrecto. Debes introducir un número')
#     exit()

# if edad <= 0 :
#     print('¡¡WOOOOOWW!! Que joven eres. Pero, lo siento, eso no es posible')
# elif edad > 115 :
#     print('¡VAYA! ¿Cómo le haces para vivir tanto? No te creo, mejor intenta de nuevo')
# elif edad < 18 : 
#     print('Eres menor de edad, así que no puedes comprar tu cigarro')
# else : 
#     print('Eres mayor de edad. Aquí tienes tu cigarro')

a_actual = input('¡Hola! Escribe el año en el que te encuentras actualmente: ')

a_cualquiera = input('Ahora escribe un año cualquiera para hacer un cálculo: ')

calculo = 0

# if a_actual.isnumeric() and a_cualquiera.isnumeric():
#    calculo = int(a_actual) - int(a_cualquiera) 
# else :
#     print('Dato incorrecto. Debes introducir un número para ambos casos.')
#     exit()

# if a_actual.isnumeric() == a_cualquiera.isnumeric():
#    print('Dato incorrecto. Has introducido el mismo año que el actual.')
# else :
#     calculo = int(a_actual) - int(a_cualquiera)
#     exit()

if a_actual.isnumeric() and a_cualquiera.isnumeric() :
   calculo = int(a_actual) - int(a_cualquiera) 
else :
    print('Dato incorrecto. Debes introducir un número para ambos casos.')
    exit()

if a_actual == a_cualquiera :
   print('Dato incorrecto. Has introducido el mismo año que el actual.')
   exit()
else :
    if calculo > 1 :
        print('Han pasado', calculo, 'años desde el año que has introducido.')
    elif calculo == 1 :
        print('Ha pasado', calculo, 'año desde el año que has introducido.')
    elif calculo < -2 :
        print('Faltan', abs(calculo), 'años para llegar al año que has introducido.')
    elif calculo == -1 :
        print('Falta', abs(calculo), 'año para llegar al año que has introducido.')
    else : 
        exit() 