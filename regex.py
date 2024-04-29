import re

texto = 'Este es un texto de prueba para el curso de Python y aplicar expresiones regulares en un texto'

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

#mat = re.findall(r'text*', texto)#

mat = re.findall(r'[a-z,A-Z,0-9]', texto)

print(mat)