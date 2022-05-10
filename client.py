# Import para criacao de uma cliente
import xmlrpc.client
import pprint


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8056')

#usando s.pow é possivel invocar os metodos do servidor
# var = []
# var = s.calculo(10,8)
#var = ('calculos', 10, 20,)
#teste = s.write(var)
#print(teste)
#temp = []
#for i in range (3):
 #   temp.append(input("Digite um valor"))
# temp = (17.6, 14.0, 3.84)
# var = tuple(temp)

# var = ("tela","mouse", "teclado",)
# implementar atualização da tupla

#test = s.take(var)
#print(test)
# print(var)
# eh possivel listar todos os metodos disponiveis no servidor
# isso pode ser utilizado para criar um dicionario de servicos
# print(s.system.listMethods())

op = 1
while op != 0:
    op = int(input("\nEscolha a operacao que deseja realizar:\n(1) Escrever uma tupla\n(2) Ler uma tupla\n(3) Atualizar uma tupla\n(4) Realizar calculo\n(5) Ler todas as tuplas\n(0) Sair\n\n-"))
    if op == 1: #write
        print("Insira os elementos da tupla(Insira -1 para indicar o fim da tupla)")
        tupla =[]
        insert = 0
        while insert != '-1':
            insert = input()
            tupla.append(insert)

        temp = tuple(tupla)
        result = s.write(temp)
        print (result)
    elif op == 2:#read
        pass
    elif op == 3:#take
        pass
    elif op == 4:#calculo
        var01 = float(input("Digite o primeiro valor:\n-"))
        var02 = float(input("\nDigite o segundo valor:\n-"))
        temp =[]
        temp.append(var01)
        temp.append(var02)
        tupla = tuple(temp)
        result = s.calculo(tupla)
        print(result)
    elif op == 5:#ver todas
        temp = s.readAll()
        print(temp)
    elif op == 0:#sair
        print("Aplicação encerrada")

