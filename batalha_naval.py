import random
import string

# Configurações do jogo
TAMANHO = 10
NUM_NAVIOS = 5

def criar_tabuleiro():
    return [["~"] * TAMANHO for _ in range(TAMANHO)]

def imprimir_tabuleiro(tabuleiro, mostrar_navios=False):
    print("   " + " ".join(string.ascii_uppercase[:TAMANHO]))
    for i, linha in enumerate(tabuleiro):
        linha_str = " ".join(
            c if (c != "N" or mostrar_navios) else "~" for c in linha
        )
        print(f"{i:2} {linha_str}")

def posicionar_navios(tabuleiro):
    for _ in range(NUM_NAVIOS):
        while True:
            x, y = random.randint(0, TAMANHO-1), random.randint(0, TAMANHO-1)
            if tabuleiro[x][y] == "~":
                tabuleiro[x][y] = "N"
                break

def jogar():
    tabuleiro = criar_tabuleiro()
    posicionar_navios(tabuleiro)
    tentativas = 0
    acertos = 0

    print("🎯 Bem-vindo ao Batalha Naval!")
    print("Digite coordenadas no formato A5 (coluna + linha).")
    imprimir_tabuleiro(tabuleiro)

    while acertos < NUM_NAVIOS:
        tentativa = input("\nDigite sua jogada: ").upper().strip()
        if len(tentativa) < 2:
            print("Entrada inválida! Exemplo válido: B3")
            continue

        coluna, linha = tentativa[0], tentativa[1:]
        if coluna not in string.ascii_uppercase[:TAMANHO] or not linha.isdigit():
            print("Coordenada inválida!")
            continue

        x, y = int(linha), string.ascii_uppercase.index(coluna)
        if x < 0 or x >= TAMANHO:
            print("Linha inválida!")
            continue

        tentativas += 1
        if tabuleiro[x][y] == "N":
            print("💥 Acertou um navio!")
            tabuleiro[x][y] = "X"
            acertos += 1
        elif tabuleiro[x][y] in ["X", "O"]:
            print("Você já tentou essa posição!")
        else:
            print("🌊 Água!")
            tabuleiro[x][y] = "O"

        imprimir_tabuleiro(tabuleiro)

    print(f"\n🏆 Parabéns! Você afundou todos os navios em {tentativas} tentativas.")

if __name__ == "__main__":
    jogar()
