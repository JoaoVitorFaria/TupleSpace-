# Import para criacao de uma cliente
import xmlrpc.client
import pprint


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8057')

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
            if insert == '-1':continue
            else:
                tupla.append(insert)

        temp = tuple(tupla)
        result = s.write(temp)
        print (result)
    elif op == 2:#read
        print("Insira os elementos da tupla que deseja pesquisar(Insira -1 para indicar o fim da tupla)")
        tupla =[]
        search = 0
        while search != '-1':
            search = input()
            if search == '-1':continue
            else:
                tupla.append(search)
            

        temp = tuple(tupla)
        print(temp)
        result = s.read(temp)
        print (result)
    elif op == 3:#take
        print("Insira os elementos da tupla que deseja atualizar(Insira -1 para indicar o fim da tupla)")
        tupla =[]
        search = 0
        while search != '-1':
            search = input()
            if search == '-1':continue
            else:
                tupla.append(search)

        temp = tuple(tupla)
        result = s.take(temp)
        print (result)
        tupla  = result['tupla']
        print("Digite 1 para inserir um elemento na tupla, 2 para remover e -1 para finalizacar a operacao")
        search = 0
        while search != '-1':
            search = input()
            if search == '-1':continue
            elif search == '1':
                new = input("-")
                tupla.append(new)
            elif search == '2':
                new = input("-")
                tupla.remove(new)
        
        final = tuple(tupla)
        result = s.write(final)
        print(result)
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

