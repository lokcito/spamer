# coding: utf-8
contador = open('cv.txt', 'r+')   # Abro contador
#ultimo_num = int(contador.read())       # obtengo ultimo numero
#nuevo = ultimo_num+1                    # genero nuevo número
array = contador.read()
array = array.split("\n")
#print array[0]
sub_array = array[0].split(":")
sub_array_2 = array[1].split(":")
#print sub_array
sub_array[1] = "g.com"
sub_array_2[1] = "adios mundo"
espacio = "\t\t\t\t\t\t"
array_output = sub_array[0] + ":" + sub_array[1] + espacio + "\n"
array_output += sub_array_2[0] + ":" + sub_array_2[1] + espacio
contador.seek(0)
contador.write(str(array_output))                   # sobreescribo el número
contador.close()      
