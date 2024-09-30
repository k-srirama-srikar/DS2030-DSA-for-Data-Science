def steps(position:tuple, station:tuple, sum=0) -> int:
    '''This is the recursive function that will be called during both case1 and case 2'''
    if position == station:
        # base case is when the positions become the same
        sum += 1
        return sum
    else:
        if position[0] > station[0]:
            sum = steps((position[0]-1,position[1]), station, sum)
            # recursive call
        if position[1] > station[1]:
            sum = steps((position[0],position[1]-1), station, sum)
            # recursive call
    return sum
