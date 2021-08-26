def central(board, round):
    """
    Process machines moves when it is second to move and human's first move is B1
    Parameters: board, move (counts the number of round played)
    Return: board
    """

    if round == 1:
        board["B"][0] = "X"

    if round == 2:
        if board["B"][1] == "O" and board["B"][0] == "X":
            if board["A"][0] == "O":
                board["C"][2] = "X"
            elif board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][1] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
            elif board["C"][2] == "O":
                board["A"][0] = "X"
    
    if round == 3:
        if board["A"][0] == board["B"][1] == "O" and board["B"][0] == board["C"][2] == "X":
            if board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][1] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"                
            elif board["B"][2] == "O":
                board["C"][0] = "X"
        
        elif board["A"][1] == board["B"][1] == "O" and board["B"][0] == board["C"][1] == "X":
            if board["A"][0] == "O":
                board["A"][2] = "X"
            elif board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"                
            elif board["C"][2] == "O":
                board["A"][0] = "X"
        
        elif board["B"][1] == board["A"][2] == "O" and board["B"][0] == board["C"][0] == "X":
            if board["A"][0] == "O":
                board["C"][2] = "X"
            elif board["A"][1] == "O":
                board["A"][0] = "X"
            elif board["C"][1] == "O":
                board["A"][0] = "X"
            elif board["B"][2] == "O":
                board["A"][0] = "X"                
            elif board["C"][2] == "O":
                board["A"][0] = "X"
        
        elif board["B"][1] == board["B"][2] == "O" and board["A"][0] == board["B"][0] == "X":
            if board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][1] == "O":
                board["C"][0] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"                
            elif board["C"][2] == "O":
                board["C"][0] = "X"
        
        elif (board["C"][0] == board["B"][1] == "O" and board["B"][0] == board["A"][2] == "X") or\
             (board["C"][1] == board["B"][1] == "O" and board["B"][0] == board["A"][1] == "X") or\
             (board["B"][1] == board["C"][2] == "O" and board["B"][0] == board["A"][0] == "X"):

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
                            "A": [c0, c1, c2],
                            "B": [b0, b1, b2],
                            "C": [a0, a1, a2]
                        }

            transitBoard = central(adaptedBoard, round)

            c0 = transitBoard.get("A")[0]
            c1 = transitBoard.get("A")[1]
            c2 = transitBoard.get("A")[2]
            b0 = transitBoard.get("B")[0]
            b1 = transitBoard.get("B")[1]
            b2 = transitBoard.get("B")[2]
            a0 = transitBoard.get("C")[0]
            a1 = transitBoard.get("C")[1]
            a2 = transitBoard.get("C")[2]

            board = {
                            " ": ["1", "2", "3"],
                            "A": [a0, a1, a2],
                            "B": [b0, b1, b2],
                            "C": [c0, c1, c2]
                        }
        
    if round == 4:
        if board["A"][0] == board["C"][0] == board["B"][1] == "O" and board["B"][0] == board["A"][2] == board["C"][2] == "X":
            if board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"
       
        elif board["A"][0] == board["A"][1] == board["B"][1] == "O" and board["B"][0] == board["C"][1] == board["C"][2] == "X":
            if board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"
       
        elif board["A"][0] == board["B"][1] == board["C"][1] == "O" and board["B"][0] == board["A"][1] == board["C"][2] == "X":
            if board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
       
        elif board["A"][0] == board["B"][1] == board["A"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][2] == "X":
            if board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"
        
        elif board["A"][0] == board["B"][1] == board["B"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][2] == "X":
            if board["A"][1] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
        
        elif board["A"][0] == board["A"][1] == board["B"][1] == "O" and board["B"][0] == board["C"][1] == board["A"][2] == "X":
            if board["C"][0] == "O":
                board["C"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][2] = "X"
        
        elif board["C"][0] == board["A"][1] == board["B"][1] == "O" and board["B"][0] == board["C"][1] == board["A"][2] == "X":
            if board["A"][0] == "O":
                board["C"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["A"][0] = "X"

        elif board["A"][1] == board["B"][1] == board["A"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][1] == "X":
            if board["B"][2] == "O":
                board["A"][0] = "X"
            elif board["C"][2] == "O":
                board["A"][0] = "X"

        elif board["A"][1] == board["B"][1] == board["B"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][1] == "X":
            if board["A"][0] == "O":
                board["C"][2] = "X"
            elif board["A"][2] == "O":
                board["A"][0] = "X"
            elif board["C"][2] == "O":
                board["A"][0] = "X"

        elif board["A"][1] == board["B"][1] == board["C"][2] == "O" and board["A"][0] == board["B"][0] == board["C"][1] == "X":
            if board["C"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"

        elif board["A"][0] == board["B"][1] == board["A"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][2] == "X":
            if board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"

        elif board["C"][0] == board["B"][1] == board["B"][2] == "O" and board["A"][0] == board["B"][0] == board["A"][2] == "X":
            if board["A"][1] == "O":
                board["C"][2] = "X"
            elif board["C"][1] == "O":
                board["A"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"

        elif (board["C"][0] == board["C"][1] == board["B"][1] == "O" and board["B"][0] == board["A"][1] == board["A"][2] == "X") or\
             (board["C"][0] == board["B"][1] == board["A"][1] == "O" and board["B"][0] == board["C"][1] == board["A"][2] == "X") or\
             (board["C"][0] == board["B"][1] == board["C"][2] == "O" and board["B"][0] == board["A"][0] == board["A"][2] == "X") or\
             (board["C"][0] == board["B"][1] == board["B"][2] == "O" and board["B"][0] == board["A"][0] == board["A"][2] == "X") or\
             (board["C"][0] == board["C"][1] == board["B"][1] == "O" and board["B"][0] == board["A"][1] == board["C"][2] == "X") or\
             (board["A"][0] == board["C"][1] == board["B"][1] == "O" and board["B"][0] == board["A"][1] == board["C"][2] == "X") or\
             (board["C"][1] == board["B"][1] == board["C"][2] == "O" and board["B"][0] == board["A"][0] == board["A"][1] == "X") or\
             (board["C"][1] == board["B"][1] == board["B"][2] == "O" and board["B"][0] == board["A"][0] == board["A"][1] == "X") or\
             (board["C"][1] == board["B"][1] == board["A"][2] == "O" and board["C"][0] == board["B"][0] == board["A"][1] == "X") or\
             (board["A"][0] == board["B"][1] == board["A"][2] == "O" and board["B"][0] == board["C"][0] == board["C"][2] == "X"):

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
                            "A": [c0, c1, c2],
                            "B": [b0, b1, b2],
                            "C": [a0, a1, a2]
                        }

            transitBoard = central(adaptedBoard, round)

            c0 = transitBoard.get("A")[0]
            b0 = transitBoard.get("A")[1]
            a0 = transitBoard.get("A")[2]
            c1 = transitBoard.get("B")[0]
            b1 = transitBoard.get("B")[1]
            a1 = transitBoard.get("B")[2]
            c2 = transitBoard.get("C")[0]
            b2 = transitBoard.get("C")[1]
            a2 = transitBoard.get("C")[2]

            board = {
                            " ": ["1", "2", "3"],
                            "A": [a0, b0, c0],
                            "B": [a1, b1, c1],
                            "C": [a2, b2, c2]
                        }

    return board