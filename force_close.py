# fecha programas pelo nome do executável
# diaseduardo139@gmail.com

import os
from winsound import Beep as bp

def close_app(app):
    print(f'Pedido realisado mmpara o app {app};')
    os.system('taskkill /im "{}" /f'.format(app))
    bp(800, 1000)
    return

def main():
    print('force close;'.title())
    while True:
        exe = input('Qual o nome do executável do programa que deseja fechar?')

        if '.' in exe:
            close_app(exe)

        else:
            print('Nome inválido.')
            bp(600, 1000)
            continue

        question = input('Deseja fechar outro programa? (S ou N)')
        if question.lower() == 'n':
            print('Ok, saindo...')
            break

        elif question.lower() == 's':
            os.system('cls') # limpa a tela
            bp(1500, 50)
            continue

main()