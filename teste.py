# Entrada = input('[E] para Entrar [S] para sair:')

# if Entrada == 'E':
#     print('Senha de Acesso')
# elif Entrada == 'S':
#     print('Voce saiu do Sistema')
#     exit() 
# else:
#     print('Senha Invalida')
    
# Senha = input('Digite a Senha para entrar no Sistema:')
# Senha_correta = '213969'

# if Senha == Senha_correta: 
#     print('senha correta!')
# else:
#     print('senha incorreta')
# Num1 = int(input('Digite um valor:'))
# Num2 = int(input('Digite um valor:'))
# Num3 = int(input('digite um valor:'))

# media = (Num1 + Num2 + Num3)/2
# print('Esse é a media do Aluno:', media)

# Saida = input('Voce deseja continuar ou sair do sistema? [C] ou [S]:')
# if Saida == 'C':
#     print('Voce ainda Esta no Sistema')
# else: 
#     print('Voce saiu do Sistema')
    
# Saida = input('Voce deseja continuar ou sair do sistema? [C] ou [S]:')
# if Saida == 'C':
#     print('Voce ainda Esta no Sistema')
# else: 
#     print('Voce saiu do Sistema')
#     exit()
# Num1 = int(input('Digite um valor:'))
# Num2 = int(input('Digite um valor:'))
# Num3 = int(input('digite um valor:'))

# media = (Num1 + Num2 + Num3)/2
# print('Esse é a media do Aluno:', media)
# Saida = input('Voce deseja continuar ou sair do sistema? [C] ou [S]:')
# if Saida == 'C':
#     print('Voce ainda Esta no Sistema')
# else: 
#     print('Voce saiu do Sistema')
# def adicionar(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# def multiplicar(x, y):
#     return x * y

# def dividir(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Erro: Divisão por zero!"

# while True:
#     print("\nSelecione a operação:")
#     print("1. Adição")
#     print("2. Subtração")
#     print("3. Multiplicação")
#     print("4. Divisão")
#     print("5. Sair")

#     operacao = input("Digite o número da operação (1/2/3/4/5): ")

#     if operacao == '5':
#         print("Saindo da calculadora.")
#         break  # Sai do loop

#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))

#     if operacao == '1':
#         print(f"{num1} + {num2} = {adicionar(num1, num2)}")
#     elif operacao == '2':
#         print(f"{num1} - {num2} = {subtrair(num1, num2)}")
#     elif operacao == '3':
#         print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
#     elif operacao == '4':
#         print(f"{num1} / {num2} = {dividir(num1, num2)}")
#     else:
#         print("Operação inválida!")



# while True:
#     secreto = int(input("digite um numero de 0 a 20 até acertar!"))
#     numero = 14
#     if secreto == numero:
#         print("voce acertou o numero secreto!")
#         break
#     else:
#         print("vc errou, tente novamente!")

import random

def escolher_palavra():
    palavras = ["abacaixi", "amora", "leite", "mercado", "faculade"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
    ]
    return estagios[tentativas]

def jogar():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6


    while tentativas > 0:
        print(exibir_forca(tentativas))
        print("Palavra:", " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra]))
        print("Tentativas restantes:", tentativas)
        print("Letras já adivinhadas:", " ".join(letras_adivinhadas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra!")
        elif letra in palavra:
            letras_adivinhadas.append(letra)
            print("Boa! A letra está na palavra.")
        else:
            letras_adivinhadas.append(letra)
            tentativas -= 1
            print("Oops! A letra não está na palavra.")

        # Verifica se o jogador adivinhou todas as letras
        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"Parabéns! Você adivinhou a palavra: {palavra}")
            break
    else:
        print(exibir_forca(tentativas))
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()

