import functions

print("\t -==Criptografia==-\n")
texto = "The quick brown fox jumps over the lazy dog"
# texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum sem, lacinia vitae gravida ac, elementum non viverra."
texto_chave = input("Digite a chave: ")

while True:
        # Verificando se a chave contem espaços.
    if " " in texto_chave:
            texto_chave = texto_chave.replace(" ", "")
    if len(texto_chave) < len(texto):

        tamanho_chave = len(texto) - len(texto_chave)
        texto_chave += functions.gen_string_key(tamanho_chave)

    elif len(texto_chave) > len(texto):
        texto_chave = texto_chave[:len(texto)]
    else:
        # Convertendo o texto e a chave para binário
        texto_bin = functions.convert_bin(texto)
        texto_chave_bin = functions.convert_bin(texto_chave)

        # Gerando o texto cifrado em binário
        texto_cifrado_bin = functions.gen_ciphertext_bin(texto_bin, texto_chave_bin)

        # Convertendo o texto cifrado em binario para string
        texto_cifrado = functions.binario_para_string(texto_cifrado_bin)

        print("Texto: ", texto, len(texto))
        print("Chave: ", texto_chave, len(texto_chave))
        print("Texto cifrado: ", texto_cifrado, len(texto_cifrado))

        # Resultado:
        descriptografado = functions.gen_ciphertext_bin(texto_cifrado_bin, texto_chave_bin)
        descriptografado = functions.binario_para_string(descriptografado)
        print("Texto descriptografado: ", descriptografado, len(descriptografado))

        print("\n\n")
        print("\tFIM DO PROGRAMA")
        break
