cantidad_minuto=input("dijite la cantidad de minutos: ")
cantidad_minuto=int(cantidad_minuto)

if cantidad_minuto<=3:
    valor_llamada=300

else:
    valor_llamada=300+50*(cantidad_minuto-3)

print("el valor de la llamada es: "+str(valor_llamada))