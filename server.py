
#https://docs.python.org/pt-br/3/library/xmlrpc.server.html

# Import para criacao do servidor
from platform import architecture
from xmlrpc.server import SimpleXMLRPCServer

# from click import argument
from tuplas import Tuple_Space
# Verificar funcionalidade
# from xmlrpc.server import SimpleXMLRPCRequestHandler

# Verificar funcionalidade
# # Restrict to a particular path.
# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ('/RPC2',)

class Server:
    
    def __init__(self, PORT):
        print("Servidor iniciado")
        #In python the with keyword is used when working with 
        # unmanaged resources (like file streams). 
        # It is similar to the using statement in VB.NET and C#.
        #  It allows you to ensure that a resource is "cleaned 
        # up" when the code that uses it finishes running, even 
        # if exceptions are thrown
        with SimpleXMLRPCServer(('localhost', PORT)) as server:
            # Descomente a linha abaixo para chamar o metodo que lista as funcoes do servidor para o cliente
            # server.register_introspection_functions()

            
            # Register an instance; all the methods of the instance are
            # published as XML-RPC methods (in this case, just 'mul').
            class tuple_operations:
                def __init__(self):
                    self.minha_tupla = Tuple_Space()

                def calculo(self, argument):
                    # retorna a invocacao do metodo calculo
                    pass

                def read(self, argument):
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

            
            # instaciacao de um objeto da classe tuple_operations
            # que lista os metodos que nao foram listados com register_function()
            server.register_instance(tuple_operations())

            # Run the server's main loop
            server.serve_forever()
        
    
if __name__ == '__main__':
    PORT = 8054
    server = Server(PORT)
    