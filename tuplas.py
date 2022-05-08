import threading

class Tuple_Space:
    def __init__(self):
        self.lock = threading.Lock()
        self.tuplas = []

    def Read(self, tupla):
        if self.Verifica_Tupla(tupla):  
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                return {
                    "msg": "Tupla " + str("("+str(tupla[0])+", ...)") + "\nnão encontrada.",
                }
            return {
                "tupla": minha_tupla,
                "msg": "Tupla " + str(minha_tupla) + "\nlida com sucesso.",
            }
        else:
            return{
                "msg": "Tupla inexistente."
            }

    def Write(self, tupla):
        if self.Verifica_Tupla(tupla):
            minnha_tupla = self.Get_Tupla(tupla)
            if minnha_tupla == False:
                self.tuplas.append(tupla)
                return{
                    "tupla": tupla,
                    "msg": "Tupla " + str(tupla) + "\nescrita com sucesso!",
                } 
            else:
                return{
                    "msg": "Tupla " + str("("+str(tupla[0])+", ...)") + "\njá existe, você precisa obtê-la utilizando o método take para atualizá-la."
                }
        else:
            return{
                "msg": "Erro ao escrever tupla\n" + str(tupla) + "."
            }

    def Take(self, tupla):
        if self.Verifica_Tupla(tupla):  
            self.lock.acquire()
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                self.lock.release()
                return{
                    "msg": "Tupla " + str(tupla) + "\nnão pode ser obtida."
                }

            try:
                self.tuplas.remove(minha_tupla)
            except Exception as e:
                self.lock.release()
                return{
                    "msg": "Ocorreu um erro ao tentar obter a tupla" + str(minha_tupla)
                }
            self.lock.release()
            return{
                "tupla": minha_tupla,
                "msg": "Tupla " + str(minha_tupla) + "\nobtida com sucesso."
            }
        else:
            self.lock.release()
            return {
                "msg": "Tupla em uso ou não existe."
            }
        
    def calculo(self, tupla):
        pass

    def Verifica_Tupla(self, tupla):
        if type(tupla) != tuple:
            return False
        return True

    def Get_Tupla(self, tupla):
        if len(self.tuplas) == 0:
            return False
        if len(tupla) == 0:
            try:
                return self.tuplas
            except Exception as e:
                return False
        else:
            continua_verificacao = False
            for _, x in enumerate(self.tuplas):
                for i in range(len(tupla)):
                    if i == 0:
                        if tupla[i] == x[i]:
                            continua_verificacao = True
                            continue
                        else:
                            break
                    else:
                        if type(tupla[i]) == type(x[i]) and continua_verificacao:
                            return x
                        else:
                            break
        return False