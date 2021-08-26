import random
import time
import engine
import machine_starts_diagonals as msd
import machine_starts_verticals as msv
import machine_starts_central as msc
import human_starts_diagonals as hsd
import human_starts_verticals as hsv
import human_starts_central as hsc

board = {
                " ": ["1", "2", "3"],
                "A": ["", "", ""],
                "B": ["", "", ""],
                "C": ["", "", ""]
            }

endGame = False
firstMove = 'machine'
round = 1

startGame = input("Bem vindo! Deseja iniciar o jogo? [S]im ou [N]ão: ")

while startGame.upper() not in ("S", "N"):
    startGame = input("A informação não é válida. Digite [S] para inicial o jogo ou [N] para sair: ")

if startGame.upper() == "N":
    print("Que pena, volte mais tarde!")
    exit()

elif startGame.upper() == "S":
    oddsEvens = input('\nEntão vamos sortear quem irá começar. Escolha [P]ar ou [I]mpar: ')
    while oddsEvens.upper() not in ("P", "I"):
        oddsEvens = input('Digite [P] para escolher um número par ou [I] para um número ímpar: ')
    randomChoice = random.randint(1,6)
    print('\nO número sorteado foi: ', end="")
    for i in range(randomChoice):
        print(i+1, sep=",", end=" ", flush=True)
        time.sleep(1)

    if randomChoice % 2 == 0:
        if oddsEvens.upper() == "P":
            firstMove = "human"
            print("- Você será o primeiro a jogar.\n")
        else:
            print("- A máquina será o primeiro a jogar.\n")
    else:
        if oddsEvens.upper() == "I":
            firstMove = "human"
            print("- Você será o primeiro a jogar.\n")
        else:
            print("- A máquina será o primeiro a jogar.\n")
    
    print("Dica: Existem 9 jogadas em que é logicamente possível ganhar do computador. Em todas as demais ou o computador ganha ou o jogo empata. Divirta-se tentando encontrá-las!! =]")
    print("Atenção: Digite as coordenadas da sua jogada no formato letra e número [Ex: 'A 1', 'B 2', 'C 3']\n")

if firstMove == "human":
    engine.printBoard(board)
    board, letter, number = engine.humanMove(board)

    humanFirstMove = (letter, number)
    if humanFirstMove == ("A", 0):
        boardTrail = hsd.diagonalA0
    elif humanFirstMove == ("C", 2):
        boardTrail = hsd.diagonalC2
    elif humanFirstMove == ("C", 0):
        boardTrail = hsd.diagonalC0
    elif humanFirstMove == ("A", 2):
        boardTrail = hsd.diagonalA2
    elif humanFirstMove == ("B", 0):
        boardTrail = hsv.verticalB0
    elif humanFirstMove == ("B", 2):
        boardTrail = hsv.verticalB2
    elif humanFirstMove == ("C", 1):
        boardTrail = hsv.verticalC1
    elif humanFirstMove == ("A", 1):
        boardTrail = hsv.verticalA1
    elif humanFirstMove == ("B", 1):
        boardTrail = hsc.central
    board = boardTrail(board, round)

else:
    machineFirstMove = random.randint(1,9)
    if machineFirstMove == 1:
        boardTrail = msc.central
    elif machineFirstMove == 2:
        boardTrail = msd.diagonalA0
    elif machineFirstMove == 3:
        boardTrail = msd.diagonalC2
    elif machineFirstMove == 4:
        boardTrail = msd.diagonalC0
    elif machineFirstMove == 5:
        boardTrail = msd.diagonalA2
    elif machineFirstMove == 6:
        boardTrail = msv.verticalB0
    elif machineFirstMove == 7:
        boardTrail = msv.verticalB2
    elif machineFirstMove == 8:
        boardTrail = msv.verticalC1
    elif machineFirstMove == 9:
        boardTrail = msv.verticalA1
    board = boardTrail(board, round)

    engine.printBoard(board)
    board, _, _ = engine.humanMove(board)

while True:
    if firstMove == "human":
        round += 1
        engine.printBoard(board)
        board, _, _ = engine.humanMove(board)
        endGame = engine.checkEnding(board, "O")
        if endGame:
            break
        board = boardTrail(board, round)
        endGame = engine.checkEnding(board, "X")
        if endGame:
            break

    else:
        round += 1
        board = boardTrail(board, round)
        engine.printBoard(board)
        endGame = engine.checkEnding(board, "X")
        if endGame:
            break
        board, _, _ = engine.humanMove(board)
        endGame = engine.checkEnding(board, "O")
        if endGame:
            break
