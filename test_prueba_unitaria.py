import pytest
from prueba_unitaria import numeros_amigos, sum, main

def test_sum():
    assert sum(220,284)==504
    print("La funcion esta trabajando correctamente")

def test_numero_amigos():
    assert numeros_amigos(220,284)=="220 y 284 son amigos"
    print("La funcion esta trabajando correctamente")


if __name__ == '__main__':
    test_numero_amigos()
    test_sum()
    
