import random

MAXIMO_LINHAS = 3
MAXIMO_APOSTA = 100
MINIMO_APOSTA = 5

ROWS = 3
COLS = 3

quantidade_simbolos = {'A': 2, 'B': 4, 'C': 6, 'D': 8}

valor_simbolos = {'A': 5, 'B': 4, 'C': 3, 'D': 2}

def check_win(colunas, linhas, aposta, valor):
    win = 0
    win_lines= []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_check = coluna[linha]
            if simbolo != simbolo_check:
                break
        else: 
            win += valor[simbolo] * aposta
            win_lines.append(linhas + 1)

    return win, win_lines

def get_maquina_cassino(rows, cols, simbolo):
    all_simbolo = []
    for simbolo, quantidade_simbolos in simbolo.items():
        for _ in range(quantidade_simbolos):
            all_simbolo.append(simbolo)


    colunas = []
    for _ in range (cols):
        coluna = []
        current_symbols = all_simbolo[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coluna.append(value)
        colunas.append(coluna)
    return colunas


def print_maquina(colunas):
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[row], end=" | ")
            else:
                print(coluna[row], end="")
        
        print()


def deposit():
    while True:
        quantia = input('Quanto você gostaria de depositar? R$')
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 0:
                break
            else:
                print('a quantia deve ser maior que 0')
        else: 
            print('Por favor, digite um número.')
    return quantia 

def pegar_linhas():
    while True:
        linhas = input("em quantas linhas você quer apostar (1-" + str(MAXIMO_LINHAS) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1<= linhas <= MAXIMO_LINHAS:
                break
            else:
                print('Digite um valor entre 1 e ' + str(MAXIMO_LINHAS))
        else: 
            print('Por favor, digite um número.')
    return linhas 
def get_aposta():
    while True:
        quantia = input('Quanto você gostaria de apostar? R$')
        if quantia.isdigit():
            quantia = int(quantia)
            if MINIMO_APOSTA <= quantia <= MAXIMO_APOSTA:
                break
            else:
                print(f'a quantia deve ser entre R${MINIMO_APOSTA} - R${MAXIMO_APOSTA}')
        else: 
            print('Por favor, digite um número.')
    return quantia 



def spin(poupança):
    linhas = pegar_linhas()
    while True:
        aposta = get_aposta()
        total_aposta = aposta * linhas
        if total_aposta > poupança:
            print(f"Você não saldo suficiente para apostar, seu saldo é:  R${poupança}")
        else:
            break
    print(f"Você está apostando R${aposta} em {linhas} linhas. O total da aposta é igual a: R${total_aposta}")

    slots = get_maquina_cassino(ROWS, COLS, quantidade_simbolos)
    print_maquina(slots)
    win, win_lines = check_win(slots, linhas, aposta, valor_simbolos)
    print(f"voce ganhou R${win}")
    print(f"Você ganhou na linha", *win_lines)
    return win - total_aposta

def main():
    poupança = deposit()
    while True:
        print(f"A poupança atual é de R${poupança}")
        resposta = input("Clique enter para girar (q to quit)")
        if resposta == "q":
            break
        poupança += spin(poupança)
    
    print(f"Você saiu com R${poupança}")


main()


