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
from numpy import around
import requests

from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from time import sleep
from myColorsTerminal import FONT_Colors, BACKGROUND_Colors, RESET_colors

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

sys.stdout.write("\x1b]2;Run YoutubeDown_T in Terminal\x07")

ft = FONT_Colors
bg = BACKGROUND_Colors
res = RESET_colors.reset


class App:
    """A classe 'App' é a classe onde tudo acontece"""

    def __init__(self):
        self.list_menu = [
            ['Baixar apenas 1 vídeo', 'Baixar playlist completa', 'Sair'],
            ['Baixar apenas o audio (formato mp3)', 'Baixar vídeo completo (formato mp4)', 'Sair']]

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

        try:
            _title = yt.title
        except:
            _title = 'Nenhum titulo definido'
        try:
            _views = yt.views
        except:
            _views = 'Indefinido'
        try:
            _length = yt.length
        except:
            _length = 'Indefinido'
        try:
            _publish_date = yt.publish_date
        except:
            _publish_date = 'Indefinido'
        try:
            _rating = yt.rating
        except:
            _rating = 'Indefinido'
        try:
            _description = yt.description
        except:
            _description = 'Indefinido'

        list_description = ['Título do vídeo:', 'Visualizações:',
                            'Duração:', 'Publicado em:', 'classificação:', 'Descrição:']
        list_functions = [_title, _views, around(_length / 60, 2),
                          _publish_date, _rating, _description]

        for description, functions in zip(list_description, list_functions):
            print(
                f'\t{ft.light_yellow}{description.rjust(16)}{res} {ft.light_green}{functions}{res}')

        if self._format == 'audio':
            print(f'\tBaixando o vídeo {yt.title} no formato "mp4"(audio)')
            yt.streams.filter(only_audio=True).first().download(
                output_path='Downloads_audios', filename='.'+yt.title+'.mp4')

            self.convert_mp4_to_mp3(
                f'Downloads_audios/.{yt.title}.mp4', f'Downloads_audios/{yt.title}.mp3')
            self.delete_file(f'Downloads_audios/.{yt.title}.mp4')
        else:
            print(
                f'\n\tBaixando o vídeo {yt.title} no formato "mp4"(vídeo)\n\n')
            yt.streams.filter(file_extension='mp4').first().download(
                output_path='Downloads_videos')

    def download_playlist(self, url):
        '''Função que faz o download da playlist completa'''
        playlist = Playlist(url)

        try:
            playlist_title = playlist.title
        except:
            playlist_title = 'Nenhum titulo definido'
        try:
            playlist_length = playlist.length
        except:
            playlist_length = 'Indefinido'
        try:
            playlist_views = playlist.views
        except:
            playlist_views = 'Nenhuma Visualização'

        print(f'''
        {ft.light_yellow}Nome da playlist:{res} {ft.light_green}{playlist_title}{res}
        {ft.light_yellow}Total de vídeos:{res} {ft.light_green}{playlist_length}{res}
        {ft.light_yellow}Total de visualizações:{res} {ft.light_green}{playlist_views}{res}
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

            print('\n\n\tConvertendo arquivos para mp3, aguarde...\n\n')

            for files in self.list_files('Playlists/Audios/'+playlist_title):
                self.convert_mp4_to_mp3(files, f'{files}.mp3')
                self.delete_file(files)

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
        user_option = 'Informe abaixo a url do video:' if list_options[
            0] == 1 else 'Informe abaixo a url da playlist'

        self.title_init()
        print(f'\t{ft.light_blue}{user_option}{res}\n')
        url = str(input('\t>>> '))
        self.title_init()

        try:
            if YouTube(url):
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
        except:
            self.title_init()
            print(f'\t{bg.dark_red}{ft.white} A url informada é inválida {res}\n\n')

            

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

    def convert_mp4_to_mp3(self, path_mp4, path_mp3):
        try:
            mp4_without_frames = AudioFileClip(path_mp4)
            mp4_without_frames.write_audiofile(path_mp3)
            mp4_without_frames.close()
        except Exception as error:
            self.title_init()
            print(
                f'''
        Não foi possível realizar o download pois o seguinte erro foi gerado:
        {ft.light_red}"{error}"{res}
        Informe ao desenvolvedor o erro gerado para que mesmo possa ser corrijido.
        \n\n''')

    def delete_file(self, path_file):
        if os.path.exists(path_file):
            os.remove(path_file)

    def list_files(self, path):
        listFiles = []

        os.chdir(path)
        [listFiles.append(files)
         for files in os.listdir() if files.endswith('.mp4')]

        return listFiles


if __name__ == '__main__':
    app = App()

    if not app.check_internet():
        app.title_init()
        print(
            f'\t\t{bg.dark_red}{ft.white} Sem conexão com a internet, favor verificar. {res}\n\n')
    else:
        app.download()
