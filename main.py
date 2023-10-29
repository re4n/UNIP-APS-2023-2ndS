import functions

# Gerando a chave aleatória
texto = "The quick brown fox jumps over the lazy dog"
texto_chave = functions.gen_string_key(len(texto))

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