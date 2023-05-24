import random

print('Seja Bem Vindo ao Jogo Adivinha o Número da Valquiria!')
escolha_num = input('Digite o número teto do desafio: ')

# A função (.isdigit) verifica se o que está dentro dos parêntes é um número ou outra.coisa
if escolha_num.isdigit():
    escolha_num = int(escolha_num)
else:
    print('Erro: valor informado não é numérico. Favor execute novamente e informe um número!')
    quit()

random_number = random.randint(0, escolha_num)
n_escolha = 0

while True:
    usuario_responde = input('Adivinha o número: ')

    if usuario_responde.isdigit():
        usuario_responde = int(usuario_responde)
    else:
        print('Erro: valor informado não é numérico. Favor informe um número!')
        continue

    n_escolha = n_escolha + 1
    if usuario_responde == random_number:
        print('Acertou!')
        break
    elif usuario_responde > random_number:
        print('Chutou alto, o número randomico é menor que isso...')
    else:
        print('Chutou baixo, o número randomico é maior que isso...')
print('N° de tentativas: '+ str(n_escolha))


