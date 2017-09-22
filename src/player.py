import os
from pygame import mixer

# Music Player


class Music(object):

    # inicializar mixer do pygame
    def __init__(self):
        mixer.init()

    # carregar música selecionada
    @classmethod
    def load(cls, file):
        mixer.music.load('musics/{}.mp3'.format(file).lower().replace(' ', '_'))

    # iniciar múscia
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

    # pausar música
    @classmethod
    def rewind(cls):
        Music.play()
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
    def exists(cls, name):
        if os.path.exists('musics/{}.mp3'.format(name)):
            Music.load(name)
            Music.play()
        else:
            print('Música não encontrada!')