'''''
Escreva um programa que ao inciar gera um valor aleatorio de 1 a 10 e permite que o usuario 
chute um numero até que o valor aleatorio gerado no inicio do programa seja chutado corretamente.
O programa deve informar se o chute foi acima, abaixo ou igual valor aleatorio gerado no iniciou do programa.
'''
import random

valor_aleatorio = random.randint(1,10) #gerando valor aleatorio através da biblioteca py
chute = int(input('Chute um valor de 1 a 10: '))
acertou = False
while acertou == False:
 chute = int(input('Chute um valor de 1 a 10: '))
 if chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado')
 elif chute > valor_aleatorio:
    print("Chute foi maior que o valor gerado")
 elif chute == valor_aleatorio:
    print("Você acertou!")


