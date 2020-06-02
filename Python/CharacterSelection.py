def street_fighter_selection(fighters, initial_position, moves):
    xCoord = initial_position[0]
    yCoord = initial_position[1]

    output = []

    for move in moves:
        if move.lower() == "up" and yCoord > 0:
            yCoord -= 1     
        elif move.lower() =="down" and yCoord < 1:
            yCoord += 1
        elif move.lower() == "left":
            xCoord -= 1
        elif move.lower() == "right":  
            xCoord += 1
        
        if xCoord >= len(fighters[0]):
            xCoord = 0
        elif xCoord < 0:
            xCoord = len(fighters[0])-1
        
        output.append(fighters[yCoord][xCoord])
    
    return output
        

fighters = [["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]]
moves = ["left"]*7


street_fighter_selection(fighters,(0,0), moves)