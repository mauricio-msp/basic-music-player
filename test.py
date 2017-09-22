"""
Aplicação simples e básica em Python 3 desenvolvido
no conceito de POO(Programação Orientada a Objetos)
usando como abstração a 'música' como exemplo, onde
você pode inicia-lá, pausar, retomar de onde parou,
parar, alterar volume, mostrar volume e reinicia-lá.
"""
from src.player import Music

music = Music()

print('1 - Carregar/Iniciar música')
print('2 - Parar música')
print('3 - Pausar música')
print('4 - Retomar música')
print('5 - Reiniciar música')
print('6 - Alterar volume')
print('7 - Mostrar volume')
print('8 - Sair')

while True:
    option = int(input('\nEscolha uma das opções: '))

    if option == 1:
        name = str(input('Informe o nome da música: '))
        music.exists(name)
    elif option == 2:
        music.stop()
    elif option == 3:
        music.pause()
    elif option == 4:
        music.resume()
    elif option == 5:
        music.rewind()
    elif option == 6:
        valor = float(input('Informe o volume da música entre 0.0 até 1.0: '))
        music.set_volume(valor)
    elif option == 7:
        music.get_volume()
    elif option == 8:
        break
    else:
        print('Opção inválida!')