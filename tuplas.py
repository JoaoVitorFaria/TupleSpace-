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
            self.Calculo(tupla)
            minha_tupla = self.Get_Tupla(tupla)
            # Caso ela não esteja no espaço de tupla uma mensagem apropriada é retornada
            if minha_tupla == False:
                return {
                    "msg": "Tupla " + str(tupla) + " não existente, utilize o método Write para adicioná-la ao espaço.",
                }
            return {
                "tupla": minha_tupla,
                "msg": "Tupla " + str(minha_tupla) + " lida com sucesso.",
            }
        else:
            return{
                "msg": "O objeto passado não é uma tupla!"
            }

    # A função Write adiciona uma nova tupla ao espaço de tuplas, mas antes disso ele verifica se a tupla já existe dentro do espaço, caso
    # ela exista é retornada uma mensagem apropriada
    def Write(self, tupla):
        if self.Verifica_Tupla(tupla):
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                self.tuplas.append(tupla)
                with open("tupla.pickle","wb") as f:
                    pickle.dump(self.tuplas, f)
                return{
                    "tupla": tupla,
                    "msg": "Tupla " + str(tupla) + " escrita com sucesso!",
                } 
            else:
                return{
                    "msg": "Tupla " + str("("+str(tupla[0])+", ...)") + " já existe, você precisa obtê-la utilizando o método take para atualizá-la."
                }
        else:
            return{
                "msg": "O objeto passado não é uma tupla!"
            }

    # O método Take busca e retira uma tupla do espaço de tupla, bem como retorna essa tupla ao usuário para que o mesmo possa modificá-la
    def Take(self, tupla):
        if self.Verifica_Tupla(tupla):  
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                return{
                    "msg": "Tupla " + str(tupla) + " não pode ser obtida."
                }
            self.tuplas.remove(minha_tupla)
            return{
                "tupla": minha_tupla,
                "msg": "Tupla " + str(minha_tupla) + " obtida com sucesso."
            }
        else:
            return {
                "msg": "Tupla em uso ou não existe."
            }
        
    def Calculo(self, tupla):
        if self.Verifica_Tupla(tupla):  
            (num1, num2) = tupla
            return {
                "tupla": tupla,
                "msg": "A multiplicação dos valores da tupla é: " + str(float(num1)*float(num2)),
            }
        else:
            return{
                "msg": "Tupla inexistente."
            }

    # Função que verificar se o objeto passado é de fato uma tupla, se for retorna verdadeiro se não retorna falso
    def Verifica_Tupla(self, tupla):
        if type(tupla) != tuple:
            return False
        return True

    # Função para retornar uma tupla específica
    def Get_Tupla(self, tupla):
        # Caso o espaço de tupla esteja vazio retorna False
        if len(self.tuplas) == 0:
            return False
        # Caso seja passada uma tupla vazia retorna todas as tuplas contidas no espaço de tuplas
        if len(tupla) == 0:
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
                    if i == 0:
                        if tupla[i] == t[i]:
                            continua_verificacao = True
                            continue
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