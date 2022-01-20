""" Bem vindos(as) ao MyColors-terminal.

    Projeto em python para imprimir fontes coloridas usando sequências de escape ANSI no seu terminal.
    Para usar esse pequeno módulo, basta colocar o arquivo myColorsTerminal.py na pasta do seu projeto 
    e fazer as devidas importações das classes, algo do tipo assim:

    from myColorsTerminal import FONT_Colors, BACKGROUND_Colors, RESET_colors

        ft = FONT_Colors
        bg = BACKGROUND_Colors
        res = RESET_colors.reset 

        a seguir um exemplo básico do uso:
    print(f'''\n{ft.amarelo_c}Testando o {ft.vermelho_c}{bg.branco} "myColorsTerminal" {res}\n\n''')
"""

__author__ = "Claudinei Miller"
__copyright__ = "Copyright 2022, by Claudinei"
__credits__ = "ao mesmo"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Claudinei Miller"
__email__ = "claudineimiller25@gmail.com"
__status__ = "Prototype"

class FONT_Colors:                  # CORES DAS FONTES
    """Configuração das cores"""    
    black = '\033[1;30m'            # preto
    dark_red = '\033[1;31m'         # vermelho escuro
    dark_green = '\033[1;32m'       # vermelho escuro
    dark_yellow = '\033[1;33m'      # amarelo escuro
    dark_blue = '\033[1;34m'        # azul escuro
    dark_magenta = '\033[1;35m'     # magenta escuro
    dark_cyan = '\033[1;36m'        # ciano escuro
    light_gray = '\033[1;37m'       # cinza claro
    dark_gray = '\033[1;90m'        # cinza escuro
    light_red = '\033[1;91m'        # vermelho claro
    light_green = '\033[1;92m'      # verde claro
    light_yellow = '\033[1;93m'     # amarelo claro
    light_blue = '\033[1;94m'       # azul claro
    light_magenta = '\033[1;95m'    # magenta claro
    light_cyan = '\033[1;96m'       # ciano claro
    white = '\033[1;97m'            # branco
    bold = '\033[;1m'               # negrito
    invert = '\033[;7m'             # inverte


class BACKGROUND_Colors:             # CORES DE FUNDO
    """Configuração do background"""           
    black = '\033[1;40m'            # preto
    dark_red = '\033[1;41m'         # vermelho escuro
    dark_green = '\033[1;42m'       # verde escuro
    dark_yellow = '\033[1;43m'      # amarelo escuro
    dark_blue = '\033[1;44m'        # azul escuro
    dark_magenta = '\033[1;45m'     # magenta escuro
    dark_cyan = '\033[1;46m'        # ciano escuro
    light_gray = '\033[1;47m'       # cinza claro
    dark_gray = '\033[1;100m'       # cinza escuro
    light_red = '\033[1;101m'       # vermelho claro
    light_green = '\033[1;102m'     # verde claro
    light_yellow = '\033[1;103m'    # amarelo claro
    light_blue = '\033[1;104m'      # azul claro
    light_magenta = '\033[1;105m'   # magenta claro
    light_cyan = '\033[1;106m'      # ciano claro
    white = '\033[1;107m'           # branco


class RESET_colors:
    """Configuração do reset"""     # RESETA AS CORES
    reset = '\033[0;0m'             # resete

print()