import os
import os
base_name = "archivo"
i=1

while True:
    print("while")

    nombre_archivo = f"{base_name}{i}.txt"
    if not os.path.exists(nombre_archivo):
        print("no exits")
        break
    i+=1

with open(nombre_archivo,"w") as archivo:
    archivo.write("valencia nuevo contenido")
print(f"se ha creado el archivo{nombre_archivo} con exito")

