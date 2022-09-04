"""
-- Módulos e Pacotes --
    - Modularização
        : Surgiu no inicio da decadá de 60
        : Decorrido de sistemas maiores
    - Os focos da modularização
        : Dividir uma programa grande
        : Aumentar multi legibilidade
        : Facilitar multi manuntenção
-- Parte Teórica --
    - Vantagens da modularização
        : Organização do código
        : Agilidade de manuntenção
        : Ocultação de código detalhado
        : Reutilização em outros projetos
-- Pacotes --
-- Parte Prática --
"""

from uteis import numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')