'''''
 Projeto - Medidor de Velocidade

 Levando em consideração a velocidade maxima permitida de 80km em uma determinada rua. Crie um programa que recebe usuario
 um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave, gravissima.
 Levando em consideração que se a pessoa estiver abaixo da velocidade maxima seu programa deve exibir "Não houve multa", caso esteja
 a 10 km acima, deve exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade maxima, exiba: "levou multa gravissima".
 '''

velocidade_maxima = 80
velocidade = int(input('Digite sua velocidade: '))
if velocidade_maxima <= velocidade:
 print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
 print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima  + 20:
 print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
 print('Levou multa gravissima')