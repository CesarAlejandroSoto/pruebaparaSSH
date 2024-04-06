empresa = {
"empleados":[
    {"nombre":"maria","edad":20},
    {"nombre":"esteban","edad":30},
    {"nombre":"pepe","edad":25}
],
"autos":[
    {"marca":"ford","modelo":"f20","submodelo":["f20.01","f20.02"]},
    {"marca":"nissan","modelo":"n20","submodelo":["n20.01","n20.02"]},
    {"marca":"seat","modelo":"s20","submodelo":["s20.01","s20.02"]}
]
}
print("la edad del empleado numero 2 es :",empresa["empleados"][2]["edad"])
print("el segundo submodelo del auto numero 2 :", empresa["autos"][2]["submodelo"][1])

registro_ventas = {'producto1':50,'producto2':100,'producto3':150,'producto4':80,'producto5':110,'producto6':90,}

print(registro_ventas[50])