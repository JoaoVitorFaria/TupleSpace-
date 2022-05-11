# Import para criacao de um cliente
import xmlrpc.client


# # instanciacao da comunicacao com o servidor
s = xmlrpc.client.ServerProxy('http://localhost:8057')

op = 1
while op != 0:
    try:
        op = int(input("\nEscolha a operacao que deseja realizar:\n(1) Escrever uma tupla\n(2) Ler uma tupla\n(3) Atualizar uma tupla\n(4) Realizar calculo\n(5) Ler todas as tuplas\n(6) Consultar por prefixo\n(0) Sair\nSua opção-> "))
    except:
        print("Entrada inválida! Por favor selecione uma das opções apresentadas")
        continue

    if op == 1: #write
        print("\nInsira os elementos da tupla(Insira -1 para indicar o fim da tupla)")
        tupla =[]
        insert = 0
        while insert != '-1':
            insert = input()
            if insert == '-1':continue
            else:
                tupla.append(insert)

        temp = tuple(tupla)
        result = s.write(temp)
        print()
        for chave, valor in result.items():
            print(f"{chave}: {valor}")
    elif op == 2:#read
        temp = s.readAll()
        print()
        if len(temp) == 1:
            for chave, valor in temp.items():
                print(f"{chave}: {valor}")
        else:
            print("\nInsira os elementos da tupla que deseja pesquisar(Insira -1 para indicar o fim da tupla)")
            tupla =[]
            search = 0
            while search != '-1':
                search = input()
                if search == '-1':continue
                else:
                    tupla.append(search)
            temp = tuple(tupla)
            result = s.read(temp)
            print()
            for chave, valor in result.items():
                print(f"{chave}: {valor}")
    
    elif op == 3:#take
        temp = s.readAll()
        print()
        if len(temp) == 1:
            for chave, valor in temp.items():
                print(f"{chave}: {valor}")
        else:
            print("\nInsira os elementos da tupla que deseja atualizar(Insira -1 para indicar o fim da tupla)")
            tupla =[]
            search = 0
            while search != '-1':
                search = input()
                if search == '-1':continue
                else:
                    tupla.append(search)
            temp = tuple(tupla)
            result = s.take(temp)
            if len(result) == 1:
                print()
                for chave, valor in result.items():
                    print(f"{chave}: {valor}")
            else:
                tupla  = result['tupla']
                while search != -1:
                    try:
                        search = int(input("\nDigite 1 para inserir um elemento na tupla, 2 para remover e -1 para finalizacar a operacao\n"))
                    except:
                        print("Entrada inválida! Por favor digite uma das opções apresentadas.")
                        continue
                    if search == -1:continue
                    elif search == 1:
                        new = input("-> ")
                        tupla.append(new)
                    elif search == 2:
                        new = input("-> ")
                        try:
                            tupla.remove(new)
                        except:
                            print("\nA tupla não possuem o elemento " + str(new) + " por favor selecione um elemento válido! ")
                            print("\nDigite 1 para inserir um elemento na tupla, 2 para remover e -1 para finalizacar a operacao")
                            continue
                final = tuple(tupla)
                result = s.write(final)
                print()
                for chave, valor in result.items():
                    print(f"{chave}: {valor}")
    
    elif op == 4:#calculo
        var01 = ''
        var02 = ''
        while var01 != float or var02 != float:
            try:
                var01 = float(input("\nDigite o primeiro valor:\n-> "))
                var02 = float(input("\nDigite o segundo valor:\n-> "))
                break
            except:
                print("\nEntrada inválida! Por favor digite um valor numérico.")
                continue
        temp = []
        temp.append(var01)
        temp.append(var02)
        tupla = tuple(temp)
        result = s.calculo(tupla)
        print()
        for chave, valor in result.items():
            print(f"{chave}: {valor}")

    elif op == 5:#ver todas
        temp = s.readAll()
        print()
        if len(temp) == 1:
            for chave, valor in temp.items():
                print(f"{chave}: {valor}")
        else:
            j = 0
            for chave in temp:
                if (j == 0):
                    print(chave + ":")
                    break
                j += 1
            for tupla in temp['tuplas']:
                print(" " + str(tupla))
            for chave, valor in temp.items():
                if chave != 'tuplas':
                    print(f"{chave}: {valor}")

    elif op == 6:#ver todas com determinado prefixo
        print("\nInsira o prefixo (primeiro elemento) da tupla: ")
        tupla = []
        insert = input()
        tupla.append(insert)
        temp = s.consulta_prefixo(tuple(tupla))
        print()
        if len(temp) == 1:
            for chave, valor in temp.items():
                print(f"{chave}: {valor}")
        else:
            j = 0
            for chave in temp:
                if (j == 0):
                    print(chave + ":")
                    break
                j += 1
            for tupla in temp['tuplas']:
                print(" " + str(tupla))
            for chave, valor in temp.items():
                if chave != 'tuplas':
                    print(f"{chave}: {valor}")

    elif op == 0:#sair
        print("Aplicação encerrada")

