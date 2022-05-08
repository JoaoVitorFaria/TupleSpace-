class Tuple_Space:
    def __init__(self):
        # TupleSpace pode ser armazenado em uma lista
        self.tuplas = []

    def read(self, tupla):
        # Aqui teremos que descobrir uma maneira de bloquear o acesso à tupla enquanto ela esta sendo utilizada
        if self.verifica_tupla(tupla):  
            # Se a tupla estiver no TupleSpace: retorne seus valores
            # Senao: retorne erro
            pass
        else:
            # Retornar erro com o dado passado
            pass

    def write(self, tupla):
        # Eh bom verificar se o dado passado eh uma tupla
        if self.verifica_tupla(tupla):
            # Se tupla já inserida: retorne erro
            # Senao: append da tupla
            pass 
        else:
            # Retornar erro com o dado passado
            pass

    def take(self, tupla):
        # Aqui teremos que descobrir uma maneira de bloquear o acesso à tupla enquanto ela esta sendo utilizada
        if self.verifica_tupla(tupla):  
            # Verificar se tupla esta no TupleSpace
                # Se estiver, remove-la
                # Senao: retornar erro 
            pass
    
        else:
            # Retornar erro com o dado passado
            pass
        
    def calculo(self, tupla):
        pass

    def verifica_tupla(self, tupla):
        # Implementar uma forma de verificar se o dado é do tipo tupla
        pass
