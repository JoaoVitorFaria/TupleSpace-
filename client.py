# Import para criacao de uma cliente
import xmlrpc.client
import pprint


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8054')

#usando s.pow é possivel invocar os metodos do servidor
# var = []
# var = s.calculo(10,8)
#var = ('calculos', 10, 20,)
#teste = s.write(var)
#print(teste)
#temp = []
#for i in range (3):
 #   temp.append(input("Digite um valor"))
temp = (17.6, 14.0, 3.84)
var = tuple(temp)

# var = ("tela","mouse", "teclado",)
# implementar atualização da tupla

#test = s.take(var)
#print(test)
# print(var)
# eh possivel listar todos os metodos disponiveis no servidor
# isso pode ser utilizado para criar um dicionario de servicos
# print(s.system.listMethods())
