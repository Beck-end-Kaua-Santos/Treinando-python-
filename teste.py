Entrada = input('[E] para Entrar [S] para sair:')

if Entrada == 'E':
    print('Voce entrou no Sistema')
elif Entrada == 'S':
    print('Voce saiu do Sistema')
    exit() 
else:
    print('Senha Invalida')
    
Senha = input('Digite a Senha para entrar no Sistema:')
Senha_correta = '213969'

if Senha == Senha_correta: 
    print('senha correta!')
else:
    print('senha incorreta')
    
Saida = input('Voce deseja continuar ou sair do sistema? [C] ou [S]:')
if Saida == 'C':
    print('Voce ainda Esta no Sistema')
else: 
    print('Voce saiu do Sistema')
    exit()
Num1 = int(input('Digite um valor:'))
Num2 = int(input('Digite um valor:'))
Num3 = int(input('digite um valor:'))

media = (Num1 + Num2 + Num3)/2
print('Esse é a media do Aluno:', media)
Saida = input('Voce deseja continuar ou sair do sistema? [C] ou [S]:')
if Saida == 'C':
    print('Voce ainda Esta no Sistema')
else: 
    print('Voce saiu do Sistema')