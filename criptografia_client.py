import socket

# Função para criptografar usando a cifra de César com uma chave N=5
def criptografar_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for caractere in mensagem:
        if caractere.isalpha():  # Verifica se o caractere é uma letra do alfabeto
            deslocado = ord(caractere) + chave  # Calcula o deslocamento da letra
            if caractere.islower():  # Se for uma letra minúscula
                if deslocado > ord('z'):  # Verifica se ultrapassou 'z'
                    deslocado -= 26  # Volta ao início do alfabeto
            elif caractere.isupper():  # Se for uma letra maiúscula
                if deslocado > ord('Z'):  # Verifica se ultrapassou 'Z'
                    deslocado -= 26  # Volta ao início do alfabeto
            mensagem_criptografada += chr(deslocado)  # Adiciona o caractere criptografado
        else:
            mensagem_criptografada += caractere  # Se não for uma letra, mantém o caractere original
    return mensagem_criptografada

# Define a mensagem a ser criptografada
mensagem = "Realizando um teste para o trabalho da Uni !"

# Criptografa a mensagem usando a função criptografar_cesar com chave 5
mensagem_criptografada = criptografar_cesar(mensagem, 5)

# Exibe a mensagem criptografada
print("Mensagem Criptografada:", mensagem_criptografada)

# Estabelece uma conexão de cliente com um servidor em 'localhost' na porta 12345
endereco_servidor = ('localhost', 12345)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
    cliente_socket.connect(endereco_servidor)  # Conecta-se ao servidor
    cliente_socket.sendall(mensagem_criptografada.encode())  # Envia a mensagem criptografada para o servidor


