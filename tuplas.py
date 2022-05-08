import pickle
import threading
import os.path

# from sqlalchemy import false

class Tuple_Space:
    def __init__(self):
        self.lock = threading.Lock()
        # self.tuplas = []
        if not os.path.isfile("tupla.pickle"):
            self.tuplas = []
        else:
            with open("tupla.pickle", "rb") as f:
                self.tuplas = pickle.load(f)
        

    def Read(self, tupla):
        if self.Verifica_Tupla(tupla):  
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                return {
                    "msg": "Tupla " + str("("+str(tupla[0])+", ...)") + " não encontrada.",
                }
            return {
                "tupla": minha_tupla,
                "msg": "Tupla " + str(minha_tupla) + " lida com sucesso.",
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
                "msg": "Erro ao escrever tupla\n" + str(tupla) + "."
            }

    def Take(self, tupla):
        if self.Verifica_Tupla(tupla):  
            self.lock.acquire()
            minha_tupla = self.Get_Tupla(tupla)
            if minha_tupla == False:
                self.lock.release()
                return{
                    "msg": "Tupla " + str(tupla) + " não pode ser obtida."
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
                "msg": "Tupla " + str(minha_tupla) + " obtida com sucesso."
            }
        else:
            self.lock.release()
            return {
                "msg": "Tupla em uso ou não existe."
            }
        
    def Calculo(self, tupla):
        if self.Verifica_Tupla(tupla):  
            temp = list(tupla)
            result =[]
            result.append(temp[1]*temp[2])
            pass
        else:
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
                        if type(tupla[i]) == type(x[i]) and continua_verificacao and tupla[i] == x[i]:
                            continue
                        else:
                            continua_verificacao = False
                            break
                if i == (len(tupla) - 1) and continua_verificacao:
                    return x
        return False