from models.cliente import Cliente
from utils.helper import date_para_str, str_para_date


class Conta:
    codigo = 100

    def __init__(self, cliente: Cliente) -> None:
        self.numero: int = Conta.codigo
        self.__cliente: Cliente = Cliente
        self.__saldo: float = 0.0
        self.__limite: float = 150.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self):
        return f''
