from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:8000", allow_none=True)

while(True):

  valores = server.read(('cliente', int(), int()))

  if valores['data'] == -1:
      pass
  else:
      num1 = valores['data'][1]
      num2 = valores['data'][2]

      soma = ('servidor', num1 + num2)

      tuplaSoma = server.read(soma)

      if tuplaSoma['data'] == -1:
          server.write(soma)
      else:
          if soma != tuple(tuplaSoma['data']):
              server.take(soma)
              server.write(soma)