# from math import factorial


# print('Impares menores a 10')
# x = 1
# while x <= 10 :
#     print(x)
#     x += 2

# ###############

# factorial = 5
# contador = factorial - 1
# while contador > 0 :
#     factorial *= contador
#     contador -= 1

# print('El factorial de 5 es', factorial)

# #################

# for i in 1, 2, 3 :
#     print(i)

# for i in range(5) :
#     print(i)

# for i in ['Ale', 'Iván', 'Monse', 'Luis', 'Rafa', 'Luca'] :
#     print(i)

# #######################

# for i in 'Hola Mundo' :
#     if i == 'M' :
#         pass
#     else : 
#         print(i, end=' ')

# for i in range(2, 200) :
#     primo = True
#     for j in range(2, i) :
#         if i == j :
#             break
#         elif i % j == 0 :
#             primo = False
#         else :
#             continue
    
#     if primo == True :
#         print(i, end=' ')

############################
# Reto semana 6 - contraseñas

password1 = input('Ingresa una contraseña: ')

while password1[0].isnumeric() == False :
    print('La contraseña debe comenzar con un número.')
    password1 = input('Ingresa una contraseña: ')
    
if password1[0].isnumeric() :
    password2 = input('Ingresa de nuevo la contraseña: ')
    while password1 != password2 :
        print('Las contraseñas no coinciden.') 
        password2 = input('Ingresa la contraseña nuevamente: ') 
        
        if password1 == password2 :
            print('Contraseña correcta')
               
else :
    exit()
    

