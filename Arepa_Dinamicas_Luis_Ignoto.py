#Tarea 1 - Arepas Dinámicas 

#Escriba un programa en Python que pueda solicitar los ingredientes 
# al usuario e indique la cantidad (masa) de arepas resultante. 
# Use input("pregunta") para permitirle al usuario introducir el valor.

#Resolución:

#Introducir cantidades de ingredientes solicitados
agua =int(input("¿Cuántas tazas de agua? :"))
harina =int(input("¿Cuántas tazas de harina? :"))
sal = int(input("¿Cuántas cucharaditas de sal? :"))
aceite = int(input("¿Cuántas cucharaditas de aceite? :"))

#Conversiones de unidades de volumen de los ingredientes.
#Recordar que:      1 tza = 250 ml;     1 cdta = 5 ml;
agua = agua * 250;
harina = harina * 250;
sal = sal * 5;
aceite = aceite * 5;

#Volumen total de la mezcla
volumen = agua + harina + sal + aceite;

#Estimar cantidad de masa según densidad promedio de la mezcla
densidad_promedio = 3; #g/ml
masa = volumen * densidad_promedio;

#Imprimir resultados
print("La cantidad de masa de arepa que se tiene con los ingredientes dados es de: " , masa , " gramos")

