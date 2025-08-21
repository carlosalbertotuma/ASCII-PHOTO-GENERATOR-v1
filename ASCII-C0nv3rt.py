#!/usr/bin/env python3
import sys
from PIL import Image

# Banner
BANNER = r"""
    #     #####   #####  ### ###    ######                             
   # #   #     # #     #  #   #     #     # #    #  ####  #####  ####  
  #   #  #       #        #   #     #     # #    # #    #   #   #    # 
 #     #  #####  #        #   #     ######  ###### #    #   #   #    # 
 #######       # #        #   #     #       #    # #    #   #   #    # 
 #     # #     # #     #  #   #     #       #    # #    #   #   #    # 
 #     #  #####   #####  ### ###    #       #    #  ####    #    ####  
                                                                       
                                                                       
  ####  ###### #    # ###### #####    ##   #####  ####  #####          
 #    # #      ##   # #      #    #  #  #    #   #    # #    #         
 #      #####  # #  # #####  #    # #    #   #   #    # #    #         
 #  ### #      #  # # #      #####  ######   #   #    # #####          
 #    # #      #   ## #      #   #  #    #   #   #    # #   #          
  ####  ###### #    # ###### #    # #    #   #    ####  #    #         
                                                                       

       [*] ASCII PHOTO GENERATOR v.0.1 [*]
       [*]   Carlos Tuma - Bl4dsc4n    [*]

"""

print(BANNER)

# Verifica argumentos
if len(sys.argv) < 2:
    print("Uso: python3 aaa.py <imagem>")
    sys.exit(1)

image_path = sys.argv[1]

# Carregar imagem e converter para tons de cinza
img = Image.open(image_path).convert("L")
img = img.resize((80, 40))  # Ajuste o tamanho como quiser

# Caracteres do mais escuro (preto) para o mais claro (branco)
ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = int(pixel / 255 * (len(ASCII_CHARS) - 1))  # Garante índice válido
        ascii_str += ASCII_CHARS[index]
    return ascii_str

ascii_image = pixel_to_ascii(img)

# Exibir em linhas
for i in range(0, len(ascii_image), img.width):
    print(ascii_image[i:i + img.width])
