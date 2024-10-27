import os
# Aqui eu importei o módulo "os" do Windows, para usar a função "pause" do sistema operacional.

print('Olá, mundo!') # função print para gerar a sáida e mostrar a mensagem que está entre aspas simples

os.system("pause") # O python se comunica com sistema operacional Windows para utilizar o comando pause

'''
Foi uma alternativa bacana que encontrei para que a janela do terminal não fechasse logo após executar 
o arquivo. 
Aqui o comando pause é colocado entre aspas porque estamos passando o comando pause como uma string para a
função os.system()
Se não fosse colocado entre aspas o Python iria interpretar como uma variável ou função ao invés de um
comando do sistema
'''
