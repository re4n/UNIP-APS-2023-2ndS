import random
import string

def gen_string_key(tamanho):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho)) #? Retorna uma string aleatória com o tamanho do texto a ser cifrado


def convert_bin(texto):
    binario = ""
    for i in texto:
        valor_decimal = ord(i)
        valor_binario = bin(valor_decimal)[2:]
        valor_binario = valor_binario.zfill(8)
        binario += valor_binario

    return binario #? Retorna o texto em binário

def gen_ciphertext_bin(bin_text, bin_key):
    bin_ciphertext = ""

    for i in range(len(bin_text)):
        if bin_text[i] == bin_key[i]:
            bin_ciphertext += "0"
        else:
            bin_ciphertext += "1"

    return bin_ciphertext #? Retorna o texto cifrado em binário


def binario_para_string(binario):
    bytes_list = [binario[i:i+8] for i in range(0, len(binario), 8)]
    caracteres = [chr(int(byte, 2)) for byte in bytes_list]

    return ''.join(caracteres) #? Retorna o texto cifrado em string




  




