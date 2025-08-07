#condicionais
#if, elif e else
'''''
Eu cheguei atrasado na aula, ainda posso entrar?
se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrario ira tomar uma suspensão
'''

numero_de_atrasos = 5
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1: #são executados caso os if não tenha executado
    print('Pode entrar, porém caso tome mais 2 falas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 falta, irá ser expulso')
else:
    print('Pode entrar')
