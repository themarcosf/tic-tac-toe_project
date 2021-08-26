def diagonalA0(board, round):
    """
    Process machines moves when it is second to move and human's first move is A0
    Parameters: board, move (counts the number of round played)
    Return: board
    """

    if round == 1:
        board["B"][1] = "X"

    if round == 2:
        if board["A"][0] == "O" and board["B"][1] == "X":
            if board["B"][0] == "O":
                board["C"][0] = "X"
            elif board["C"][0] == "O":
                board["B"][0] = "X"
            elif board["A"][1] == "O":
                board["A"][2] = "X"
            elif board["C"][1] == "O":
                board["B"][0] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"
            elif board["C"][2] == "O":
                board["B"][0] = "X"
    
    if round == 3:
        if board["A"][0] == board["B"][0] == "O" and board["C"][0] == board["B"][1] == "X":
            if board["A"][1] == "O":
                board["A"][2] = "X"
            elif board["C"][1] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"                
            elif board["C"][2] == "O":
                board["A"][2] = "X"
        
        elif board["A"][0] == board["C"][0] == "O" and board["B"][0] == board["B"][1] == "X":
            if board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"
            elif board["C"][2] == "O":
                board["B"][2] = "X"
        
        elif board["A"][0] == board["A"][1] == "O" and board["B"][1] == board["A"][2] == "X":
            if board["B"][0] == "O":
                board["C"][0] = "X"
            elif board["C"][0] == "O":
                board["B"][0] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
            elif board["C"][2] == "O":
                board["C"][0] = "X"
        
        elif board["A"][0] == board["C"][1] == "O" and board["B"][0] == board["B"][1] == "X":
            if board["C"][0] == "O":
                board["B"][2] = "X"
            elif board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"
            elif board["C"][2] == "O":
                board["B"][2] = "X"      
        
        elif board["A"][0] == board["A"][2] == "O" and board["A"][1] == board["B"][1] == "X":
            if board["B"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["B"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"      
        
        elif board["A"][0] == board["B"][2] == "O" and board["A"][1] == board["B"][1] == "X":
            if board["B"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["A"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"   

        elif board["A"][0] == board["C"][2] == "O" and board["B"][0] == board["B"][1] == "X":
            if board["C"][0] == "O":
                board["B"][2] = "X"
            elif board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"

    if round == 4:
        if board["A"][0] == board["B"][0] == board["A"][2] == "O" and board["C"][0] == board["A"][1] == board["B"][1] == "X":
            if board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"
        
        elif board["A"][0] == board["C"][0] == board["B"][2] == "O" and board["B"][0] == board["A"][1] == board["B"][1] == "X":
            if board["C"][1] == "O":
                board["C"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"
        
        elif board["A"][0] == board["C"][0] == board["A"][1] == "O" and board["B"][0] == board["B"][1] == board["A"][2] == "X":
            if board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["B"][2] = "X"
                   
        elif board["A"][0] == board["C"][1] == board["B"][2] == "O" and board["B"][0] == board["B"][1] == board["A"][2] == "X":
            if board["C"][0] == "O":
                board["C"][2] = "X"
            elif board["A"][1] == "O":
                board["C"][0] = "X"
            elif board["C"][2] == "O":
                board["C"][0] = "X"
        
        elif board["A"][0] == board["C"][1] == board["A"][2] == "O" and board["B"][0] == board["A"][1] == board["B"][1] == "X":
            if board["C"][0] == "O":
                board["B"][2] = "X"
            elif board["C"][2] == "O":
                board["A"][1] = "X"
            elif board["C"][2] == "O":
                board["B"][2] = "X"
        
        elif board["A"][0] == board["C"][1] == board["B"][2] == "O" and board["C"][0] == board["A"][1] == board["B"][1] == "X":
            if board["B"][1] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["A"][2] = "X"

        elif board["A"][0] == board["B"][2] == board["C"][2] == "O" and board["B"][0] == board["B"][1] == board["A"][2] == "X":
            if board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["A"][1] == "O":
                board["C"][0] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
        
    return board

def diagonalC2(board, move):
    """
    Process machines moves when it is second to move and human's first move is C2
    Done by gyrating the board 180° clock-wise
    Parameters: board, move (counts the number of round played)
    Return: board
    """
    newKeyC = board.get("A")
    newKeyC.reverse()
    newKeyB = board.get("B")
    newKeyB.reverse()
    newKeyA = board.get("C")
    newKeyA.reverse()

    adaptedBoard = {
                    " ": ["3", "2", "1"],
                    "C": newKeyC,
                    "B": newKeyB,
                    "A": newKeyA
                }

    transitBoard = diagonalA0(adaptedBoard, move)

    finalKeyA = transitBoard.get("C")
    finalKeyA.reverse()
    finalKeyB = transitBoard.get("B")
    finalKeyB.reverse()
    finalKeyC = transitBoard.get("A")
    finalKeyC.reverse()

    board = {
                    " ": ["1", "2", "3"],
                    "A": finalKeyA,
                    "B": finalKeyB,
                    "C": finalKeyC
            }

    return board

def diagonalC0(board, move):
    """
    Process machines moves when it is second to move and human's first move is C0
    Done by creating a mirror-image of the board
    Parameters: board, move (counts the number of round played)
    Return: board
    """
    a0 = board.get("A")[0]
    a1 = board.get("A")[1]
    a2 = board.get("A")[2]
    b0 = board.get("B")[0]
    b1 = board.get("B")[1]
    b2 = board.get("B")[2]
    c0 = board.get("C")[0]
    c1 = board.get("C")[1]
    c2 = board.get("C")[2]

    adaptedBoard = {
                    " ": ["1", "2", "3"],
                    "A": [c0, b0, a0],
                    "B": [c1, b1, a1],
                    "C": [c2, b2, a2]
                }

    transitBoard = diagonalA0(adaptedBoard, move)

    c0 = transitBoard.get("A")[0]
    b0 = transitBoard.get("A")[1]
    a0 = transitBoard.get("A")[2]
    c1 = transitBoard.get("B")[0]
    b1 = transitBoard.get("B")[1]
    a1 = transitBoard.get("B")[2]
    c2 = transitBoard.get("C")[0]
    b2 = transitBoard.get("C")[1]
    a2 = transitBoard.get("C")[2]

    finalBoard = {
                    " ": ["1", "2", "3"],
                    "A": [a0, a1, a2],
                    "B": [b0, b1, b2],
                    "C": [c0, c1, c2]
                }

    return finalBoard

def diagonalA2(board, move):
    """
    Process machines moves when it is second to move and human's first move is A2
    Done by creating a mirror-image of the board
    Parameters: board, move (counts the number of round played)
    Return: board
    """
    a0 = board.get("A")[0]
    a1 = board.get("A")[1]
    a2 = board.get("A")[2]
    b0 = board.get("B")[0]
    b1 = board.get("B")[1]
    b2 = board.get("B")[2]
    c0 = board.get("C")[0]
    c1 = board.get("C")[1]
    c2 = board.get("C")[2]

    adaptedBoard = {
                    " ": ["1", "2", "3"],
                    "A": [a2, b2, c2],
                    "B": [a1, b1, c1],
                    "C": [a0, b0, c0]
                }

    transitBoard = diagonalA0(adaptedBoard, move)

    a2 = transitBoard.get("A")[0]
    b2 = transitBoard.get("A")[1]
    c2 = transitBoard.get("A")[2]
    a1 = transitBoard.get("B")[0]
    b1 = transitBoard.get("B")[1]
    c1 = transitBoard.get("B")[2]
    a0 = transitBoard.get("C")[0]
    b0 = transitBoard.get("C")[1]
    c0 = transitBoard.get("C")[2]

    finalBoard = {
                    " ": ["1", "2", "3"],
                    "A": [a0, a1, a2],
                    "B": [b0, b1, b2],
                    "C": [c0, c1, c2]
                }

    return finalBoard