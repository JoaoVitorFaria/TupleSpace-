#https://docs.python.org/pt-br/3/library/xmlrpc.server.html

# Import para criacao do servidor
from xmlrpc.server import SimpleXMLRPCServer

from tuplas import Tuple_Space

class Server:
    
    def __init__(self, PORT):
        print("Servidor iniciado")

        with SimpleXMLRPCServer(('localhost', PORT)) as server:
            # Descomente a linha abaixo para chamar o metodo que lista as funcoes do servidor para o cliente
            # server.register_introspection_functions()

            class tuple_operations:
                def __init__(self):
                    self.minha_tupla = Tuple_Space()

                def calculo(self, argument):
                    # retorna a invocacao do metodo de calculo
                    temp = tuple(argument)
                    return self.minha_tupla.Calculo(temp)

                def read(self, argument):
                    # retorna a invocacao do metodo read
                    temp = tuple(argument)
                    return self.minha_tupla.Read(temp)

                def take(self, argument):
                    # retorna a invocacao do metodo take
                    temp = tuple(argument)
                    return self.minha_tupla.Take(temp)
                
                def write(self, content):
                    # retorna a invocacao do metodo write
                    temp = tuple(content)
                    return self.minha_tupla.Write(temp)

                def readAll(self):
                    # retorna a invocacao do metodo readAll
                    return self.minha_tupla.Read_All()
                
                def consulta_prefixo(self, content):
                    # retorna a invocacao do metodo consulta_prefixo
                    temp = tuple(content)
                    return self.minha_tupla.Consulta_Prefixo(temp)
            
            server.register_instance(tuple_operations())

            server.serve_forever()
        
    
if __name__ == '__main__':
    PORT = 8057
    server = Server(PORT)
    