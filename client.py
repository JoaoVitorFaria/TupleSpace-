
# Import para criacao de uma cliente
import xmlrpc.client


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8054')

#usando s.pow é possivel invocar os metodos do servidor
# var = []
# var = s.calculo(10,8)
var = ('joao', 'wesley', 'daniel',)
teste = s.write(var)
print(teste)
teste = s.read(var)
print(teste)
test = s.take(var)
print(test)
# print(var)
# eh possivel listar todos os metodos disponiveis no servidor
# isso pode ser utilizado para criar um dicionario de servicos
# print(s.system.listMethods())