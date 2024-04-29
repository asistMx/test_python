

string = "Esta,es,una,cadena,de,caracteres"

# Split
list_string = string.split(",")

print(list_string)

# Join
new_string = ",".join(list_string)

print(new_string)

string2 = "Hola Mundo"
list_string2 = string2.split(" ")

print(list_string2)

# Replace

string3 = "     Hola Mundo "
new_string3 = string3.replace("Hola", "Hello")
print(new_string3)

print(string3.endswith("la"))
print(string3.find("Mundoss"))

print(string3.strip())


# Formateo de cadenas

name = "Juan"
age = 30

print("Hola, mi nombre es {} y tengo {} años".format(name, age))

print(f"Hola, mi nombre es {name} y tengo {age} años")

print("Hola, mi nombre es {0} y tengo {1} años".format(name, age))

print("Hola, mi nombre es {name} y tengo {age} años".format(name="Pedro", age=40))

print("Hola, mi nombre es {name} y tengo {age} años".format(name=name, age=age))



print(string3.startswith("Hola"))