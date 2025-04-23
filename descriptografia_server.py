import socket

# Função para descriptografar usando a cifra de César com uma chave N=5
def descriptografar_cesar(mensagem_criptografada, chave):
    mensagem_descriptografada = ""
    for caractere in mensagem_criptografada:
        if caractere.isalpha():  # Verifica se o caractere é uma letra do alfabeto
            deslocado = ord(caractere) - chave  # Calcula o deslocamento para descriptografar
            if caractere.islower():  # Se for uma letra minúscula
                if deslocado < ord('a'):  # Verifica se é menor que 'a'
                    deslocado += 26  # Volta ao fim do alfabeto
            elif caractere.isupper():  # Se for uma letra maiúscula
                if deslocado < ord('A'):  # Verifica se é menor que 'A'
                    deslocado += 26  # Volta ao fim do alfabeto
            mensagem_descriptografada += chr(deslocado)  # Adiciona o caractere descriptografado
        else:
            mensagem_descriptografada += caractere  # Mantém o caractere original se não for uma letra
    return mensagem_descriptografada

# Configuração do servidor para aguardar conexões
endereco_servidor = ('localhost', 12345)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
    servidor_socket.bind(endereco_servidor)
    servidor_socket.listen()

    print("Aguardando conexão...")
    cliente_socket, endereco_cliente = servidor_socket.accept()  # Aceita a conexão do cliente

    mensagem_criptografada = cliente_socket.recv(1024).decode()  # Recebe a mensagem criptografada
    chave_descriptografia = 5  # A chave usada para descriptografar (N=5)
    mensagem_descriptografada = descriptografar_cesar(mensagem_criptografada, chave_descriptografia)

    print("Mensagem Recebida do Cliente (Criptografada):", mensagem_criptografada)
    print("Mensagem Descriptografada:", mensagem_descriptografada)
