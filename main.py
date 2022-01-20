""" Bem vindos(as) ao YoutubeDown_T.

    Projeto em python para fazer downloads de vídeos do youtube em formato mp4(somente audio), ou mp4(audio e vídeo)

"""

__author__ = "Claudinei Miller"
__copyright__ = "Copyright 2022, by Claudinei"
__credits__ = "ao mesmo"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Claudinei Miller"
__email__ = "claudineimiller25@gmail.com"
__status__ = "Prototype"


import os
import sys
import requests

from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from time import sleep
from myColorsTerminal import FONT_Colors, BACKGROUND_Colors, RESET_colors

sys.stdout.write("\x1b]2;Run YoutubeDown_T in Terminal\x07")

ft = FONT_Colors
bg = BACKGROUND_Colors
res = RESET_colors.reset


class App:
    """A classe 'App' é a classe onde tudo acontece"""

    def __init__(self):
        self.list_menu = [
            ['Baixar apenas 1 vídeo', 'Baixar playlist completa', 'Sair'],
            ['Baixar apenas audio', 'Baixar vídeo completo', 'Sair']]

    def clear(self):
        '''Pequena função para limpar o terminal'''
        os.system('clear')

    def title_init(self):
        '''Exibe o cabeçalho de apresentação do projeto'''
        self.clear()
        print(f"\t{ft.dark_yellow}{62 * '-'}\n\t|{'DOWLOADS DE VÍDEOS DO YOUTUBE USANDO PYTHON/PYTUBE '.center(60)}|\n\t|{'Developed by:'.rjust(15)} {ft.light_blue}{'claudineimiller25@gmail.com'.ljust(28)}{res}{ft.dark_yellow}- version 1.0   |\n\t{62 * '-'}{res}\n\n")

    def menu_apresentation(self, lista):
        '''Apresenta o menu na tela, logo abaixo do cabeçalho'''
        self.title_init()
        for cont, option in zip(range(1, len(lista)+1), lista):
            print(
                f'\t{ft.light_yellow}[{cont}]{res} {ft.light_green}{option}{res}')
        print('\n')

    def get_option_menu(self):
        '''Função para capturar as opções escolhidas pelo usuário'''
        self.list_temp = []
        cont = 0

        while cont < 2:
            self.menu_apresentation(self.list_menu[cont])
            try:
                get_menu = int(input('\t>>> '))

                if get_menu > 3 or get_menu < 1:
                    print(
                        f'\t{bg.dark_red}{ft.white}A opção{res}{bg.dark_red}{ft.dark_cyan} "{get_menu}" {res}{bg.dark_red}{ft.white}é inválida, tente novamente.{res}')
                    sleep(3)
                    self.menu_apresentation(self.list_menu[0])
                elif get_menu == 3:
                    self._exit()
                else:
                    self.list_temp.append(get_menu)
                    cont += 1

            except ValueError:
                print(
                    f'\t{bg.dark_red}{ft.white}Opção inválida, tente novamente.{res}')
                sleep(3)
                self.menu_apresentation(self.list_menu[0])

        return self.list_temp

    def download_one_video(self, url):
        '''Função que faz o download de apenas 1 vídeo'''

        yt = YouTube(url, on_progress_callback=on_progress)

        list_description = ['Título do vídeo:', 'Visualizações:',
                            'Duração:', 'Publicado em:', 'classificação:', 'Descrição:']
        list_functions = [yt.title, yt.views, yt.length,
                          yt.publish_date, yt.rating, yt.description]

        for description, functions in zip(list_description, list_functions):
            print(
                f'\t{ft.light_yellow}{description.rjust(16)}{res} {ft.light_green}{functions}{res}')

        if self._format == 'audio':
            print(f'\tBaixando o vídeo {yt.title} no formato "mp4"(audio)')
            yt.streams.filter(only_audio=True).first().download(
                output_path='Downloads_audios')
        else:
            print(
                f'\n\tBaixando o vídeo {yt.title} no formato "mp4"(vídeo)\n\n')
            yt.streams.filter(file_extension='mp4').first().download(
                output_path='Downloads_videos')

    def download_playlist(self, url):
        '''Função que faz o download da playlist completa'''
        playlist = Playlist(url)

        print(f'''
        {ft.light_yellow}Nome da playlist:{res} {ft.light_green}{playlist.title}{res}
        {ft.light_yellow}Total de vídeos:{res} {ft.light_green}{playlist.length}{res}
        {ft.light_yellow}Total de visualizações:{res} {ft.light_green}{playlist.views}{res}
        ''')

        list_links = []
        playlist_title = playlist.title.title()

        for _url in playlist.video_urls:
            list_links.append(_url)

        if self._format == 'audio':
            print(
                f'\tBaixando a playlist {playlist.title} no formato "mp4"(áudio)')
            for video in playlist.videos:
                video.register_on_progress_callback(on_progress)
                video.streams.filter(only_audio=True).first().download(
                    output_path='Playlists/Audios/'+playlist_title)
        else:
            print(
                f'\tBaixando a playlist {playlist.title} no formato "mp4"(vídeo)')
            for video in playlist.videos:
                video.streams.filter(file_extension='mp4').first().download(
                    output_path='Playlists/Videos/'+playlist_title)

    def download(self):
        '''Função que chama a função de download de 1 vídeo, ou download da playlist inteira, ista baseado na escolha do usuário'''
        list_options = self.get_option_menu()

        self._format = 'audio' if list_options[1] == 1 else "video"
        user_option = 'video' if list_options[0] == 1 else 'playlist'

        self.title_init()
        print(f'\t{ft.light_blue}Informe abaixo a url do(a) {user_option}:{res}\n')
        url = str(input('\t>>> '))
        self.title_init()

        try:
            if user_option == 'video':
                self.download_one_video(url)
            else:
                self.download_playlist(url)

            print(
                f'\n\n\t{bg.dark_blue}{ft.white}Download finalizado com sucesso.{res}\n\n')
        except Exception as error:
            self.title_init()
            print(
                f'''
        Não foi possível realizar o download pois o seguinte erro foi gerado:
        {ft.light_red}"{error}"{res}
        Informe ao desenvolvedor o erro gerado para que mesmo possa ser ajustado.
        Isto é constrangedor, mas acontece quando o Youtube faz alguma alteração em seu código.
        \n\n''')

    def check_internet(self):
        '''Função que checa a conexão com a internet'''

        url = 'https://www.google.com'
        timeout = 5
        try:
            requests.get(url, timeout=timeout)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def _exit(self):
        '''Função para sair do programa'''
        self.clear()
        sys.exit()


if __name__ == '__main__':
    app = App()

    if not app.check_internet():
        app.title_init()
        print(
            f'\t\t{bg.dark_red}{ft.white} Sem conexão com a internet, favor verificar. {res}\n\n')
    else:
        app.download()
