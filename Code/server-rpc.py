
from xmlrpc.server import SimpleXMLRPCServer
import time
import json

class RPC:
    _metodos_rpc = ['request_bank', 'relase', 'get']

    def __init__(self, direccion):
        self._nro_actual = 0
        self._nro_cola = 0
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))


    def request_bank(self):
        nro = self._nro_cola + 1
        self._nro_cola = self._nro_cola + 1
        if self._nro_actual == 0:
            self._nro_actual = nro
        return nro

    def relase(self, nro):
        if self._nro_actual == nro:
            self._nro_actual = self._nro_actual + 1
            return 0
        return 1
    
    def get(self):
        return self._nro_actual

    def iniciar_servidor(self):
        self._servidor.serve_forever()


if __name__ == '__main__':
    rpc = RPC(('', 20064))
    print('Se ha iniciado el servidor')
    rpc.iniciar_servidor()
