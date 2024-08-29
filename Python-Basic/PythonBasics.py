# variables test
codigo = 10
salario = 1500.00
nome = "José da Silva"

# typing test
tipo = type (salario)

#input test
print("O codigo é :", codigo, "e é do tipo: ", type(codigo), "\a")

# for test
for n in range(10):
    print("Valor: ", n)
    
# while test
x = 1
while x < 10:
    print("Valor: ", x)
    x = x + 1
    
# function test   
def message():
    print("Hello World")
    
# file opening and whriting
file = open("ras.txt","w")
file.write("Teste de escrite: \n")
file.write("hahahahaha ")
file.close()
file = open("ras.txt","r")
fileText = file.read()
print (fileText)

