## Leonardo Stella de Oliveira
## 14/12/2022
## atividade do curso de cibersegurança da dio

import os ##importar o sistema operacional
import pyaes ##importar a biblioteca de criptografia
#abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll' ##vai receber o nome do arquivo
file = open(file_name, 'rb') ##ler o arquivo
file_data = file.read() ##para setar o que foi lido no file_data
file.close() ##então, fehcar o arquivo

#chave de descriptografia
key = b'testeransomwares' ##receber a chave
aes = pyaes.AESModeOfOperationCTR(key) ##utiliza a descriptografia através do cálculo
decrypt_data = aes.decrypt(file_data) ##então, descriptografa passando o conteúdo do arquivo que foi lido anteriormente

##remover o arquivo criptografado
os.remove(file_name) ##remove o arquivo com o nome setado, por isso importar o sistema operacional (os)

##criar um novo arquivo descriptografado
new_file = 'teste.txt' ##dá o nome pro arquivo que vai ser criado
new_file = open(f'{new_file}','wb') ##abre o arquivo criado
new_file.write(decrypt_data) ##decripta dentro do arquivo novo
new_file.close() ##aqui fecha o arquivo 
