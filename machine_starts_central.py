def central(board, move):
    """
    Process machines moves when it is first to move and its first move is B1
    Parameters: board, move (counts the number of round played)
    Return: board
    """

    if move == 1:
        board["B"][1] = "X"

    if move == 2:
        if board["B"][1] == "X":
            if board["A"][0] == "O":
                board["A"][1] = "X"
            elif board["B"][0] == "O":
                board["A"][0] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["A"][1] == "O":
                board["A"][2] = "X"
            elif board["C"][1] == "O":
                board["C"][2] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"
    
    if move == 3:
        if board["B"][0] == board["B"][1] == "X" and board["A"][0] == "O":
            if board["A"][1] == "O":
                board["C"][1] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["A"][2] == "O":
                board["C"][1] = "X"                
            elif board["B"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"
        
        elif board["A"][0] == board["B"][1] == "X" and board["B"][0] == "O":
            if board["C"][0] == "O":
                board["C"][2] = "X"
            elif board["A"][1] == "O":
                board["C"][2] = "X"
            elif board["C"][1] == "O":
                board["C"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["A"][2] = "X"
        
        elif board["B"][1] == board["C"][1] == "X" and board["C"][0] == "O":
            if board["A"][0] == "O":
                board["A"][1] = "X"
            elif board["B"][0] == "O":
                board["A"][1] = "X"
            elif board["A"][1] == "O":
                board["A"][0] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"
            elif board["C"][2] == "O":
                board["A"][1] = "X"        
        
        elif board["B"][1] == board["A"][2] == "X" and board["A"][1] == "O":
            if board["A"][0] == "O":
                board["C"][0] = "X"
            elif board["B"][0] == "O":
                board["C"][0] = "X"
            elif board["C"][0] == "O":
                board["B"][0] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
            elif board["C"][2] == "O":
                board["C"][0] = "X"      
        
        elif board["B"][1] == board["C"][2] == "X" and board["C"][1] == "O":
            if board["A"][0] == "O":
                board["B"][0] = "X"
            elif board["B"][0] == "O":
                board["A"][0] = "X"
            elif board["C"][0] == "O":
                board["A"][0] = "X"
            elif board["A"][1] == "O":
                board["A"][0] = "X"
            elif board["A"][2] == "O":
                board["A"][0] = "X"
            elif board["B"][2] == "O":
                board["A"][0] = "X"      
        
        elif board["A"][1] == board["B"][1] == "X" and board["A"][2] == "O":
            if board["A"][0] == "O":
                board["C"][1] = "X"
            elif board["B"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["C"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][1] = "X"
            elif board["C"][2] == "O":
                board["C"][1] = "X"   
        
        elif board["B"][1] == board["C"][2] == "X" and board["B"][2] == "O":
            if board["A"][0] == "O":
                board["A"][1] = "X"
            elif board["B"][0] == "O":
                board["A"][0] = "X"
            elif board["C"][0] == "O":
                board["A"][0] = "X"
            elif board["A"][1] == "O":
                board["A"][0] = "X"
            elif board["C"][1] == "O":
                board["A"][0] = "X"
            elif board["A"][2] == "O":
                board["A"][0] = "X"   
        
        elif board["B"][1] == board["C"][1] == "X" and board["C"][2] == "O":
            if board["A"][0] == "O":
                board["A"][1] = "X"
            elif board["B"][0] == "O":
                board["A"][1] = "X"
            elif board["C"][0] == "O":
                board["A"][1] = "X"
            elif board["A"][1] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["A"][1] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"   

    if move == 4:
        if board["C"][0] == board["A"][1] == board["B"][1] == "X" and board["A"][0] == board["C"][1] == "O":
            if board["B"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"
            elif board["C"][2] == "O":
                board["A"][2] = "X"
        
        elif board["A"][0] == board["B"][1] == board["A"][2] == "X" and board["B"][0] == board["C"][2] == "O":
            if board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["A"][1] == "O":
                board["C"][0] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
        
        elif board["A"][0] == board["B"][1] == board["B"][2] == "X" and board["C"][0] == board["A"][1] == "O":
            if board["B"][0] == "O":
                board["C"][2] = "X"
            elif board["A"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][1] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["B"][0] = "X"
        
        elif board["B"][0] == board["B"][1] == board["A"][2] == "X" and board["C"][0] == board["A"][1] == "O":
            if board["A"][0] == "O":
                board["B"][2] = "X"
            elif board["C"][1] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["B"][2] = "X"
        
        elif board["B"][0] == board["B"][1] == board["C"][2] == "X" and board["A"][0] == board["C"][1] == "O":
            if board["C"][0] == "O":
                board["B"][2] = "X"
            elif board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][2] = "X"
        
        elif board["A"][1] == board["B"][1] == board["C"][2] == "X" and board["C"][1] == board["A"][2] == "O":
            if board["A"][0] == "O":
                board["B"][0] = "X"
            elif board["B"][0] == "O":
                board["A"][0] = "X"
            elif board["C"][0] == "O":
                board["A"][0] = "X"
            elif board["B"][2] == "O":
                board["A"][0] = "X"
        
        elif board["A"][1] == board["B"][1] == board["C"][2] == "X" and board["A"][0] == board["B"][2] == "O":
            if board["B"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["C"][0] = "X"
            elif board["A"][2] == "O":
                board["C"][1] = "X"
        
        elif board["B"][1] == board["C"][1] == board["A"][2] == "X" and board["A"][1] == board["C"][2] == "O":
            if board["A"][0] == "O":
                board["C"][0] = "X"
            elif board["B"][0] == "O":
                board["C"][0] = "X"
            elif board["C"][0] == "O":
                board["B"][0] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"

    if move == 5:
        if board["C"][0] == board["A"][1] == board["B"][1] == board["B"][2] == "X" and board["A"][0] == board["C"][1] == board["A"][2] == "O":
            if board["B"][0] == "O":
                board["C"][2] = "X"
            elif board["C"][2] == "O":
                board["B"][0] = "X"
        
        elif board["A"][0] == board["B"][1] == board["C"][1] == board["A"][2] == "X" and board["B"][0] == board["C"][0] == board["C"][2] == "O":
            if board["A"][1] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][1] = "X"
        
        elif board["A"][0] == board["B"][1] == board["C"][1] == board["B"][2] == "X" and board["C"][0] == board["A"][1] == board["C"][2] == "O":
            if board["B"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][0] = "X"
        
        elif board["B"][0] == board["B"][1] == board["A"][2] == board["C"][2] == "X" and board["C"][0] == board["A"][1] == board["B"][2] == "O":
            if board["A"][0] == "O":
                board["C"][1] = "X"
            elif board["C"][1] == "O":
                board["A"][0] = "X"
        
        elif board["B"][0] == board["B"][1] == board["A"][2] == board["C"][2] == "X" and board["A"][0] == board["C"][1] == board["B"][2] == "O":
            if board["A"][1] == "O":
                board["C"][0] = "X"
            elif board["C"][0] == "O":
                board["A"][1] = "X"
        
        elif board["B"][0] == board["A"][1] == board["B"][1] == board["C"][2] == "X" and board["A"][0] == board["C"][1] == board["A"][2] == "O":
            if board["C"][0] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["C"][0] = "X"
        
        elif board["C"][0] == board["A"][1] == board["B"][1] == board["C"][2] == "X" and board["A"][0] == board["C"][1] == board["B"][2] == "O":
            if board["B"][0] == "O":
                board["A"][2] = "X"
            elif board["A"][2] == "O":
                board["B"][0] = "X"

        elif board["B"][0] == board["B"][1] == board["C"][1] == board["A"][2] == "X" and board["C"][0] == board["A"][1] == board["C"][2] == "O":
            if board["A"][0] == "O":
                board["B"][2] = "X"
            elif board["B"][2] == "O":
                board["A"][0] = "X"

    return board