import pickle
import os.path

class Tuple_Space:
    def __init__(self):
        if not os.path.isfile("tupla.pickle"):
            self.tuplas = []
        else:
            with open("tupla.pickle", "rb") as f:
                self.tuplas = pickle.load(f)

    # A função Read busca a tupla desejada para leitura, caso ela esteja no espaço de tuplas nós a retornamos juntamente com uma mensagem
    # de sucesso utilizando um formato de dicionário
    def Read(self, tupla):
        if self.Verifica_Tupla(tupla):
            minha_tupla = self.Get_Tupla(tupla)
            # Caso ela não esteja no espaço de tupla uma mensagem apropriada é retornada
            if minha_tupla == False:
                return {
                    "mensagem": "Tupla " + str("["+str(tupla[0])+", ...]") + " não adicionada, utilize o método Write para adicioná-la ao espaço.",
                }
            return {
                "tupla": minha_tupla,
                "mensagem": "Tupla lida com sucesso.",
            }
        else:
            return{
                "mensagem": "O objeto passado não é uma tupla ou é uma tupla vazia!"
            }

    # A função Write adiciona uma nova tupla ao espaço de tuplas, mas antes disso ele verifica se a tupla já existe dentro do espaço, caso
    # ela exista é retornada uma mensagem apropriada
    def Write(self, tupla):
        if self.Verifica_Tupla(tupla):
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                self.tuplas.append(tupla)
                with open("tupla.pickle", "wb") as f:
                    pickle.dump(self.tuplas, f)
                return{
                    "tupla": tupla,
                    "mensagem": "Tupla adicionada ao espaço de tuplas com sucesso!",
                }
            else:
                return{
                    "mensagem": "Tupla " + str("["+str(tupla[0])+", ...]") + " já existe, você precisa obtê-la utilizando o método Take para atualizá-la."
                }
        else:
            return{
                "mensagem": "O objeto passado não é uma tupla ou é uma tupla vazia!"
            }

    # O método Take busca e retira uma tupla do espaço de tupla, bem como retorna essa tupla ao usuário para que o mesmo possa modificá-la
    def Take(self, tupla):
        if self.Verifica_Tupla(tupla):
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                return{
                    "mensagem": "Tupla " + str("["+str(tupla[0])+", ...]") + " em uso ou não existe."
                }
            self.tuplas.remove(minha_tupla)
            with open("tupla.pickle", "wb") as f:
                    pickle.dump(self.tuplas, f)
            return{
                "tupla": minha_tupla,
                "mensagem": "Tupla obtida com sucesso."
            }
        else:
            return {
                "mensagem": "O objeto passado não é uma tupla ou é uma tupla vazia!"
            }

    # Função que calcula e retorna o produto dos valores contidos em uma tupla de tamanho 2
    def Calculo(self, tupla):
        if self.Verifica_Tupla(tupla):
            temp = list(tupla)
            num1 = temp[0]
            num2 = temp[1]
            return {
                "tupla": tupla,
                "mensagem": "A multiplicação dos valores da tupla é: {:.2f}".format(num1*num2),
            }
        else:
            return{
                "mensagem": "O objeto passado não é uma tupla ou é uma tupla vazia!"
            }

    # Função que verificar se o objeto passado é de fato uma tupla, se for retorna verdadeiro se não retorna falso
    def Verifica_Tupla(self, tupla):
        if type(tupla) != tuple or len(tupla) == 0:
            return False
        return True

    # Função para retornar uma tupla específica
    def Get_Tupla(self, tupla):
        # Caso o espaço de tupla esteja vazio retorna False
        if len(self.tuplas) == 0:
            return False
        # Se não for uma tupla vazia então iremos buscar a tupla desejada no espaço
        else:
            # Essa variável booleana irá nos ajudar a otimizar nossa busca
            continua_verificacao = False
            # Para cada tupla contida no espaço de tuplas primeiro nós comparamos o tamnanho da tupla desejada com o tamanho da tupla atual (t)
            # se as tuplas tiverem tamanhos diferentes então nós vamos para o próxima iteração caso elas tenham o mesmo tamanho
            # nós iremos comparar campo a campo para ver se elas possuem os mesmos valores
            for t in self.tuplas:
                if len(tupla) != len(t):
                    continue
                for i in range(len(tupla)):
                    # Se o primeiro campo já for diferente nós encerramos as comparações e passamos para a próxima tupla, caso eles sejam iguais
                    # nós atualizamos o valor do continua_verificação para dizer ao programa que ele pode comparar os campos restantes
                    # caso a tupla possua apenas um campo nós a retornamos
                    if i == 0:
                        if tupla[i] == t[i] and len(tupla) > 1:
                            continua_verificacao = True
                            continue
                        elif tupla[i] == t[i] and len(tupla) == 1:
                            return t
                        else:
                            break
                    else:
                        # Nós só iremos retornar a tupla caso todos os campos sejam iguais
                        if tupla[i] == t[i] and continua_verificacao:
                            if i == (len(tupla) - 1):
                                return t
                            continue
                        else:
                            # Durante estas comparações caso algum campo seja diferente nós passamos para a próxima tupla e retornamos o valor
                            # do continua_verifição para falso
                            continua_verificacao = False
                            break
        # Caso a tupla desejada não seja encotrada nós retornamos o valor falso
        return False

    # A função Read_All retorna todas as tuplas presentes no espaço de tupla para o usuário consultar
    def Read_All(self):
        if len(self.tuplas) == 0:
            return{
                "mensagem": "Nenhuma tupla presente no espaço de tuplas."
            }
        return {
            "tuplas": self.tuplas,
            "mensagem": "Todas as tuplas foram exibidas com sucesso."
        }

    # A função Consulta_Prefixo retorna todas as tuplas no espaço de tupla que possuirem o mesmo prefixo (primeiro elemento)
    def Consulta_Prefixo(self, tupla):
        if self.Verifica_Tupla(tupla):
            # Aqui nós verificamos se o espaço de tupla não está vazio
            if len(self.tuplas) == 0:
                return{
                    "mensagem": "Nenhuma tupla presente no espaço de tuplas."
                }
            else:
                # Caso ele não esteja nós iremos guardar em uma lista temporária todas as tuplas que possuirem
                # o prefixo desejado e em seguida iremos converte-lá para uma tupla a qual iremos retornar para o usuario
                temp = []
                for t in self.tuplas:
                    if tupla[0] == t[0]:
                        temp.append(t)
                aux = tuple(temp)
                if len(aux) > 0:
                    return {
                        "tuplas": aux,
                        "mensagem": "Todas as tuplas do tipo " + str("[" + str(tupla[0]) + ", ...]") + " foram exibidas com sucesso."
                    }
                else:
                    return {
                        "mensagem": "Não foram encontradas tuplas do tipo " + str("("+str(tupla[0])+", ...)")
                    }
        else:
            return{
                "mensagem": "O objeto passado não é uma tupla ou é uma tupla vazia!"
            }