#prototipo de calculadora 
num1 = int(input('ingrese primer numero:'))
num2 = int(input('ungrese segundo numero:'))

print('menu de opciones:')
print('1:suma')
print('2:resta')
print('3:Division')
print('4:multiplicacion')

opciones = int(input('escoja una opcion del menu'))

if opciones == 1: 
    print('la suma es :', num1 + num2)
elif opciones == 2 : 
    print('la resta es:', num1 - num2)  
elif opciones == 3: 
    print('la Division es:', num1 / num2) 
elif opciones == 4:
    print('la multiplicacion:', num1 * num2) 

else:
    print("no se eligio una opcion valida") 
     
      