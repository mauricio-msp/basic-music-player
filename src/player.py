import os
from pygame import mixer

# Music Player


class Music(object):

    # inicializar mixer do pygame
    def __init__(self):
        mixer.init()

    # carregar música selecionada
    @classmethod
    def load(cls, path, file):
        mixer.music.load('{}/{}.mp3'.format(path, file))

    # iniciar música
    @classmethod
    def play(cls):
        mixer.music.play()

    # pausar música
    @classmethod
    def pause(cls):
        mixer.music.pause()

    # retomar música
    @classmethod
    def resume(cls):
        mixer.music.unpause()

    # reiniciar música
    @classmethod
    def rewind(cls):
        mixer.music.rewind()

    # parar música
    @classmethod
    def stop(cls):
        mixer.music.stop()

    # alterar volume - 0.0 até 1.0
    @classmethod
    def set_volume(cls, value):
        mixer.music.set_volume(value)

    # mostra o volume da música
    @classmethod
    def get_volume(cls):
        print('Volume atual: {:.2f}'.format(mixer.music.get_volume()))

    # verifica se a música existe no diretório /musics/
    @classmethod
    def is_valid(cls, dir_name, file_name):
        if os.path.isdir(dir_name):
            if os.path.exists('{}/{}.mp3'.format(dir_name, file_name)):
                Music.load(dir_name, file_name)
                Music.play()
            else:
                print('Música não encontrada!')
        else:
            print('o diretório \033[33m{}\033[m não existe!'.format(dir_name))