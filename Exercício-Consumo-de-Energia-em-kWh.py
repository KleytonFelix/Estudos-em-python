import os
"""
Programa que calcula o preço a pagar pelo fornecimento de energia elétrica.
As variáveis de entrada são o consumo em kWh e o tipo de instalação do cliente.
R para residências, I para indústrias e C para comércios

"""

"""
#################################################################
#                                                               # 
#             PREÇO POR TIPO E FAIXA DE CONSUMO                 # 
#                                                               # 
#################################################################
#      TIPO      #      FAIXA (kWh)      #      Preço (R$)      #     
#################################################################
#                #       Até 500         #                      # 
#                #                       #        0,40          #
#  Residencial   ################################################ 
#                #      Acima de 500     #                      # 
#                #                       #        0,65          # 
#################################################################
#                #       Até 1000        #                      #
#                #                       #        0,55          #  
#  Comercial     ################################################ 
#                #      Acima de 1000    #                      # 
#                #                       #        0,60          #
#################################################################
#                #       Até 5000        #                      #
#                #                       #        0,55          #
#  Industrial    ################################################
#                #      Acima 5000       #                      #
#                #                       #        0,60          #
#################################################################

"""

consumo = int(input("Quanto de energia (em kWh) foi consumido no mês? "))
print("1 - Residencial ")
print("2 - Comercial ")
print("3 - Industrial ")
tipo = int(input("Qual o seu tipo de instalação? "))

if(tipo == 1 ):
    if(consumo <= 500):
        total = float(consumo * 0.40)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel residencial, total a pagar: R$ {total:.2f}")
    else:
        total = float(consumo * 0.65)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel residencial, total a pagar: R$ {total:.2f}")
elif(tipo == 2):
    if(consumo <= 1000):
        total = float(consumo * 0.55)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel comercial, total a pagar: R$ {total:.2f}")
    else:
        total = float(consumo * 0.60)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel comercial, total a pagar: R$ {total:.2f}")
elif(tipo == 3):
    if(consumo <= 5000):
        total = float(consumo * 0.55)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel Industrial, total a pagar: R$ {total:.2f}")
    else:
        total = float(consumo * 0.60)
        print(f"Você consumiu {consumo}kWh este mês em seu imóvel Industrial, total a pagar: R$ {total:.2f}")
else:
    print("Opa! Opção escolhida inválida!")

os.system("pause")
