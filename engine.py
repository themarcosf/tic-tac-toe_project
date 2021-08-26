from tabulate import tabulate

def correctEntryValidation(letter, number):
    if letter not in ["A", "B", "C"] or number not in ["1", "2", "3"]:
        return False
    else:
        return True

def availableEntryValidation(board, letter, number):
    if board[letter][number-1] != "":
        return False
    else:
        return True

def entryValidation(board, letterNumber):
    """
    Parameters: board, human move's coordinates
    Return: valid coordinates
    """
    try:
        letter, number = letterNumber.upper().split()
    except:
        return entryValidation(board, input(f"Coordenada inválida, digite uma válida: "))
    
    if correctEntryValidation(letter, number):
        if availableEntryValidation(board, letter, int(number)):
            return letter, int(number)
        else:
            return entryValidation(board, input(f"Coordenada indisponível, digite uma livre: ")) 
    else:
        return entryValidation(board, input(f"Coordenada inválida, digite uma válida: "))  

def humanMove(board):
    """
    Ask human's move and updates the board
    Parameters: board
    Return: board
    """
    letter, number = entryValidation(board, input(f"Vez do jogador: "))
    number -=1
    board[letter][number] = "O"

    return board, letter, number

def congratulateWinner(board, playerWon):
    if playerWon == "X":
        print("A máquina ganhou!")
    else:
        printBoard(board)
        print("Parabéns! Você encontrou umas das 9 jogadas logicamente vencedoras. Faltam apenas 8. Continue jogando!")

def printBoard(board):
    print(tabulate(board, headers="keys", tablefmt="fancy_grid"))

def checkWinner(board, player):
    if board["A"].count("X") == 3 or board["A"].count("O") == 3 or \
       board["B"].count("X") == 3 or board["B"].count("O") == 3 or \
       board["C"].count("X") == 3 or board["C"].count("O") == 3:
        congratulateWinner(board, player)
        return True
    
    elif board["A"][0] == board["B"][0] == board["C"][0] and board["A"][0] != "" or \
         board["A"][1] == board["B"][1] == board["C"][1] and board["A"][1] != "" or \
         board["A"][2] == board["B"][2] == board["C"][2] and board["A"][2] != "":
        congratulateWinner(board, player)
        return True
    
    elif board["A"][0] == board["B"][1] == board["C"][2] or board["C"][0] == board["B"][1] == board["A"][2] and board["B"][1] != "":
        congratulateWinner(board, player)
        return True
    return False

def checkTie(board):
    if "" not in board["A"] and "" not in board["B"] and "" not in board["C"]:
        print("O jogo empatou!")
        return True
    else:
        return False

def checkEnding(board, player):
    """
    Checks if human or machine have won or if the match is tied
    Parameters: board, player (last move)
    Return: True (game is finished)/ False (game continues)
    """
    ending = False
    ending = checkWinner(board, player)
    if not ending:
        ending = checkTie(board)
    return ending
