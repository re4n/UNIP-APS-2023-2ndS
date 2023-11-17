import functions

print("\t -==Criptografia==-\n")

# Entrada do texto para ser criptografado
try:
    texto = input("Digite um texto: ")

    if len(texto) > 128:
        raise NameError("String longer than 128 characters")

except NameError:
    raise

try:
    # ? Caso o texto for uma string vazia
    if len(texto) == 0:
        raise NameError("Empty String")
except NameError:
    raise

try:
    # Entrada da chave
    texto_chave = input("Digite a chave: ")

    while True:
        try:
            # ? Caso a chave for uma string vazia
            if len(texto_chave) == 0:
                raise NameError("Empty Key")
        except NameError:
            raise

        if " " in texto_chave:
            # ? Retira os espaços da string
            texto_chave = texto_chave.replace(" ", "")
        elif len(texto_chave) < len(texto):
            # ? Caso a chave for menor que o texto, complementa a chave fornecida com caracteres aleatórios
            tamanho_chave = len(texto) - len(texto_chave)
            texto_chave += functions.gen_string_key(tamanho_chave)
        elif len(texto_chave) > len(texto):
            # ? Caso a chave for maior que o texto, retira os caracteres excedentes da chave
            texto_chave = texto_chave[:len(texto)]


        else:
            break
except:
    raise

# Convertendo o texto e a chave para binário
texto_bin = functions.convert_bin(texto)
texto_chave_bin = functions.convert_bin(texto_chave)

# Gerando o texto cifrado em binário
texto_cifrado_bin = functions.gen_ciphertext_bin(texto_bin, texto_chave_bin)

# Convertendo o texto cifrado em binario para string
texto_cifrado = functions.bin_to_string(texto_cifrado_bin)

print("\nTexto: ", texto, len(texto))
print("\n")

functions.loading_animation()

# Resultado:
print("\n\nTexto cifrado: \n")
print(texto_cifrado, len(texto_cifrado))
descriptografado = functions.gen_ciphertext_bin(texto_cifrado_bin, texto_chave_bin)
descriptografado = functions.bin_to_string(descriptografado)
print("\nTexto descriptografado: ", descriptografado)

print("\n\n")
print("\tFIM DO PROGRAMA")