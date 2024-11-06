import os
#Como sempre, deixo este arquivo disponível para executar no terminal do Windows. 
#Graças ao módulo "os" do sistema e a função "pause" no final, a janela do programa no terminal não fecha!

ano_Nascimento = int(input("Qual o seu ano de nascimento? ")) #mostra na tela uma requisição, via teclado, do ano de nascimento do usuário
ano_Atual = int(input("Em que ano estamos? ")) #mostra na tela uma requisição, via teclado, do ano atual ao usuário
idade = ano_Atual - ano_Nascimento #variável para armazenar idade que vai ser útil na condicional else da primeira estrutura de decisão

if(ano_Atual - ano_Nascimento >= 18):   #operação lógica que verifica se a idade do usuário é maior ou igual a 18 anos.
	print(f"Parabéns você tem {ano_Atual - ano_Nascimento} anos, Já podes tirar a carteira de motorista!")
else:  #caso não for igual ou menor que 18 anos, segue este código abaixo
	print(f"Opa! Você tem {ano_Atual - ano_Nascimento} anos, parece que você ainda não pode tirar a carteira de motorista!")
	print(f"Aguarde mais {18 - idade} anos!") #aqui mostra uma quantidade de tempo (em anos) que o usuário deve aguardar até poder tirar a carteira
if(idade >= 140):  #eu quis brincar um pouco com as limitações, caso alguém digite um valor absurdo no ano de nascimento ! :v
	print("Pera, você é um vampiro? D:")

os.system("pause")
