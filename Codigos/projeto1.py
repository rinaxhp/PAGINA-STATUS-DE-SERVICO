#exemplo 5 - fatorial de um numero
'''''
Crie um programa que receber um número e imprime o fatorial daquele número

#Método 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(tente explicar este problema para você mesmo em voz alta e peça mais informações/ investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários ?  --> numero
2. O que devo fazer com estes dados? --> devo calcular o fatorial do numero que for passado para o meu programa e o exibir na tela
3. Quais são as restrições deste problema ?  ---> deve ser um valor positivo, e um valor inteiro
4 Qual é o resultado esperado ? ---> exibir numero fatorial seja exibido na tela
5. Qual é sequencia de passos a ser feitas para chegar ao resultado esperado ? 
--> input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero 
 fatorial = fatorial * numero
 print(fatorial)
'''

numero = int (input('Digite um número: '))
if numero > 0:
 fatorial = 1
for item in range(1, numero +1):
 fatorial = fatorial * item
 print(fatorial)
