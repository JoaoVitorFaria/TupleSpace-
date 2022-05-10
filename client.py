# Import para criacao de uma cliente
import xmlrpc.client


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8054')

#usando s.pow é possivel invocar os metodos do servidor
# var = []
# var = s.calculo(10,8)
#var = ('calculos', 10, 20,)
#teste = s.write(var)
#print(teste)
temp = []
for i in range (2):
    temp.append(input("Digite um valor"))

var = tuple(temp)

# var = ("tela","mouse", "teclado",)
teste = s.write(var)
print(teste)

temp = s.read(var)
print(temp)

convert = list(temp['tupla'])

a = int(input("Deseja adicionar elemento?"))

if a == 1:
    convert.append(input("Digite um valor"))
    var = tuple(convert)
    teste = s.write(var)
    print(teste)
elif a == 2:
    convert.remove(input("Digite um valor:"))
    var = tuple(convert)
    teste = s.write(var)
    print(teste)



# implementar atualização da tupla

#test = s.take(var)
#print(test)
# print(var)
# eh possivel listar todos os metodos disponiveis no servidor
# isso pode ser utilizado para criar um dicionario de servicos
# print(s.system.listMethods())