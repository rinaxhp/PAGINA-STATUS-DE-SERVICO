#laços de repetição + lista --> são maneiras de executar comando varias vezes
'''''
print('Carregando')
print('Carregando')
print('Carregando')
'''


for palavra in range(1,4):
    print('Carregando')
    '''
    for item coleção: ----> ex: nossa coleção seria nome, então ira pegar versão plural e ela no singular como feito abaixo!!
        espressão
    '''
    for item in range(1,21):
        print(item)
    for item in range(1,20,2):
        print(item)

nomes = ['Ana','Clara', 'Jhonatan', 'Diego', 'Carlos']
for nome in nomes:
   print(nome)