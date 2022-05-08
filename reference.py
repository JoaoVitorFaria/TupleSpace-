
# Import para criacao de uma cliente
import xmlrpc.client


# instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8053')

#usando s.pow é possivel invocar os metodos do servidor
var = []
var = s.calculo(10,8)

print(var)
# eh possivel listar todos os metodos disponiveis no servidor
# isso pode ser utilizado para criar um dicionario de servicos
# print(s.system.listMethods())