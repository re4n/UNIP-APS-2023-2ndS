import random
import string
import time
import sys


def loading_animation():
    
    chars = "/-\|"
    for i in range(20):
        sys.stdout.write('\r')
        sys.stdout.write(f'Carregando... {chars[i % len(chars)]}')
        sys.stdout.flush()
        time.sleep(0.1)

def gen_string_key(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)) #? Retorna uma string aleatória com o tamanho do texto a ser cifrado


def convert_bin(text):
    binary = ""
    for i in text:
        decimal_value = ord(i)
        bin_value = bin(decimal_value)[2:]
        bin_value = decimal_value.zfill(8)
        binary += bin_value

    return binary #? Retorna o texto em binário

def gen_ciphertext_bin(bin_text, bin_key):
    bin_ciphertext = ""

    for i in range(len(bin_text)):
        if bin_text[i] == bin_key[i]:
            bin_ciphertext += "0"
        else:
            bin_ciphertext += "1"

    return bin_ciphertext #? Retorna o texto cifrado em binário


def bin_to_string(binary):
    bytes_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    chars = [chr(int(byte, 2)) for byte in bytes_list]

    return ''.join(chars) #? Retorna o texto cifrado em string




  




