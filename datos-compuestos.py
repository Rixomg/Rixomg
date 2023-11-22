
#creando una lista (se pueden modificar)
lista = ["Rix","Hydra",True,1.79,"Hydra"]

#creando una tupla (no se pueden modificar)
tupla = ("Rix","Hydra",True,1.79,"Hydra")

#esto vale
lista[3] = "Maquina"

#esto no
#tupla[3] = "Maquina"

#creando un conjunto(set)(no se accede a elementos por índice, no almacena datos duplicados)
conjunto = {"Rix", "Hydra", True, 1.79, "Hydra"}

#print(conjunto[3])->no puede acceder al elemento

#creando un diccionario (dict) (la estructura es key:value y separamos con comas en medio)
diccionario = {
    'nombre':"Rix",
    'canal': "Rix231",
    'esta_triste':True,
    'altura':1.79,
    'dato_duplicado':"Rix"
}
print(diccionario['canal'])

#corchetes rectos para el print, 2 comillas para el value y una para el key,

print(tupla[3])